from prelude import *
from game import Game
from move import Move


class Ai:
    game: Game

    def __init__(self, game: Game) -> None:
        self.game = game

    def nextMove(game: Game) -> Move:
        return Move("R3")
