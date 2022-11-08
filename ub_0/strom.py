from wypp import *

# Monatlichen Rechnungsbetrag fuer Tarif Billing Strom berechnen
# Eingabe: Monatsverbrauch in kWh, als float
# Ergebnis: Rechnungsbetrag als float


def billigStrom(kwh: float) -> float:
    return 4.99 + kwh * 0.19


# Tests
check(billigStrom(10), 6.89)
check(billigStrom(0), 4.99)
check(billigStrom(-2), 4.61)
