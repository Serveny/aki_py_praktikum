from prelude import *
from game import Game
from move import Move, textToMoves

# "AI" lel
class Ai:
    game: Game

    # Constructor
    def __init__(self, game: Game) -> None:
        self.game = game

    # Get next move
    # Tactic: Just do what other player does if enemy will not win through this. If he do, do something else..
    def nextMove(self) -> Move:

        # Repeat last move
        move = self.game.lastMove or Move("B", self.game.size)
        if self.game.isAllowedMove(move):
            return move

        moves = self.otherMovesThan([move])

        # Find other allowed move
        for move in moves:
            if self.game.isAllowedMove(move):
                return move

        raise Exception("No move possible anymore :(")

    # Returns all possible moves except the moves in the input list
    def otherMovesThan(self, forbiddenMoves: list[Move]) -> list[Move]:

        allowedMoves = []
        for direction in ["B", "R", "L", "T"]:
            for number in range(1, self.game.size + 1)[::-1]:
                if not any(
                    direction == fm.direction and number == fm.number
                    for fm in forbiddenMoves
                ):
                    allowedMoves.append(Move(direction, number))

        return allowedMoves


class TestAi(unittest.TestCase):
    def testOtherMovesThan(self) -> None:
        ai = Ai(Game(4))
        self.assertEqual(
            len(ai.otherMovesThan(textToMoves(["T1", "T2", "T3", "T4"]))), 12
        )

    def testGameSituation(self) -> None:
        ttt = Game(4)
        ttt.executeMoves(
            textToMoves("R4\nR4\nR4\nR4\nR4\nB2\nB2\nB2\nB2\n".split("\n"))
        )
        ai = Ai(ttt)
        self.assertNotEqual(ai.nextMove().toStr(), "B2")
