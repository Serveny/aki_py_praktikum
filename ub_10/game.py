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

    # Executes one move
    def execute(self, move: Move) -> None:
        coords = self.indexBy(move)
        mark = self.getField(coords)
        if mark != "-":
            self.moveFields(coords)
        self.setField(coords)

    # Finds index of first/last occurence of given mark in row
    def findIndexInRow(self, rowNo: int, mark: Mark, findLast: bool) -> Optional[int]:
        r = range(self.size - 1, -1, -1) if findLast else range(self.size)
        for i in r:
            if self.arena[rowNo][i] == mark:
                return i
        return None

    # Finds index of first/last occurence of given mark in column
    def findIndexInCol(self, colNo: int, mark: Mark, findLast: bool) -> Optional[int]:
        r = range(self.size - 1, -1, -1) if findLast else range(self.size)
        for i in r:
            if self.arena[i][colNo] == mark:
                return i
        return None

    # Moves every item in row one index right
    def moveInRowToRight(self, coords: Coords) -> None:
        for (i,) in range(self.findIndexInRow(coords[0], "-", False)):
            self.arena[coords[0]][i] = self.arena[coords[0]][i - 1]

    # Executes all given moves
    def executeMoves(self, moves: list[Move]) -> None:
        for move in moves:
            self.execute(move)

    # Gives back the current and toggles the property to another player
    def getAndToggleCurrentPlayer(self) -> Player:
        current = str(self.currentPlayer)
        self.currentPlayer = "x" if self.currentPlayer == "o" else "o"
        return current


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

    def testMoves1(self) -> None:
        ttt = Game(4)
        ttt.executeMoves(textToMoves("T1\nT2\nT3\nT4\n".split("\n")))
        self.assertEqual(
            ttt.arena,
            [
                ["x", "o", "x", "o"],
                ["-", "-", "-", "-"],
                ["-", "-", "-", "-"],
                ["-", "-", "-", "-"],
            ],
        )

    def testMoves2(self) -> None:
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
