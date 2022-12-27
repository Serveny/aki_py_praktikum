from __future__ import annotations
from wypp import *
import unittest

# Player-Literal: x, o
Player = Literal["x", "o"]

# Mark on field: Player, -
Mark = Literal[Player, "-"]

# Game field: list of rows of marks
GameArena = list[list[Mark]]

# Move directions: T (top), R (right), B (Bottom), L (Left)
Direction = Literal["T", "R", "B", "L"]

Coords = tuple[int, int]

# Returns column of arena
# IN: Arena: list[list[Any]]
# OUT: Column as list: List[Any]
def column(arena: list[list[Any]], i: int) -> list[Any]:
    return [row[i] for row in arena]


class PreludeTests(unittest.TestCase):
    def testColumn(self) -> None:
        arena = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        self.assertEqual(column(arena, 0), [1, 4, 7])
        self.assertEqual(column(arena, 1), [2, 5, 8])
        self.assertEqual(column(arena, 2), [3, 6, 9])
