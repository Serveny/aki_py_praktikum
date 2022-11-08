from wypp import *

# Zutaten einer Pizza
@record
class Zutaten:
    isOliven: bool = False
    isPilze: bool = False
    isSalami: bool = False
    isKaese: bool = False


# Groesse einer Pizza
groesse = Literal["normal", "gross"]

# Groesse und Zutaten einer Pizza
@record
class Pizza:
    groesse: groesse
    zutaten: Zutaten = Zutaten()


# Errechnet den Preis einer Zutat
# Eingang: Normalpreis: float, Pizzagroesse
# Ausgang: Preis Zutat: float
def preisZutat(normPreis: float, groesse: groesse) -> float:
    return normPreis if groesse == "normal" else normPreis * 1.1


# Errechnet den Preis der Pizza
# Eingang: Pizza
# Ausgang: Preis in Euro: float
def preis(p: Pizza) -> float:
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

check(preis(pizza_1), 2)
check(preis(pizza_2), 2.5)
check(preis(pizza_3), 2.4)
check(preis(pizza_4), 3.9)
check(preis(pizza_5), 3.05)
check(preis(pizza_6), 3.6)
check(preis(pizza_7), 4.59)
