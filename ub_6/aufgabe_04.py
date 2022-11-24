from wypp import *

# Matrix als Liste von mehreren Listen (Reihen) mit Float-Werten (Spalten)
Matrix = list[list[float]]

d = [[3, 2, 1], [1, 0, 2]]
e = [[1, 2], [0, 1], [4, 0]]

# Gibt eine Spalte einer Matrix zurueck
# Eingang: Matrix, Spaltenindex: int (Beginnt ab 0)
# Ausgang: Spalte als Liste: List[float]
def column(matrix: Matrix, i: int) -> list[float]:
    return [row[i] for row in matrix]


# Gibt die transponierte Matrix zurueck
# Eingang: Matrix
# Ausgang: Transponierte Matrix
def transpose(matrix: Matrix) -> Matrix:
    return [column(matrix, i) for i in range(len(matrix[0]))]


# Gibt Summe der Multiplikation jeden Elements einer Liste mit jedem Element gleichen Indexes einer anderen Liste zurueck
# Oder anders ausgedrueckt: Berechnet ein Element der Produktmatrix, wenn l_1 eine Zeile und l_2 eine Spalte ist
# Eingang: Liste 1: list[float], Liste 2: list[float]
# Ausgang: Summe der Multiplikationen: float
def multiLists(l_1: list[float], l_2: list[float]) -> float:
    return sum([el * l_2[i] for i, el in enumerate(l_1)])


# Multipliziert zwei Matrizen
# Eingang: Matrix a, Matrix b
# Ausgang: Produktmatrix
def matrixMult(a: Matrix, b: Matrix) -> Matrix:
    b_t = transpose(b)
    return [[multiLists(row, b_t[i]) for i in range(len(a))] for row in a]


# Tests
check(column(e, 1), [2, 1, 0])
check(column(d, 0), [3, 1])
check(multiLists([1, 2, 3], [1, 2, 3]), 14)
check(multiLists([1, 8, 7], [6, 4, 6]), 80)
check(transpose(e), [[1, 0, 4], [2, 1, 0]])
check(transpose(d), [[3, 1], [2, 0], [1, 2]])
check(matrixMult(d, e), [[7, 8], [9, 2]])
check(
    matrixMult([[-1, -2, 5], [1, 8, 7], [6, 4, 6]], [[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
    [[-1, -2, 5], [1, 8, 7], [6, 4, 6]],
)
