from wypp import *

# Gibt Zahl mit x und Exponent ohne 1 als String zurueck
# Eingang: Zahl: float, Exponent von x: int
# Ausgang: Ausdruck als String
def zToString(z: float, e: int) -> str:
    return (
        str(z)
        if e == 0
        else (
            "x"
            if z == 1 and e == 1
            else (f"{z}x" if e == 1 else (f"x^{e}" if z == 1 else f"{z}x^{e}"))
        )
    )


# Verwandelt Polynom in String-Darstellung
# Eingang: Polynom: list[float]
# Ausgang: Polynomstring: str
def polyToString(p: list[float]) -> str:
    return " + ".join([zToString(z, i) for i, z in enumerate(p) if z != 0])


# Tests
check(zToString(1, 1), "x")
check(zToString(2, 1), "2x")
check(zToString(1, 2), "x^2")
check(zToString(2, 2), "2x^2")

check(polyToString([]), "")
check(polyToString([0]), "")
check(polyToString([0, 1, 0, 1]), "x + x^3")
check(polyToString([8, 5, 0, 0, 9]), "8 + 5x + 9x^4")
