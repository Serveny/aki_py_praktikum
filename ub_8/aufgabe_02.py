from wypp import *


# Fuegt zu neuer Liste neues Objekt hinzu, falls in alter Liste noch nicht vorhanden
# Eingang: Neues Objekt: Any, Liste mit Objekten: list[Any]
# Ausgang: Erweitere Liste mit Objekten: list[Any]
def addIfNotEq(new_obj: Any, obj_list: list[Any]) -> list[Any]:
    if any(item == new_obj for item in obj_list):
        return obj_list
    return obj_list + [new_obj]


# Fuegt zu Liste neues Objekt hinzu, falls darin noch nicht vorhanden
# Eingang: Neues Objekt: Any, Liste mit Objekten: list[Any]
# Ausgang: None
def addIfNotEqIdentical(new_obj: Any, obj_list: list[Any]) -> None:
    if not any(item == new_obj for item in obj_list):
        obj_list.append(new_obj)


# Tests
check(addIfNotEq("2", [1, "2", True, 0, ""]), [1, "2", True, 0, ""])
check(addIfNotEq("2", [1, True, 0, ""]), [1, True, 0, "", "2"])
check(addIfNotEq("2", []), ["2"])

list_1 = [1, "2", True, 0, ""]
addIfNotEqIdentical("2", list_1)
check(list_1, [1, "2", True, 0, ""])

list_2 = [1, True, 0, ""]
addIfNotEqIdentical("2", list_2)
check(list_2, [1, True, 0, "", "2"])

list_3 = []
addIfNotEqIdentical("2", list_3)
check(list_3, ["2"])
