from wypp import *

# Liefert die Fibunacci-Zahlen bis n
# Eingang: Anzahl Zahlen: int
# Ausgang: Fibunacci-Zahlen: list[int]
def fibunacci(n: int) -> list[int]:
    res = [0, 1]
    for k in range(2, n):
        res.append(res[k - 2] + res[k - 1])
    return res


# Tests
check(fibunacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
