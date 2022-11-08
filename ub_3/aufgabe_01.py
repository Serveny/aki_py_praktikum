from wypp import *

# Vor- und Nachname einer Person
@record
class Name:
    vorname: str
    nachname: str


# Strassenname und Hausnummer einer Adresse
@record
class Strasse:
    strassenname: str
    hausNr: int


# Adresse bestehend aus Name, Strasse, Zusatz, PLZ, Stadt und Land
@record
class Adresse:
    name: Name
    strasse: Strasse
    zusatz: str
    plz: int
    stadt: str
    land: str


# Aendert den Nachnamen in einer Adresse
# Eingang: Adresse, Neuer Nachname: str
# Ausgang: Adresse
def aendereNachnamen(adresse: Adresse, neuerNachname: str) -> Adresse:
    return Adresse(
        Name(adresse.name.vorname, neuerNachname),
        adresse.strasse,
        adresse.zusatz,
        adresse.plz,
        adresse.stadt,
        adresse.land,
    )


# Wandelt Adresse zu Briefadresse
# Eingang: Adresse
# Ausgang: Briefadresse: str
def briefadresse(adresse: Adresse) -> str:
    zusatz = "" if adresse.zusatz == "" else f" {adresse.zusatz}"
    return f"{adresse.name.vorname} {adresse.name.nachname}\n{adresse.strasse.strassenname} {adresse.strasse.hausNr}{zusatz}\n{adresse.plz} {adresse.stadt}\n{adresse.land}"


adresse1 = Adresse(
    Name("Max", "Mustermann"),
    Strasse("Musterstrasse", 1),
    "Zimmer 8",
    65673,
    "Musterstadt",
    "Musterland",
)

adresse2 = Adresse(
    Name("Lukas", "Lolmann"),
    Strasse("Musterstrasse", 4),
    "",
    65673,
    "Musterstadt",
    "Musterland",
)

# Tests
check(
    aendereNachnamen(adresse1, "Horst"),
    Adresse(
        Name("Max", "Horst"),
        Strasse("Musterstrasse", 1),
        "Zimmer 8",
        65673,
        "Musterstadt",
        "Musterland",
    ),
)
check(
    aendereNachnamen(adresse1, ""),
    Adresse(
        Name("Max", ""),
        Strasse("Musterstrasse", 1),
        "Zimmer 8",
        65673,
        "Musterstadt",
        "Musterland",
    ),
)

check(
    briefadresse(adresse1),
    """Max Mustermann
Musterstrasse 1 Zimmer 8
65673 Musterstadt
Musterland""",
)
check(
    briefadresse(adresse2),
    """Lukas Lolmann
Musterstrasse 4
65673 Musterstadt
Musterland""",
)
