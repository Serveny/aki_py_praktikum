from prelude import *
from move import Move, textToMoves
from series import Series

# Holds game arena and logic, the AI needs to follow the game
class Game:
    size: int
    arena: GameArena
    player: Player = "x"
    enemy: Player = "o"
    archive: list[GameArena] = []
    lastMove: Move
    kickout: Mark = "-"

    # Constructor: Inits a empty game field
    def __init__(self, size: int) -> None:
        if size < 4:
            raise Exception("Size too small. Must be at least 4.")
        self.size = size
        self.arena = [["-" for _ in range(size)] for _ in range(size)]
        self.archiveCurrentArena()

    # Raises exception
    def raiseIllegalMoveException(self, number: int) -> None:
        raise Exception(
            f"Move index {number} outside of game field. Must be between 1 and {self.size}."
        )

    def archiveCurrentArena(self) -> None:
        self.archive.append([[item for item in row] for row in self.arena])

    # Gets one field of game field
    def getField(self, coords: Coords) -> Mark:
        return self.arena[coords[0]][coords[1]]

    # Sets one field and toggles current player
    def setField(self, coords: Coords) -> None:
        self.arena[coords[0]][coords[1]] = self.player

    # Executes all given moves
    def executeMoves(self, moves: list[Move]) -> None:
        for move in moves:
            self.execute(move)
            self.archiveCurrentArena()
            self.toggleCurrentPlayer()
        self.lastMove = moves[-1] if len(moves) > 0 else Move("R", self.size)

    # Executes one move
    def execute(self, move: Move) -> None:
        self.arena = self.archive[-1].copy()
        coords = self.indexBy(move)
        if self.getField(coords) != "-":
            self.moveFields(move, coords)
        self.setField(coords)

    # Gets x,y index coordinates by move
    def indexBy(self, move: Move) -> Coords:
        if move.number < 1 or move.number > self.size:
            self.raiseIllegalMoveException(move.number)
        x = 0
        y = 0
        if move.isVertical():
            x = 0 if move.direction == "T" else (self.size - 1)
            y = move.number - 1
        else:
            x = move.number - 1
            y = 0 if move.direction == "L" else (self.size - 1)
        return (x, y)

    # Moves fields in needed direction
    def moveFields(self, move: Move, coords: Coords) -> None:
        match move.direction:
            case "L":
                self.moveInRowToRight(coords[0])
            case "R":
                self.moveInRowToLeft(coords[0])
            case "T":
                self.moveInColToBottom(coords[1])
            case "B":
                self.moveInColToTop(coords[1])

    # Finds index of first/last occurence of given mark in row
    def findIndexInRow(self, rowNo: int, mark: Mark, findLast: bool) -> Optional[int]:
        for i in range(self.size - 1, -1, -1) if findLast else range(self.size):
            if self.arena[rowNo][i] == mark:
                return i
        return None

    # Finds index of first/last occurence of given mark in column
    def findIndexInCol(self, colNo: int, mark: Mark, findLast: bool) -> Optional[int]:
        for i in range(self.size - 1, -1, -1) if findLast else range(self.size):
            if self.arena[i][colNo] == mark:
                return i
        return None

    # Save field which was kicked out
    def addKickout(self, endI: Optional[int], coords: Coords) -> None:
        if endI == None:
            self.kickout = self.getField(coords)

    # Moves items in row one index right until free field occurs
    def moveInRowToRight(self, rowI: int) -> None:
        endI = self.findIndexInRow(rowI, "-", False)
        self.addKickout(endI, (rowI, self.size - 1))
        for i in reversed(range(1, self.size if endI == None else (endI + 1))):
            self.arena[rowI][i] = self.arena[rowI][i - 1]

    # Moves items in row one index left until free field occurs
    def moveInRowToLeft(self, rowI: int) -> None:
        endI = self.findIndexInRow(rowI, "-", True)
        self.addKickout(endI, (rowI, 0))
        for i in range(0 if endI == None else endI, self.size - 1):
            self.arena[rowI][i] = self.arena[rowI][i + 1]

    # Moves items in column one index down until free field occurs
    def moveInColToBottom(self, colI: int) -> None:
        endI = self.findIndexInCol(colI, "-", False)
        self.addKickout(endI, (self.size - 1, colI))
        for i in reversed(range(1, self.size if endI == None else (endI + 1))):
            self.arena[i][colI] = self.arena[i - 1][colI]

    # Moves items in column one index up until free field occurs
    def moveInColToTop(self, colI: int) -> None:
        endI = self.findIndexInCol(colI, "-", True)
        self.addKickout(endI, (0, colI))
        for i in range(0 if endI == None else endI, self.size - 1):
            self.arena[i][colI] = self.arena[i + 1][colI]

    # Returns other (not current) player
    def otherPlayer(self) -> Player:
        return "x" if self.player == "o" else "o"

    # Toggles the property to another player
    def toggleCurrentPlayer(self) -> None:
        self.enemy = self.player
        self.player = self.otherPlayer()

    # Is enemy kickout
    def isEnemyKickout(self) -> bool:
        return self.kickout == self.enemy

    # Return arena as string
    def arenaStr(self) -> str:
        return "| " + " |\n| ".join([" | ".join(row) for row in self.arena]) + " |"

    # Are two arenas filled with the same elements at same position?
    def isSame(self, arena: GameArena) -> bool:
        for y in range(self.size):
            for x in range(self.size):
                if self.arena[y][x] != arena[y][x]:
                    return False
        return True

    # Checks if the current player has lost
    def isLooseBySame(self) -> bool:
        return any(self.isSame(arena) for arena in self.archive[:-2])

    # Checks if one of the player has more on field
    def whoWon(self) -> Optional[Player]:
        xCount = 0
        oCount = 0
        for i in range(self.size):
            horizontal = self.arena[i][0]
            vertical = self.arena[0][i]

            for u in range(1, self.size):
                if self.arena[i][u] != horizontal:
                    horizontal = "-"
                if self.arena[u][i] != vertical:
                    vertical = "-"

            if vertical == "x":
                xCount += 1
            elif vertical == "o":
                oCount += 1
            if horizontal == "x":
                xCount += 1
            elif horizontal == "o":
                oCount += 1
        return None if xCount == oCount else ("x" if xCount > oCount else "o")

    # Executes move and checks if it is allowed
    def isAllowedMove(self, move: Move) -> bool:
        self.execute(move)
        return self.whoWon() != self.otherPlayer() and not self.isLooseBySame()

    # Find series of points in a row or column
    def findSeries(self) -> tuple[list[Series], list[Series]]:
        resX = []
        resY = []
        for i in range(self.size):
            seriesX = Series()
            seriesY = Series()
            for u in range(self.size):
                seriesX = self.extendSeries(resX, seriesX, (u, i), self.arena[i][u])
                seriesY = self.extendSeries(resY, seriesY, (i, u), self.arena[u][i])
        return (resX, resY)

    # Detects point series from start to end and adds it to result (Manipulates res & series)
    def extendSeries(
        self, res: list[Series], series: Series, coords: Coords, mark: Mark
    ) -> Series:
        if mark == "-":
            if series.player != "-":
                if series.length > 1:
                    res.append(series)
                series = Series()
        else:
            if series.player != "-" and mark == series.player:
                series.end = coords
                series.length += 1
            else:
                if series.player != "-" and series.length > 1:
                    res.append(series)
                series = Series(mark, 1, coords, coords)
        return series

    # Counts player marks in arena
    def count(self, player: Player) -> int:
        count = 0
        for i in range(self.size):
            for u in range(self.size):
                if self.arena[i][u] == player:
                    count += 1
        return count

    def enemyCount(self) -> int:
        return self.count(self.otherPlayer())


