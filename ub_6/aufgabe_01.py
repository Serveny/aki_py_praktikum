from wypp import *

# Berechnet die Potenz einer Zahl
# Eingang: Basis x: float, Exponent n: int
# Ausgang: Potenz
def power(x: float, n: int) -> float:
    potenz = 1
    for _ in range(abs(n)):
        potenz *= x
    if n < 0:
        potenz = 1 / potenz
    return potenz


# Tests
check(power(2, 0), 1)
check(power(2, 1), 2)
check(power(2, 2), 4)
check(power(-2, 3), -8)
check(power(-2, 2), 4)
check(power(2, -2), 0.25)
check(power(8, 3), 512)
check(power(8, 4), 4096)
check(power(8, -4), 0.000244140625)
