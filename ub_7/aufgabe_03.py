from wypp import *


def polyToString(p: list[float]) -> str:
    res = ""
    for i, a in enumerate(p):
        if a == 0:
            continue

        # Prefix
        if res == "":
            if a < 0:
                res += "-"
        else:
            res += " - " if a < 0 else " + "

        # Number
        if a != 1:
            res += str(abs(a))

        # x
        if i > 0:
            res += "x"

        # Exponent
        if i > 1:
            res += f"^{i}"
    return res


# Tests
check(polyToString([]), "")
check(polyToString([0]), "")
check(polyToString([0, 1, 0, 1]), "x + x^3")
check(polyToString([8, 5, 0, 0, 9]), "8 + 5x + 9x^4")
check(polyToString([-8, 5, 0, 0, -9]), "-8 + 5x - 9x^4")
check(polyToString([-1, 5, 0, 0, -9]), "-1 + 5x - 9x^4")
