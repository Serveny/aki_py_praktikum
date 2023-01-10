from prelude import *
from move import Move

# Object for point series
@record(mutable=True)
class Series:
    player: Mark = "-"
    length: int = 1
    start: Optional[Coords] = None
    end: Optional[Coords] = None

    # Returns all moves to effect series
    def moves(self) -> list[Move]:
        moves = []
        if self.start[1] == self.end[1]:
            for i in range(self.start[0], self.end[0] + 1):
                moves.append(Move("T", i + 1))
                moves.append(Move("B", i + 1))
            moves.append(Move("L", self.start[1] + 1))
            moves.append(Move("R", self.end[1] + 1))
        else:
            for i in range(self.start[1], self.end[1] + 1):
                moves.append(Move("L", i + 1))
                moves.append(Move("R", i + 1))
            moves.append(Move("T", self.start[0] + 1))
            moves.append(Move("B", self.end[0] + 1))
        return moves


class TestSeries(unittest.TestCase):
    def testMoves(self) -> None:
        def movesForSeriesStr(series: Series) -> list[str]:
            return [move.toStr() for move in series.moves()]

        self.assertEqual(
            movesForSeriesStr(Series("x", 2, (0, 0), (1, 0))),
            ["T1", "B1", "T2", "B2", "L1", "R1"],
        )
        self.assertEqual(
            movesForSeriesStr(Series("x", 2, (0, 0), (0, 1))),
            ["L1", "R1", "L2", "R2", "T1", "B1"],
        )
