from prelude import *

# Move: Direction, number of row/column
class Move:
    direction: Direction
    number: int

    # Constructor
    def __init__(self, moveStr: str) -> None:
        try:
            self.direction = moveStr[0]
            self.number = int(moveStr[1])
        except Exception:
            raise Exception(f"Move not readable: {moveStr}")

    # Is move from top or bottom
    def isVertical(self) -> bool:
        return self.direction == "T" or self.direction == "B"

    def toStr(self) -> str:
        return f"{self.direction}{self.number}"


# Converts given text list to moves
def textToMoves(moves: list[str]) -> list[Move]:
    return [Move(moveStr) for moveStr in moves if moveStr != ""]


class MoveTests(unittest.TestCase):
    def testMove1(self) -> None:
        move = Move("T1")
        self.assertEqual(move.direction, "T")
        self.assertEqual(move.number, 1)
        self.assertEqual(move.isVertical(), True)

    def testMove2(self) -> None:
        move = Move("R3")
        self.assertEqual(move.direction, "R")
        self.assertEqual(move.number, 3)
        self.assertEqual(move.isVertical(), False)

    def testIllegalMoves(self) -> None:
        with self.assertRaises(Exception):
            Move("")
        with self.assertRaises(Exception):
            Move("1T")
        with self.assertRaises(Exception):
            Move("T")

    def testToStr(self) -> None:
        move = Move("T2")
        self.assertEqual(move.toStr(), "T2")
