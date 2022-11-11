from wypp import *

# --------------------------
# a)
# --------------------------

# Zutaten einer Pizza
@record
class Zutaten:
    isOliven: bool = False
    isPilze: bool = False
    isSalami: bool = False
    isKaese: bool = False


# Groesse einer Pizza
Groesse = Literal["normal", "gross"]

# Groesse und Zutaten einer Pizza
@record
class Pizza:
    groesse: Groesse
    zutaten: Zutaten = Zutaten()


# Errechnet den Preis einer Zutat
# Eingang: Normalpreis: float, Pizzagroesse
# Ausgang: Preis Zutat: float
def preisZutat(normPreis: float, groesse: Groesse) -> float:
    return normPreis if groesse == "normal" else normPreis * 1.1


# Errechnet den Preis der Pizza
# Eingang: Pizza
# Ausgang: Preis in Euro: float
def preisPizza(p: Pizza) -> float:
    g = p.groesse
    z = p.zutaten
    return round(
        (2.5 if g == "gross" else 2)
        + (preisZutat(0.5, g) if z.isOliven else 0)
        + (preisZutat(0.4, g) if z.isPilze else 0)
        + (preisZutat(0.45, g) if z.isSalami else 0)
        + (preisZutat(0.55, g) if z.isKaese else 0),
        2,
    )


pizza_1 = Pizza("normal")
pizza_2 = Pizza("gross")
pizza_3 = Pizza("normal", Zutaten(isPilze=True))
pizza_4 = Pizza("normal", Zutaten(True, True, True, True))
pizza_5 = Pizza("gross", Zutaten(isOliven=True))
pizza_6 = Pizza("gross", Zutaten(isSalami=True, isKaese=True))
pizza_7 = Pizza("gross", Zutaten(True, True, True, True))

# Tests
check(preisZutat(1, "normal"), 1)
check(preisZutat(1, "gross"), 1.1)

check(preisPizza(pizza_1), 2)
check(preisPizza(pizza_2), 2.5)
check(preisPizza(pizza_3), 2.4)
check(preisPizza(pizza_4), 3.9)
check(preisPizza(pizza_5), 3.05)
check(preisPizza(pizza_6), 3.6)
check(preisPizza(pizza_7), 4.59)


# --------------------------
# b)
# --------------------------

BierSorte = Literal["Pils", "Weizen"]
BierGroesse = Literal["0.3", "0.5"]

# Bier enthaelt:
# Sorte: Literal
# Menge in Liter: Literal
@record
class Bier:
    sorte: BierSorte
    groesse: BierGroesse


# Nudelgericht enthaelt
# Name: str
# Preis pro Gramm: float
# Bestellmenge: float
@record
class Nudelgericht:
    name: str
    preisProGramm: float
    bestellmengeGramm: int


# Gibt den Preis fuer ein Bier aus
# Eingang: Bier
# Ausgang: Preis in Euro: float
def preisBier(bier: Bier) -> float:
    return (
        (float(bier.groesse) * 8)
        if bier.sorte == "Pils"
        else (float(bier.groesse) * 8.5)
    )


# Gibt den Preis fuer ein Nudelgericht aus
# Eingang: Nudelgericht
# Ausgang: Preis in Euro: float
def preisNudelgericht(ng: Nudelgericht) -> float:
    return ng.preisProGramm * ng.bestellmengeGramm


# Gibt den Preis fuer ein Gericht (Pizza, Bier oder Nudelgericht) aus
# Eingang: Gericht: Pizza, Bier, Nudelgericht
# Ausgang: Preis: float
def preisGericht(gericht: Union[Pizza, Bier, Nudelgericht]) -> float:
    if isinstance(gericht, Pizza):
        return preisPizza(gericht)
    elif isinstance(gericht, Bier):
        return preisBier(gericht)
    else:
        return preisNudelgericht(gericht)


pilsKlein = Bier("Pils", "0.3")
pilsGross = Bier("Pils", "0.5")
weizenKlein = Bier("Weizen", "0.3")
weizenGross = Bier("Weizen", "0.5")
nudelnMitTomatensauce = Nudelgericht("Nudeln mit Tomatensauce", 0.1, 100)
nudelnMitPasta = Nudelgericht("Nudeln mit Pasta", 0.2, 100)

# Tests
check(preisBier(pilsKlein), 2.4)
check(preisBier(pilsGross), 4)
check(preisBier(weizenKlein), 2.55)
check(preisBier(weizenGross), 4.25)

check(preisNudelgericht(nudelnMitTomatensauce), 10)
check(preisNudelgericht(nudelnMitPasta), 20)

check(preisGericht(pizza_1), 2)
check(preisGericht(pizza_7), 4.59)
check(preisGericht(pizza_7), 4.59)
check(preisGericht(pilsKlein), 2.4)
check(preisGericht(weizenGross), 4.25)
check(preisGericht(nudelnMitTomatensauce), 10)
check(preisGericht(nudelnMitPasta), 20)
