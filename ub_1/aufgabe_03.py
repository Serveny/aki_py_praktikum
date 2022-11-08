from wypp import *
from aufgabe_02 import euroZuDollar

# Die Funktion rechnet Euro in Dollar mit Abzug der Transaktionssteuer um
# Die Steuer darf maximal 100€ betragen
# Analyse: EuroNachSteuer = (Euro * (Min aus (SteuerInProzent / 100) und 100)
#          Dollar = Euro * EinEuroInDollar
# Eingang: Menge in Euro: float, Steuer in Prozent: float, Ein Euro in Dollar: float
# Ausgang: Menge in Dollar: float
def euroZuDollarMitSteuer(
    wertEuro: float, steuerProzent: float, einEuroInDollar: float
) -> float:
    return euroZuDollar(euroMitSteuer(wertEuro, steuerProzent), einEuroInDollar)


# Berechnung Steuer in Euro
# Analyse: EuroNachSteuer = Euro * (SteuerInProzent / 100)
# Eingang: Menge in Euro, Steuer in %
# Ausgang: Steuer in Euro
def steuer(wertEuro: float, steuerProzent: float) -> float:
    steuer = wertEuro * (steuerProzent / 100)
    return min(steuer, 100)


# Berechnung Betrag mit Steuer in Euro
# Analyse: EuroAbzueglichSteuer = Euro - Steuer
# Eingang: Menge in Euro: float, Steuern in Prozent: float
# Ausgang: Menge in Euro: float
def euroMitSteuer(wertEuro: float, steuerProzent: float) -> float:
    return wertEuro - steuer(wertEuro, steuerProzent)


# Tests
check(steuer(2000, 10), 100)
check(steuer(100, 10), 10)
check(steuer(10, 10), 1)
check(euroMitSteuer(100, 10), 90)
check(euroMitSteuer(2000, 10), 1900)
check(euroZuDollarMitSteuer(2000, 10, 1.15), 2185)
check(euroZuDollarMitSteuer(100, 10, 1.15), 103.5)
check(euroZuDollarMitSteuer(1, 10, 1.15), 1.035)
