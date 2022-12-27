from prelude import *
from game import Game
from move import textToMoves


# Converts save file string to game
def loadGame(saveStr: str) -> Game:
    texts = saveStr.split("\n")
    game = Game(int(texts.pop(0)))
    game.executeMoves(textToMoves(texts))
    return game


ttt = loadGame("4\nT2\nT2\nR1\nR1\nL1\nR1\n")
print(ttt.arenaStr())
