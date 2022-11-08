from wypp import *

SpielerPositionen = Literal["Torhueter", "Abwehr", "Mittelfeld", "Stuermer", "Ersatz"]

# Bestimmt Position anhand der Rueckennummer
# Eingang: Rueckennummer: int,
# Ausgang: Positon: Literal
def rueckennummerZuPosition(rueckennummer: int) -> SpielerPositionen | None:
    if rueckennummer == 1:
        return "Torhueter"
    elif rueckennummer in [2, 3, 4, 5]:
        return "Abwehr"
    elif rueckennummer in [6, 7, 8, 10]:
        return "Mittelfeld"
    elif rueckennummer in [9, 11]:
        return "Stuermer"
    elif rueckennummer >= 12 and rueckennummer <= 99:
        return "Ersatz"
    return None


check(rueckennummerZuPosition(1), "Torhueter")
check(rueckennummerZuPosition(2), "Abwehr")
check(rueckennummerZuPosition(5), "Abwehr")
check(rueckennummerZuPosition(6), "Mittelfeld")
check(rueckennummerZuPosition(10), "Mittelfeld")
check(rueckennummerZuPosition(9), "Stuermer")
check(rueckennummerZuPosition(11), "Stuermer")
check(rueckennummerZuPosition(12), "Ersatz")
check(rueckennummerZuPosition(99), "Ersatz")
check(rueckennummerZuPosition(0), None)
check(rueckennummerZuPosition(100), None)
