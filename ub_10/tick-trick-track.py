from prelude import *
from game import Game


# Converts save file string to game
def loadGame(saveStr: str) -> Game:
    texts = saveStr.split("\n")
    game = Game(texts.pop(0))
    game.executeMoves(texts)
    return game