# Tests
class GameTests(unittest.TestCase):
    def testEmptyInit(self) -> None:
        self.assertEqual(
            Game(4).arena,
            [
                ["-", "-", "-", "-"],
                ["-", "-", "-", "-"],
                ["-", "-", "-", "-"],
                ["-", "-", "-", "-"],
            ],
        )

    def testErrorInit(self) -> None:
        with self.assertRaises(Exception):
            Game(2)

    def testIndexByMove(self) -> None:
        ttt = Game(4)
        self.assertEqual(ttt.indexBy(Move("T1")), (0, 0))
        self.assertEqual(ttt.indexBy(Move("B4")), (3, 3))
        self.assertEqual(ttt.indexBy(Move("L2")), (1, 0))
        self.assertEqual(ttt.indexBy(Move("R2")), (1, 3))

    def testMoves(self) -> None:
        ttt = Game(4)
        ttt.executeMoves(textToMoves("T1\nT2\nT3\nT4\nB3\nB1\nR3\nR2\n".split("\n")))
        self.assertEqual(
            ttt.arena,
            [
                ["x", "o", "x", "o"],
                ["-", "-", "-", "o"],
                ["-", "-", "-", "x"],
                ["o", "-", "x", "-"],
            ],
        )

        # Test find index in row
        self.assertEqual(ttt.findIndexInRow(2, "-", False), 0)
        self.assertEqual(ttt.findIndexInRow(3, "-", False), 1)
        self.assertEqual(ttt.findIndexInRow(3, "-", True), 3)
        self.assertEqual(ttt.findIndexInRow(3, "x", True), 2)

        # Test find index in column
        self.assertEqual(ttt.findIndexInCol(0, "o", False), 3)
        self.assertEqual(ttt.findIndexInCol(0, "-", False), 1)
        self.assertEqual(ttt.findIndexInCol(0, "-", True), 2)
        self.assertEqual(ttt.findIndexInCol(0, "x", True), 0)

        # Test move elements in row right
        ttt.moveInRowToRight(0)
        self.assertEqual(ttt.arena[0], ["x", "x", "o", "x"])
        ttt.moveInRowToRight(3)
        self.assertEqual(ttt.arena[3], ["o", "o", "x", "-"])

        # Test move elements in row left
        ttt.moveInRowToLeft(0)
        self.assertEqual(ttt.arena[0], ["x", "o", "x", "x"])
        ttt.moveInRowToLeft(2)
        self.assertEqual(ttt.arena[2], ["-", "-", "x", "x"])

        self.assertEqual(
            ttt.arena,
            [
                ["x", "o", "x", "x"],
                ["-", "-", "-", "o"],
                ["-", "-", "x", "x"],
                ["o", "o", "x", "-"],
            ],
        )

        # Test move elements in column to bottom
        ttt.moveInColToBottom(1)
        self.assertEqual(column(ttt.arena, 1), ["o", "o", "-", "o"])
        ttt.moveInColToBottom(3)
        self.assertEqual(column(ttt.arena, 3), ["x", "x", "o", "x"])

        # Test move elements in column to top
        ttt.moveInColToTop(0)
        self.assertEqual(column(ttt.arena, 0), ["x", "-", "o", "o"])
        ttt.moveInColToTop(3)
        self.assertEqual(column(ttt.arena, 3), ["x", "o", "x", "x"])

    def testMovesExample(self) -> None:
        ttt = Game(4)
        ttt.executeMoves(textToMoves("T2\nT2\nR1\nR1\nL1\nR1\n".split("\n")))
        self.assertEqual(
            ttt.arena,
            [
                ["o", "x", "o", "o"],
                ["-", "x", "-", "-"],
                ["-", "-", "-", "-"],
                ["-", "-", "-", "-"],
            ],
        )

    def testArenaString(self) -> None:
        ttt = Game(4)
        ttt.executeMoves(textToMoves("T2\nT2\nR1\nR1\nL1\nR1\n".split("\n")))
        self.assertEqual(
            ttt.arenaStr(),
            "| o | x | o | o |\n| - | x | - | - |\n| - | - | - | - |\n| - | - | - | - |",
        )

    def testIsLooseBySame(self) -> None:
        ttt = Game(4)
        ttt.executeMoves(textToMoves("L1\nR1\nL1\nR1\nL1\n".split("\n")))
        self.assertEqual(ttt.isLooseBySame(), False)
        ttt.execute(Move("R1"))
        self.assertEqual(ttt.isLooseBySame(), True)

    def testIsLooseBySame2(self) -> None:
        ttt = Game(4)
        ttt.executeMoves(
            textToMoves("R4\nR4\nR4\nR4\nR4\nB2\nB2\nB2\nB2\nB2\n".split("\n"))
        )
        self.assertEqual(ttt.isLooseBySame(), True)

    def testWhoWon(self) -> None:
        ttt = Game(4)
        ttt.executeMoves(textToMoves("L1\nR1\nL1\nR1\nT3\nB4\n".split("\n")))
        self.assertEqual(ttt.whoWon(), None)
        ttt.execute(Move("T4"))

        self.assertEqual(ttt.whoWon(), "x")

    def testFindSeries(self) -> None:
        ttt = Game(4)
        ttt.executeMoves(textToMoves("L1\nL2\nL1\nL3\nL1\n".split("\n")))
        series = ttt.findSeries()
        self.assertEqual(series[0], [Series("x", 3, (0, 0), (2, 0))])
        self.assertEqual(series[1], [Series("o", 2, (0, 1), (0, 2))])

    def testCount(self) -> None:
        ttt = Game(4)
        ttt.executeMoves(textToMoves("L1\nL2\nL1\nL3\nL1\n".split("\n")))
        self.assertEqual(ttt.count("x"), 3)
        self.assertEqual(ttt.count("o"), 2)

    def testKickoutHorizontal(self) -> None:
        ttt = Game(4)
        ttt.executeMoves(textToMoves("L1\nL1\nL1\nL1\nL1\n".split("\n")))
        self.assertEqual(ttt.kickout, "x")
        ttt.execute(Move("R1"))
        self.assertEqual(ttt.kickout, "x")

    def testKickoutVertical(self) -> None:
        ttt = Game(4)
        ttt.executeMoves(textToMoves("T1\nT1\nT1\nT1\nT1\n".split("\n")))
        self.assertEqual(ttt.kickout, "x")
        ttt.execute(Move("B1"))
        self.assertEqual(ttt.kickout, "x")
