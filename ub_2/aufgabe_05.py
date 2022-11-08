from wypp import *


@record
class Strafe:
    GeldInEuro: int
    PunkteFlensburg: int
    FahrverbotInMonaten: int


GefaehrdungStatus = Literal["Keine", "GefaehrdungDritter", "Sachbeschaedigung"]


@record
class Vergehen:
    ampelRotSekunden: int
    gefaehrdung: GefaehrdungStatus


# Die Funktion errechnet die Strafe anhand des Vergehens
# Eingang: Vergehen: class
# Ausgang: Strafe: class
def strafe(vergehen: Vergehen) -> Strafe:
    if vergehen.ampelRotSekunden == 1:
        return Strafe(
            150 if vergehen.gefaehrdung == "Sachbeschaedigung" else 50,
            1
            if vergehen.gefaehrdung == "GefaehrdungDritter"
            or vergehen.gefaehrdung == "Sachbeschaedigung"
            else 0,
            0,
        )
    elif vergehen.ampelRotSekunden > 1:
        return Strafe(
            100 + (vergehen.ampelRotSekunden * 10),
            4
            if vergehen.gefaehrdung == "GefaehrdungDritter"
            or vergehen.gefaehrdung == "Sachbeschaedigung"
            else 0,
            1
            if vergehen.gefaehrdung == "GefaehrdungDritter"
            else (4 if vergehen.gefaehrdung == "Sachbeschaedigung" else 0),
        )

    return Strafe(0, 0, 0)


# Tests
check(strafe(Vergehen(0, "Keine")), Strafe(0, 0, 0))
check(strafe(Vergehen(1, "Keine")), Strafe(50, 0, 0))
check(strafe(Vergehen(1, "GefaehrdungDritter")), Strafe(50, 1, 0))
check(strafe(Vergehen(1, "Sachbeschaedigung")), Strafe(150, 1, 0))
check(strafe(Vergehen(2, "Keine")), Strafe(120, 0, 0))
check(strafe(Vergehen(2, "GefaehrdungDritter")), Strafe(120, 4, 1))
check(strafe(Vergehen(2, "Sachbeschaedigung")), Strafe(120, 4, 4))
