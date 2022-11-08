from wypp import *

# Typdefinition
Altersklassifikation = Literal[
    "baby", "kleinkind", "kind", "teenager", "erwachsener", "erfahrener"
]


def istErmaessigterEintritt(altersklasse: Altersklassifikation) -> bool:
    for klasse in Altersklassifikation:
        if altersklasse == klasse:
            return True
    return False


check(istErmaessigterEintritt("baby"), True)
check(istErmaessigterEintritt("teenager"), False)


@record
class x:
    i: int
