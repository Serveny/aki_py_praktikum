from wypp import *

# Entfernt die Elemente in angegebener Reichweite
# Eingang: Liste: list, Start: int, Ende: int, Schritt: int
# Ausgang: None
def removeSlice(l: list, start: int, end: int, step: int) -> None:
    for index in range(start, end, step)[::-1]:
        del l[index]


# Tests
myList = ["A", "B", "C", "D", "E", "F", "G"]
removeSlice(myList, 1, 5, 2)
check(myList, ["A", "C", "E", "F", "G"])

myList2 = [1, 2, 3, 1, 2, 3]
removeSlice(myList2, 0, 3, 1)
check(myList2, [1, 2, 3])
