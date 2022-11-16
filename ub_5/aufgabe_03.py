from wypp import *

# Die Klasse Einkaufszettel enthaelt ein Datum: str, eine Liste mit Einkaeufen: list[str]
@record
class Einkaufszettel:
    datum: str
    artikels: list[str]


# Gibt die Menge der Artikel auf dem Zettel zurueck
# Eingang: Artikel: str, Einkaufszettel
# Ausgang: Menge der Artikel: int
def howMany(artikel: str, zettel: Einkaufszettel) -> int:
    return zettel.artikels.count(artikel)


# Gibt einen Einkaufszettel mit hinzugefuegtem Artikel zurueck
# Eingang: Artikel: str, Einkaufszettel
# Ausgang: Erweiterter Einkaufszettel
def addToShoppingList(artikel: str, zettel: Einkaufszettel) -> Einkaufszettel:
    return Einkaufszettel(zettel.datum, zettel.artikels + [artikel])


# Gibt Liste ohne gegebenes Element zurueck
# Eingang: Element: str, Liste mit Strings: list[str]
# Ausgang: Reduzierte Liste: list[str]
def removeAllFromList(el: str, l: list[str], i: int) -> list[str]:
    if i >= len(l):
        return l
    elif l[i] == el:
        return removeAllFromList(el, l[:i] + l[(i + 1) :], i)
    return removeAllFromList(el, l, (i + 1))


# Gibt einen Einkaufszettel mit entfernten Artikel zurueck
# Eingang: Artikel: str, Einkaufszettel
# Ausgang: Verminderter Einkaufszettel
def removeFromShoppingList(artikel: str, zettel: Einkaufszettel) -> Einkaufszettel:
    return Einkaufszettel(zettel.datum, removeAllFromList(artikel, zettel.artikels, 0))


zettel_1 = Einkaufszettel(
    "01.12.1994", ["Wasser", "Brot", "Messerset", "Brot", "Melone", "Salat"]
)

# Test
check(howMany("Wasser", zettel_1), 1)
check(howMany("Brot", zettel_1), 2)
check(howMany("USB-Stick", zettel_1), 0)

testListe = ["1", "2", "2", "3", "4"]
check(removeAllFromList("2", testListe, 0), ["1", "3", "4"])
check(removeAllFromList("3", testListe, 0), ["1", "2", "2", "4"])
check(removeAllFromList(":)", testListe, 0), ["1", "2", "2", "3", "4"])

check(
    addToShoppingList("Tofu", zettel_1),
    Einkaufszettel(
        "01.12.1994", ["Wasser", "Brot", "Messerset", "Brot", "Melone", "Salat", "Tofu"]
    ),
)
check(
    removeFromShoppingList("Packung Nudeln", zettel_1),
    Einkaufszettel(
        "01.12.1994", ["Wasser", "Brot", "Messerset", "Brot", "Melone", "Salat"]
    ),
)
check(
    removeFromShoppingList("Wasser", zettel_1),
    Einkaufszettel(
        "01.12.1994",
        ["Brot", "Messerset", "Brot", "Melone", "Salat"],
    ),
)
check(
    removeFromShoppingList("Brot", zettel_1),
    Einkaufszettel(
        "01.12.1994",
        ["Wasser", "Messerset", "Melone", "Salat"],
    ),
)
