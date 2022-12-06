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
    return [0] + [(a / i) for i, a in enumerate(p) if i != 0]


def get(l: list[Any], i: int) -> Any:
    return l[i] if i < len(l) else 0


# Polynome addieren
# Eingang: Zwei Polynome (2 list[float])
# Ausgang: Addiertes Polynom (list[float])
# Achtung: Grad der Polynome egal
def addPoly(p: list[float], q: list[float]) -> list[float]:
    result = []
    for i in range(max(len(p), len(q))):
        ai = get(p, i)
        bi = get(q, i)
        result += [ai + bi]
    return result


# Polynome multiplizieren
def multiPoly(p: list[float], q: list[float]) -> list[float]:
    if len(p) == 0 or len(q) == 0:
        return []
    r = []
    for i in range(len(p) + len(q) - 1):
        ci = 0
        for k in range(0, i + 1):
            ci += get(p, k) * get(q, i - k)
        r += [ci]
    return r


check(derivative([]), [])
check(derivative([42]), [])
check(addPoly([3, 6, 11], [2, 0, -4, 8]), [5, 6, 7, 8])
check(multiPoly([1, 2, 3], [1, 1]), [1, 3, 5, 3])
