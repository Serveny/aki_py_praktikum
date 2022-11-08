from wypp import *

# Die Funktion rechnet Euro in Dollar um
# Analyse: Dollar = Euro * EinenEuroInDollar
# Eingang: Menge in Euro: float, 1 Euro in Dollar: float
# Ausgang: Menge in Dollar: float
def euroZuDollar(wertEuro: float, einEuroInDollar: float) -> float:
    return wertEuro * einEuroInDollar


check(euroZuDollar(1, 1.15), 1.15)
check(euroZuDollar(-1, 1.15), -1.15)
check(euroZuDollar(-1.5, 1.15), -1.725)
