from prelude import *
from game import Game
from move import textToMoves


# Converts save file string to game
def loadGame(saveStr: str) -> Game:
    texts = saveStr.split("\n")
    game = Game(int(texts.pop(0)))
    game.executeMoves(textToMoves(texts))
    return game


ttt = loadGame("4\nL1\nL1\nL4\n")
print(column(ttt.arena, 0))
ttt.moveInColToBottom(0)
print(column(ttt.arena, 0))
