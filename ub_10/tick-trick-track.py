import os
from prelude import *
from game import Game
from move import textToMoves
from ai import Ai
import sys

# Read file
def readFile(path: str) -> list[str]:
    with open(path, "r") as file:
        return file.readlines()


# Save file
def saveFile(path: str, content: str) -> None:
    with open(path, "w") as file:
        file.write(content)


# Converts save file string to game
def loadGame(saveStr: list[str]) -> Game:
    game = Game(int(saveStr.pop(0)))
    game.executeMoves(textToMoves(saveStr))
    return game


# Just for local testing (To lazy to change code every time before upload)
def testArgs() -> list[str]:
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    return [
        "tick-trick-track.py",
        os.path.join(location, "__dc.in.txt"),
        os.path.join(location, "__dc.out.txt"),
    ]


# Program starts here
def main() -> None:
    args = testArgs() if len(sys.argv) < 3 else sys.argv
    saveStr = readFile(args[1])
    game = loadGame(saveStr)
    nextMove = Ai(game).nextMove()
    saveFile(args[2], nextMove.toStr())


main()
# ttt = Game(4)
# ttt.executeMoves(textToMoves("R4\nR4\nR4\nR4\nR4\nB2\nB2\nB2\nB2\n".split("\n")))
# ai = Ai(ttt)
# print(ai.nextMove().toStr())
