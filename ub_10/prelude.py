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
