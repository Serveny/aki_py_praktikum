from wypp import *

# Zuckergehalt in Fruktose und Glukose
@record
class Zuckergehalt:
    fruktose: float
    glukose: float


# Name, Packungsgroesse und Zuckergehalt eines Lebensmittels
@record
class Lebensmittel:
    name: str
    packungsgroesseGramm: int
    zuckergehalt: Zuckergehalt


cocaCola = Lebensmittel("Coca Cola", 500, Zuckergehalt(25, 25))
ritterSport = Lebensmittel(
    "Ritter Sport himmlische Beere", 100, Zuckergehalt(15.29, 24.9)
)
colaZero = Lebensmittel("Cola Zero", 500, Zuckergehalt(0, 0))

ampel = Literal["gruen", "gelb", "rot"]

# Rechnet den Gesamtzuckergehalt pro 100g fuer das Lebensmittel
# Eingang: Lebensmittel
# Ausgang: Gesamtzuckergehalt pro 100g: float
def gesamtzuckergehaltPro100g(lm: Lebensmittel) -> float:
    gesamtzucker = lm.zuckergehalt.fruktose + lm.zuckergehalt.glukose
    return (gesamtzucker / lm.packungsgroesseGramm) * 100


# Errechnet den Ampelwert fuer das Lebensmittel
# Eingang: Lebensmittel
# Ausgang: Ampelwert: Literal(str)
def ampelwert(lm: Lebensmittel) -> ampel:
    gz = gesamtzuckergehaltPro100g(lm)
    return "rot" if gz > 22.5 else ("gelb" if gz >= 5 else "gruen")


check(gesamtzuckergehaltPro100g(cocaCola), 10)
check(gesamtzuckergehaltPro100g(ritterSport), 40.19)

check(ampelwert(colaZero), "gruen")
check(ampelwert(cocaCola), "gelb")
check(ampelwert(ritterSport), "rot")
