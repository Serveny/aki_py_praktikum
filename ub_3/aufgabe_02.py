from wypp import *


# Modellname, Bildschirmdiagonale in Zoll und der Preis eines Mobiltelefons
@record
class Mobiltelefon:
    modellname: str
    bildschirmDiagonaleZoll: float
    preis: float


# Bestimmt den Preis pro Zoll des Mobiltelefons
# Eingang: Mobiltelefon
# Ausgang: Preis pro Zoll: float
def preisProZoll(mt: Mobiltelefon) -> float:
    return mt.preis / mt.bildschirmDiagonaleZoll


# Bestimmt das guenstigere von zwei Mobiltelefonen
# Eingang: Mobiltelefon, Mobiltelefon
# Ausgang: Mobiltelefon
def guenstigeres(mt_1: Mobiltelefon, mt_2: Mobiltelefon) -> Mobiltelefon:
    return mt_1 if preisProZoll(mt_1) < preisProZoll(mt_2) else mt_2


telefon_1 = Mobiltelefon("TELEFON_01", 4.7, 399)
telefon_2 = Mobiltelefon("TELEFON_02", 10, 100)
telefon_3 = Mobiltelefon("TELEFON_03", 1, 100)

# Tests
check(preisProZoll(telefon_1), 84.8936170212766)
check(preisProZoll(telefon_2), 10)
check(preisProZoll(telefon_3), 100)

check(guenstigeres(telefon_1, telefon_2), telefon_2)
check(guenstigeres(telefon_2, telefon_3), telefon_2)
