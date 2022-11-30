from wypp import *

# Integriert ein Polynom
# Eingang: Polynom: list[float]
# Ausgang: Integriertes Polynom: list[float]
def integrate(p: list[float]) -> list[float]:
    return [0] + [round(a / (i + 1), 4) for i, a in enumerate(p)]


# Tests
check(integrate([]), [0])
check(integrate([42]), [0, 42])
check(integrate([1, 2, 3]), [0, 1, 1, 1])
check(integrate([1, 1, 1, 1]), [0, 1, 0.5, 0.3333, 0.25])
