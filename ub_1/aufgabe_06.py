from wypp import *

# Die Funktion vervielfacht eine Zeichenkette
# Analyse: Ausgabe = n-mal hintereinander die Eingabe
# Eingabe: Zeichenkette: string, Anzahl der Vervielfachung: int
# Ausgabe: Vervielfachte Zeichenkette: string
def vervielfache(text: str, anzahl: int) -> str:
    output = ""
    for _ in range(anzahl):
        output += text
    return output


# Tests
check(vervielfache("", 2), "")
check(vervielfache("asdf", -5), "")

# a) verdoppeln
check(vervielfache("Ente", 2), "EnteEnte")

# b) vervierfachen
check(vervielfache("Ente", 4), "EnteEnteEnteEnte")

# c) verzwoelffachen
check(vervielfache("Ente", 12), "EnteEnteEnteEnteEnteEnteEnteEnteEnteEnteEnteEnte")

# d) versechzenfachen
check(
    vervielfache("Ente", 16),
    "EnteEnteEnteEnteEnteEnteEnteEnteEnteEnteEnteEnteEnteEnteEnteEnte",
)
