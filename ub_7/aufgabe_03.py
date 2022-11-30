from wypp import *

# Verwandelt Polynom in String-Darstellung
# Eingang: Polynom: list[float]
# Ausgang: Polynomstring: str
def polyToString(p: list[float]) -> str:
    return " + ".join(
        [
            str(z) if i == 0 else (f"{z}x" if i == 1 else f"{z}x^{i}")
            for i, z in enumerate(p)
            if z != 0
        ]
    )


# Tests
check(polyToString([8, 5, 0, 0, 9]), "8 + 5x + 9x^4")
