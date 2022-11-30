from wypp import *

# Berechnet die n-te harmonische Zahl
# Eingang: n: int
# Ausgang: Harmonische Zahl: float
def harmony(n: int) -> float:
    return round(sum([1 / k for k in range(1, n + 1)]), 4)


# Tests
check(harmony(3), 1.8333)
check(harmony(5), 2.2833)
