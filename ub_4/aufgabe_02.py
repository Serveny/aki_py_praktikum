from wypp import *


# Zuckergehalt in Fruktose und Glukose
@record
class Zucker:
    fruktose: float
    glukose: float


# Ampel fuer den Zuckergehalt:
# gruen: < 5g
# gelb: zwischen 5g und 22,5g
# rot: > 22,5g
ampel = Literal["gruen", "gelb", "rot"]

# Zuckergehalt in Zucker(Glukose, Fruktrose), pro 100g oder Ampel(gruen, gelb, rot)
zuckergehalt = Union[Zucker, float, ampel]

# Name, Packungsgroesse und Zuckergehalt eines Lebensmittels
@record
class Lebensmittel:
    name: str
    packungsgroesseGramm: int
    zuckergehalt: zuckergehalt


cocaCola = Lebensmittel("Coca Cola", 500, Zucker(25, 25))
ritterSport = Lebensmittel("Ritter Sport himmlische Beere", 100, Zucker(15.29, 24.9))
kuerbis = Lebensmittel("Kuerbis", 1000, 2.8)
gurke = Lebensmittel("Gurke", 50, "gruen")


# Rechnet den Gesamtzuckergehalt pro 100g fuer das Lebensmittel
# Fuer Zuckergehalt in Ampel kann kein Wert berechnet werden
# Eingang: Lebensmittel
# Ausgang: Gesamtzuckergehalt pro 100g: float
def gesamtzuckergehaltPro100g(lm: Lebensmittel) -> Union[float, None]:
    zg = lm.zuckergehalt
    if isinstance(zg, Zucker):
        gesamtzucker = zg.fruktose + zg.glukose
        return (gesamtzucker / lm.packungsgroesseGramm) * 100
    elif isinstance(zg, float):
        return zg
    return None


# Errechnet den Ampelwert fuer das Lebensmittel
# Eingang: Zuckergehalt: Union[Zucker, pro 100g: float, ampel]
# Ausgang: Ampelwert: Literal(str)
def ampelwert(lm: Lebensmittel) -> ampel:
    if isinstance(lm.zuckergehalt, ampel):
        return lm.zuckergehalt
    else:
        gz = gesamtzuckergehaltPro100g(lm)
        return "rot" if gz > 22.5 else ("gelb" if gz >= 5 else "gruen")


check(gesamtzuckergehaltPro100g(cocaCola), 10)
check(gesamtzuckergehaltPro100g(ritterSport), 40.19)
check(gesamtzuckergehaltPro100g(kuerbis), 2.8)

check(ampelwert(cocaCola), "gelb")
check(ampelwert(ritterSport), "rot")
check(ampelwert(kuerbis), "gruen")
check(ampelwert(gurke), "gruen")
