from math import inf, sqrt
from wypp import *

# Die Funktion berechnet die benoetigte Zeit fuer eine gegebene Strecke
# Analyse: Zeit = Strecke / Geschwindigkeit. Falls Geschwindigkeit 0 ist, benoetigt man eine unendlich lange Zeit.
# Eingang: Strecke: float, Geschwindigkeit in m/s: float
# Ausgang: Zeit in Sekunden: float
def zeitFuerStrecke(streckeM: float, geschwindigkeitMPerS: float) -> float:
    return inf if geschwindigkeitMPerS == 0 else streckeM / geschwindigkeitMPerS


# Die Funktion berechnet eine Strecke, die in einer gegebenen Zeit mit einer gegebenen Geschwindigkeit zurueckgelegt wurde.
# Analyse: Strecke = Zeit * Geschwindigkeit
# Eingang: Zeit in Sekunden: float, Geschwindigkeit in m/s: float
# Ausgang: Strecke in Meter: float
def strecke(zeit: float, geschwindigkeit: float) -> float:
    return zeit * geschwindigkeit


# Die Funktion berechnet die Laenge der Hypotenuse in einem Dreieck
# Analyse: a^2 + b^2 = c^2, c = sqrt(a^2 + b^2)
# Eingang: Laenge Ankathete in m: float, Laenge Gegenkathete in m: float
# Ausgang: Laenge Hypotenuse in m: float
def hypotenuse(ankathete: float, gegenkathete: float) -> float:
    return sqrt(ankathete**2 + gegenkathete**2)


# Die Funktion berechnet die vom Boot zurueckgelegte Strecke
# Analyse: Strecke = Hypotenuse von StreckeGerade und StreckeInFlussrichtung
# Eingang: Breite des Flusses in Meter: float,
#          Geschwindigkeit Fluss in m/s: float,
#          Geschwindigkeit Boot in m/s: float
# Ausgang: Zurueckgelegte Strecke des Bootes in Meter: float
def streckeBoot(
    flussBreiteM: float,
    geschwindigkeitFlussMPerS: float,
    geschwindigkeitBootMPerS: float,
) -> float:
    zeitBootsfahrt = zeitFuerStrecke(flussBreiteM, geschwindigkeitBootMPerS)
    ankathete = strecke(zeitBootsfahrt, geschwindigkeitBootMPerS)
    gegenkathete = strecke(zeitBootsfahrt, geschwindigkeitFlussMPerS)
    return hypotenuse(ankathete, gegenkathete)


# Tests
check(zeitFuerStrecke(100, 100), 1)
check(zeitFuerStrecke(100, 0), inf)
check(zeitFuerStrecke(0, 2), 0)

check(strecke(10, 10), 100)
check(strecke(10, 0), 0)
check(strecke(inf, 10), inf)

check(hypotenuse(1, 1), 1.4142135623730951)
check(hypotenuse(0, 1), 1)
check(hypotenuse(0, 0), 0)

check(streckeBoot(0, 5, 5), 0)
check(streckeBoot(100, 10, 10), 141.4213562373095)
check(streckeBoot(100, 10, 1), 1004.987562112089)
check(streckeBoot(3, 4, 3), 5)
