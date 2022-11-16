from wypp import *

# Unterelementmodus: PREFIX, SUFFIX, INFIX
Modus = Literal["PREFIX", "SUFFIX", "INFIX"]

# Gibt aus Zeichenkette mit durch Komma getrennter Elemente je nach Modus ein Element zurueck. Modus:
# PREFIX: Alle, ausser letztes Element
# SUFFIX: Alle, ausser erstes Element
# INFIX: Alle, ausser erstes und letztes Element
# Eingang: Zeichenkette: str, Modus: Literal
# Ausgang: Editierte Zeichenkette: str
def subElements(el: str, m: Modus) -> str:
    l = el.split(",")
    if m == "PREFIX":
        l = l[:-1]
    elif m == "SUFFIX":
        l = l[1:]
    else:
        l = l[1:-1]
    return ",".join(l)


namen = "Mara,Lana,Tobi,Max"
check(subElements(namen, "PREFIX"), "Mara,Lana,Tobi")
check(subElements(namen, "SUFFIX"), "Lana,Tobi,Max")
check(subElements(namen, "INFIX"), "Lana,Tobi")
