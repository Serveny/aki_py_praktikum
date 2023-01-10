from prelude import *
from game import Game
from move import Move, textToMoves
from series import Series

# "AI" lel
class Ai:
    game: Game
    forbiddenMoves: list[Move] = []

    # Constructor
    def __init__(self, game: Game) -> None:
        self.game = game

    # Get next move
    # Tactic: Just do what other player does if enemy will not win through this. If he do, do something else..
    def nextMove(self) -> Move:
        series = self.game.findSeries()

        # Destroy enemy series
        toDestroy = series[0 if self.game.player == "o" else 1]
        if len(toDestroy) > 0:
            for series in toDestroy:
                dm = self.findDestroyMove(toDestroy[0])
                if dm != None:
                    return dm

        # Complete own series

        # Repeat last move
        move = self.game.lastMove or Move("B", self.game.size)
        if self.game.isAllowedMove(move):
            return move
        else:
            self.forbiddenMoves.append(move)

        # Find other allowed move
        for move in self.uncheckedMoves():
            if self.game.isAllowedMove(move):
                return move

        raise Exception("No move possible anymore :(")

    # Returns all possible moves except the moves in the input list
    def uncheckedMoves(self) -> list[Move]:

        allowedMoves = []
        for direction in ["B", "R", "L", "T"]:
            for number in range(1, self.game.size + 1)[::-1]:
                if not any(
                    direction == fm.direction and number == fm.number
                    for fm in self.forbiddenMoves
                ):
                    allowedMoves.append(Move(direction, number))

        return allowedMoves

    # Filter series list
    def filterSeries(
        self, series: list[Series], player: Player, size: int
    ) -> list[Series]:
        return sorted(
            list(
                filter(
                    lambda s: s.player == player and s.length >= size,
                    series,
                )
            ),
            key=lambda s: s.length,
            reverse=True,
        )

    # Finds move to destroy a series
    def findDestroyMove(self, series: Series) -> Optional[Move]:
        for move in series.moves():
            if self.game.isAllowedMove(move):
                if self.game.isEnemyKickout():
                    return move
            else:
                self.forbiddenMoves.append(move)
        return None


class TestAi(unittest.TestCase):
    def testAllowedMoves(self) -> None:
        ai = Ai(Game(4))
        ai.forbiddenMoves = textToMoves(["T1", "T2", "T3", "T4"])
        self.assertEqual(len(ai.uncheckedMoves()), 12)

    def testGameSituation(self) -> None:
        ttt = Game(4)
        ttt.executeMoves(
            textToMoves("R4\nR4\nR4\nR4\nR4\nB2\nB2\nB2\nB2\n".split("\n"))
        )
        ai = Ai(ttt)
        self.assertNotEqual(ai.nextMove().toStr(), "B2")
