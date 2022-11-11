from wypp import *

# Bach mit Ursprung und Name
@record
class Creek:
    origin: str
    name: str


# Zusammenfluss mit Ort, Hauptstamm und Nebenfluss
@record
class Confluence:
    location: str
    mainStem: "RiverSection"
    tributary: "RiverSection"


# Flussabschnitt: Entweder Bach oder Zusammenfluss
RiverSection = Union[Creek, Confluence]

# Dreisam                 Glotter
#    |                       |
#    |-------Bahlingen-------|     Elz
#               |                   |
# Ettenbach   Riegel ---------------|
#    |          |
#    |-----Kappel-Graph.
#               |

elz = Creek("Furtwangen", "Elz")
glotter = Creek("Kandel", "Glotter")
dreisam = Creek("Stegen", "Dreisam")
ettenbach = Creek("Ettenheimmuenster", "Ettenbach")

dreisam_2 = Confluence("Bahlingen", dreisam, glotter)
elz_2 = Confluence("Riegel", elz, dreisam_2)
elz_3 = Confluence("Kappel-Graphenhausen", elz_2, ettenbach)


# Ermittelt, aus wie vielen Hauptabschnitten ein Fluss besteht
# (Eigentlich haette ich die Funktion lieber "howManyMainSections" genannt, waere genauer)
# Eingang: Flussabschnitt
# Ausgang: Anzahl der Flussabschnitte
def howManySections(rs: RiverSection) -> int:
    if isinstance(rs, Creek):
        return 1
    return howManySections(rs.mainStem) + 1


# Ermittelt, ob man flussaufwaerts zu einem gegebenen Ort gelangt
# Eingang: Flussabschnitt: RiverSection, Ort: str
# Ausgang: Ist moeglich?: bool
def canSwimUpstream(rs: RiverSection, location: str) -> bool:
    if isinstance(rs, Creek):
        return rs.origin == location
    return (
        rs.location == location
        or canSwimUpstream(rs.mainStem, location)
        or canSwimUpstream(rs.tributary, location)
    )


# Tests
check(howManySections(elz), 1)
check(howManySections(dreisam_2), 2)
check(howManySections(elz_2), 2)
check(howManySections(elz_3), 3)

check(canSwimUpstream(elz, "Riegel"), False)
check(canSwimUpstream(dreisam_2, "Riegel"), False)
check(canSwimUpstream(elz_2, "Bahlingen"), True)
check(canSwimUpstream(elz_3, "Furtwangen"), True)
