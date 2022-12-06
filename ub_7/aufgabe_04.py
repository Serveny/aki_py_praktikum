from wypp import *

# Integriert ein Polynom
# Eingabe: Polynom vom Grad n (list[float])
# Ausgabe: Polynom vom Grad n+1 bzw. vom Grad +1 falls n=+1 (list[float])
def integrate(p: list[float]) -> list[float]:
    return [0] + [round(a / (i + 1), 4) for i, a in enumerate(p)]


# Ableitung eines Polynoms berechnen
# Eingabe: Polynom vom Grad n (list[float])
# Ausgabe: Polynom vom Grad n-1 bzw. vom Grad -1 falls n=-1 (list[float])
def derivative(p: list[float]) -> list[float]:
    return [(a * i) for i, a in enumerate(p)][1:]


# Tests Integrieren
check(integrate([]), [0])
check(integrate([42]), [0, 42])
check(integrate([1, 2, 3]), [0, 1, 1, 1])
check(integrate([1, -2, 3]), [0, 1, -1, 1])
check(integrate([1, 1, 1, 1]), [0, 1, 0.5, 0.3333, 0.25])

# Tests Ableiten
check(derivative([]), [])
check(derivative([42]), [])
check(derivative([1, 2, 3]), [2, 6])
check(derivative([0, 5, 0, 0, -4]), [5, 0, 0, -16])

# Tests Kombi: Erst integrieren, dann ableiten
check(derivative(integrate([0, 5, 0, 0, -4])), [0, 5, 0, 0, -4])
check(derivative(integrate([1, -2, 3])), [1, -2, 3])
check(derivative(integrate([])), [])
