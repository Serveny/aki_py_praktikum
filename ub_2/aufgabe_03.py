from math import ceil
from operator import contains
from wypp import *


@record
class Computer:
    prozessor: str
    festplatte: int
    arbeitsspeicher: int


# Die Funktion berechnet den Preis fuer den Arbeitsspeicher
# Eingabe: Computer
# Ausgabe: Preis in Euro: int
def preisArbeitsspeicher(c: Computer) -> int:
    return max(c.arbeitsspeicher * 5, 30)


# Die Funktion berechnet den Preis fuer die Festplatte
# Eingabe: Computer
# Ausgabe: Preis in Euro: int
def preisFestplatte(c: Computer) -> int:
    return ceil(c.festplatte / 500) * 20


# Die Funktion berechnet den Preis fuer die CPU
# Eingabe: Computer
# Ausgabe: Preis in Euro: int
def preisCPU(c: Computer) -> int:
    return 110 if "Intel" in c.prozessor else 90


# Die Funktion berechnet den Preis des Computers
# Eingabe: Computer
# Ausgabe: Preis in Euro: int
def preis(c: Computer) -> int:
    return preisArbeitsspeicher(c) + preisFestplatte(c) + preisCPU(c) + 100


# Die Funktion liefert einen Computer mit erweitertem Arbeitsspeicher
# Eingabe: Computer
# Ausgabe: Computer
def erweiterterPc(c: Computer, arbeitsspeicherErweiterung: int) -> Computer:
    return Computer(
        c.prozessor,
        c.festplatte,
        c.arbeitsspeicher + max(0, arbeitsspeicherErweiterung),
    )


billigPc = Computer("Sempron", 500, 2)
gamerPc = Computer("Quad", 1000, 16)
officePc = Computer("Intel i7", 750, 8)

check(preisArbeitsspeicher(billigPc), 30)
check(preisFestplatte(billigPc), 20)
check(preisCPU(billigPc), 90)
check(preis(billigPc), 240)

check(preisArbeitsspeicher(gamerPc), 80)
check(preisFestplatte(gamerPc), 40)
check(preisCPU(gamerPc), 90)
check(preis(gamerPc), 310)

check(preisArbeitsspeicher(officePc), 40)
check(preisFestplatte(officePc), 40)
check(preisCPU(officePc), 110)
check(preis(officePc), 290)

check(erweiterterPc(Computer("Quad", 1000, 16), 16), Computer("Quad", 1000, 32))
check(erweiterterPc(Computer("Quad", 1000, 16), -16), Computer("Quad", 1000, 16))
