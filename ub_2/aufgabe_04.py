from wypp import *

Schadstoffklasse = Literal["1-4", "5", "6"]

# Die Funktion ermittelt, ob die Einfahrt in die Stadt moeglich ist
# Eingang: Ist Maut bezahlt?: bool, Ist Sondergenehmigung?: bool, Schadstoffklasse Auto: Literal
# Ausgang: Darf einfahren?: bool
def istEinfahrMoeglich(
    istBezahltMaut: bool, istSondergenehmigung: bool, schadstoffklasse: Schadstoffklasse
) -> bool:
    return (
        istSondergenehmigung
        if not istBezahltMaut
        else (istSondergenehmigung if schadstoffklasse == "1-4" else True)
    )


# Tests
check(istEinfahrMoeglich(True, True, "5"), True)
check(istEinfahrMoeglich(False, True, "6"), True)
check(istEinfahrMoeglich(True, False, "1-4"), False)
check(istEinfahrMoeglich(False, False, "6"), False)
check(istEinfahrMoeglich(True, False, "5"), True)
check(istEinfahrMoeglich(False, False, "1-4"), False)
