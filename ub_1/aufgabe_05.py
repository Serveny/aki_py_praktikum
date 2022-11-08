from wypp import *

# Die Funktion liefert Luises Lieblingszahlen zurueck
# Analyse: Liefert True wenn Zahl 6, 11, 13 oder groesser als 100 ist
# Eingang: Zahl: int
# Ausgang: IstLieblingszahl: bool
def istLieblingszahl(zahl: int) -> bool:
    return zahl in [6, 11, 13] or zahl > 100


# Tests
check(istLieblingszahl(6), True)
check(istLieblingszahl(123), True)
check(istLieblingszahl(42), False)
