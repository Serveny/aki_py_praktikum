from prelude import *
from move import Move, textToMoves


# Holds game arena and game logic
class Game:
    size: int
    arena: GameArena
    currentPlayer: Player = "x"

    # Constructor: Inits a empty game field
    def __init__(self, size: int) -> None:
        if size < 4:
            raise Exception("Size too small. Must be at least 4.")
        self.size = size
        self.arena = [["-" for _ in range(size)] for _ in range(size)]

    # Raises exception
    def raiseIllegalMoveException(self, number: int) -> None:
        raise Exception(
            f"Move index {number} outside of game field. Must be between 1 and {len(self.arena)}."
        )

    # Gets one field of game field
    def getField(self, coords: Coords) -> Mark:
        return self.arena[coords[0]][coords[1]]

    # Sets one field and toggles current player
    def setField(self, coords: Coords) -> None:
        self.arena[coords[0]][coords[1]] = self.getAndToggleCurrentPlayer()

    # Gets x,y index coordinates by move
    def indexBy(self, move: Move) -> Coords:
        if move.number < 1 or move.number > len(self.arena):
            self.raiseIllegalMoveException(move.number)
        x = 0
        y = 0
        if move.isVertical():
            x = 0 if move.direction == "T" else (len(self.arena) - 1)
            y = move.number - 1
        else:
            x = move.number - 1
            y = 0 if move.direction == "L" else (len(self.arena) - 1)
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

    # Executes one move
    def execute(self, move: Move) -> None:
        coords = self.indexBy(move)
        mark = self.getField(coords)
        if mark != "-":
            self.moveFields(move, coords)
        self.setField(coords)

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

    # Moves items in row one index right until free field occurs
    def moveInRowToRight(self, rowI: int) -> None:
        endI = self.findIndexInRow(rowI, "-", False)
        for i in reversed(range(1, self.size if endI == None else (endI + 1))):
            self.arena[rowI][i] = self.arena[rowI][i - 1]

    # Moves items in row one index left until free field occurs
    def moveInRowToLeft(self, rowI: int) -> None:
        endI = self.findIndexInRow(rowI, "-", True)
        for i in range(0 if endI == None else endI, self.size - 1):
            self.arena[rowI][i] = self.arena[rowI][i + 1]

    # Moves items in column one index down until free field occurs
    def moveInColToBottom(self, colI: int) -> None:
        endI = self.findIndexInCol(colI, "-", False)
        for i in reversed(range(1, self.size if endI == None else (endI + 1))):
            self.arena[i][colI] = self.arena[i - 1][colI]

    # Moves items in row one index up until free field occurs
    def moveInColToTop(self, colI: int) -> None:
        endI = self.findIndexInCol(colI, "-", True)
        r = range(0 if endI == None else endI, self.size - 1)
        for i in r:
            self.arena[i][colI] = self.arena[i + 1][colI]

    # Executes all given moves
    def executeMoves(self, moves: list[Move]) -> None:
        for move in moves:
            self.execute(move)

    # Returns the current and toggles the property to another player
    def getAndToggleCurrentPlayer(self) -> Player:
        current = str(self.currentPlayer)
        self.currentPlayer = "x" if self.currentPlayer == "o" else "o"
        return current

    # Return arena as string
    def arenaStr(self) -> str:
        return "| " + " |\n| ".join([" | ".join(row) for row in self.arena]) + " |"


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
