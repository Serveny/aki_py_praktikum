from math import ceil
from wypp import *

# Die Funktion bestimmt das Bußgeld fuer zu langes Parken
# Eingang: Ueberschreitungsdauer in Minuten: int
# Ausgang: Bußgeld in Euro: float
def bussgeld(ueberschreitungDauerMinuten: int) -> int:
    if ueberschreitungDauerMinuten == 0:
        return 0
    elif ueberschreitungDauerMinuten <= 30:
        return 10
    elif ueberschreitungDauerMinuten <= 60:
        return 15
    elif ueberschreitungDauerMinuten <= 120:
        return 20
    elif ueberschreitungDauerMinuten <= 180:
        return 25
    else:
        n = ceil(ueberschreitungDauerMinuten / 60)
        return (n - 1) * 10


check(bussgeld(0), 0)
check(bussgeld(30), 10)
check(bussgeld(60), 15)
check(bussgeld(120), 20)
check(bussgeld(180), 25)
check(bussgeld(181), 30)
