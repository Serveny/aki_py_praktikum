from prelude import *
from game import Game
from move import textToMoves
from ai import Ai
import sys

# Read file
def readFile(path: str) -> list[str]:
    with open(path) as file:
        return [line for line in file]


# Save file
def saveFile(path: str, content: str) -> None:
    with open(path) as file:
        file.write(content)


# Converts save file string to game
def loadGame(saveStr: list[str]) -> Game:
    game = Game(int(saveStr.pop(0)))
    game.executeMoves(textToMoves(saveStr))
    return game


# Program starts here
def main() -> None:
    saveStr = readFile(sys.argv[1])
    game = loadGame(saveStr)
    saveFile(sys.argv[2], Ai(game).nextMove().toStr())


# main()

game = Game(4)
game.executeMoves(textToMoves("L1\nR1\nL1\nR1\nL1\n".split("\n")))
print(f"Winner: {game.isLooseBySame()}")
