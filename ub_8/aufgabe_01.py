from wypp import *

# Erstellt neue Liste ohne Leerstrings aus String-Liste
# Eingang: String-Liste: list[str]
# Ausgang: Bereinigte String-Liste: list[str]
def removeEmpties(str_list: list[str]) -> list[str]:
    return [item for item in str_list if item != ""]


# Entfernt aus bestehender Liste alle Leerstrings
# Eingang: String-Liste: list[str]
# Ausgang: None
def removeEmptiesMutable(str_list: list[str]) -> None:
    for i in range(len(str_list) - 1, -1, -1):
        if str_list[i] == "":
            del str_list[i]


# Tests
check(removeEmpties(["1", "2", "", "3"]), ["1", "2", "3"])
check(removeEmpties(["1", "", "", "3"]), ["1", "3"])
check(removeEmpties(["", "", "", ""]), [])

list_1 = ["1", "2", "", "3"]
removeEmptiesMutable(list_1)
check(list_1, ["1", "2", "3"])

list_2 = ["1", "", "", "3"]
removeEmptiesMutable(list_2)
check(list_2, ["1", "3"])

list_3 = ["", "", "", ""]
removeEmptiesMutable(list_3)
check(list_3, [])
