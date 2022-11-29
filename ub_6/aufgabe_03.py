from wypp import *

# Liefert einen Wert zu einem Schluessel aus einer Schluessel-Wert-Paar-Liste zurueck
# Eingang: Schluessel: str, Schluessel-Wert-Paar-Liste: [(int, Any)]
# Ausgang: Gefundener Wert zu Schluessel: Union[Any, None]
def lookup(k: int, l: list[tuple[int, Any]]) -> Union[Any, None]:
    for el in l:
        if el[0] == k:
            return el[1]
    return None


# Sorgt fuer gesetztes Schluessel-Wert-Paar in Liste bei gegebenem Schluessel
# Eingang: Schluessel: int, Wert: Any
# Ausgang: Erweiterte/Veraenderte Liste: list[tuple[str, Any]]
def insert(k: int, v: Any, l: list[tuple[int, Any]]) -> list[tuple[int, Any]]:
    for i in range(len(l)):
        if l[i][0] == k:
            return l[:i] + [(k, v)] + l[(i + 1) :]
    return l + [(k, v)]


# Tests aus Uebungsblatt
personList = [(42, "Max"), (100, "Helene"), (1, "Verena"), (10, "Dirk")]
check(lookup(10, personList), "Dirk")
check(lookup(11, personList), None)
check(
    insert(101, "Helene", personList),
    [(42, "Max"), (100, "Helene"), (1, "Verena"), (10, "Dirk"), (101, "Helene")],
)
check(
    insert(100, "Gundula", personList),
    [(42, "Max"), (100, "Gundula"), (1, "Verena"), (10, "Dirk")],
)
