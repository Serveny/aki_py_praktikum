from wypp import *

# P(x) = -5x^3 + x - 6
poly = [-6, 1, 0, -5]

# P(x) = 2x^2 - 7x^4
poly_2 = [0, 0, 2, 0, 4]


def skalarMulti(p: list[float], skalar: float) -> list[float]:
    return [(el * skalar) for el in p]


def polyEval(p: list[float], sigma: float) -> float:
    return sum([(a * (sigma**i)) for i, a in enumerate(p)])


def derivative(p: list[float]) -> list[float]:
    return [(a * i) for i, a in enumerate(p)][1:]


def integrate(p: list[float]) -> list[float]:
    # TODO
    return [0] + [(a / i) for i, a in enumerate(p) if i != 0]


check(derivative([]), [])
check(derivative([42]), [])
