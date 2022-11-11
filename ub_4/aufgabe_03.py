from wypp import *

# Groesse(S, M oder L)
Groesse = Literal["S", "M", "L"]

# Farbe (schwarz, gruen, blau oder rot)
Farbe = Literal["schwarz", "gruen", "blau", "rot"]

# Optionale Rueckennummer
RueckenNr = Union[intNonNegative, None]

# Trikot mit Groesse(S, M oder L), Farbe (schwarz, gruen, blau oder rot) und einer optionalen Rueckennummer
@record
class Trikot:
    groesse: Groesse
    farbe: Farbe
    rueckenNr: RueckenNr


# Hose mit Größe (S, M oder L) und Farbe (schwarz, gruen, blau oder rot)
@record
class Hose:
    groesse: Groesse
    farbe: Farbe


# Stutzengroesse mit einer oberen und unteren Schranke fuer die passende Schuhgroessee
@record
class Stutzengroesse:
    groesse: intNonNegative
    bereichSchuhgroesse: tuple[intNonNegative, intNonNegative]


# Stutzen mit Stuetzengroesse und einer Farbe(schwarz, gruen, blau oder rot)
@record
class PaarStutzen:
    farbe: Farbe
    groesse: Stutzengroesse


# Sportartikel. Entweder Trikot, Hose, oder ein Paar Stutzen
Sportartikel = Union[Trikot, Hose, PaarStutzen]


# Ermittelt, ob Rueckennummer enthalten ist
# Eingang: Trikot
# Ausgang: Ist enthalten?: bool
def istRueckennummerEnthalten(trikot: Trikot) -> bool:
    return isinstance(trikot.rueckenNr, int)


# Berechnet den Preis eines Trikots
# Eingang: Trikot
# Ausgang: Preis in Euro: float
def preisTrikot(trikot: Trikot) -> float:
    return 25 if istRueckennummerEnthalten(trikot) else 20


# Berechnet den Preis einer Hose
# Eingang: Hose
# Ausgang: Preis in Euro: float
def preisHose(hose: Hose) -> float:
    g = hose.groesse
    return 10 if g == "S" else (12 if g == "M" else 15)


# Berechnet den Preis fuer ein Paar Stutzen
# Eingang: Stutzen
# Ausgang: Preis in Euro: float
def preisStutzen(stutzen: PaarStutzen) -> float:
    return 5 if stutzen.groesse.bereichSchuhgroesse[1] <= 38 else 9


# Berechnet den Preis eines Sportartikels
# Eingang: Sportartikel
# Ausgang: Preis in Euro
def preisSportartikel(spa: Sportartikel) -> float:
    if isinstance(spa, Trikot):
        return preisTrikot(spa)
    elif isinstance(spa, Hose):
        return preisHose(spa)
    return preisStutzen(spa)


trikot_1 = Trikot("S", "schwarz", None)
trikot_2 = Trikot("L", "rot", 21)
hose_1 = Hose("S", "schwarz")
hose_2 = Hose("M", "rot")
hose_3 = Hose("L", "blau")

stutzengroesse_1 = Stutzengroesse(1, (27, 30))
stutzengroesse_2 = Stutzengroesse(4, (39, 42))
stutzen_1 = PaarStutzen("schwarz", stutzengroesse_1)
stutzen_2 = PaarStutzen("rot", stutzengroesse_2)

# Tests
check(istRueckennummerEnthalten(trikot_1), False)
check(istRueckennummerEnthalten(trikot_2), True)
check(preisTrikot(trikot_1), 20)
check(preisTrikot(trikot_2), 25)
check(preisHose(hose_1), 10)
check(preisHose(hose_2), 12)
check(preisHose(hose_3), 15)
check(preisStutzen(stutzen_1), 5)
check(preisStutzen(stutzen_2), 9)

check(preisSportartikel(trikot_1), 20)
check(preisSportartikel(hose_1), 10)
check(preisSportartikel(stutzen_1), 5)
