from wypp import *

# Fuegt Element an Index hinzu und verschiebt alle Nachfolger um i + 1
# Eingang: Liste: list[Any]
# Ausgang: None
def myInsert(l: list[Any], i: int, x: Any) -> None:
    if i > len(l) - 1:
        l.append(x)
    else:
        if i < -len(l):
            i = 0
        l.append(l[-1])
        for u in range(len(l) - 1, (len(l) + i - 1) if i < 0 else i, -1):
            l[u] = l[u - 1]
        l[(i - 1) if i < 0 else i] = x


# Tests
liste_1 = [1, 2, 3, 4]
myInsert(liste_1, 0, "blub")
check(liste_1, ["blub", 1, 2, 3, 4])

liste_2 = [1, 2, 3, 4]
myInsert(liste_2, 3, "blub")
check(liste_2, [1, 2, 3, "blub", 4])

liste_3 = [1, 2, 3, 4]
myInsert(liste_3, -2, "blub")
check(liste_3, [1, 2, "blub", 3, 4])

liste_4 = [1, 2, 3, 4]
myInsert(liste_4, 999, "blub")
check(liste_4, [1, 2, 3, 4, "blub"])

liste_5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
myInsert(liste_5, -4, "blub")
check(liste_5, [1, 2, 3, 4, 5, "blub", 6, 7, 8, 9])

liste_5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
myInsert(liste_5, -9, "blub")
check(liste_5, ["blub", 1, 2, 3, 4, 5, 6, 7, 8, 9])

liste_6 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
myInsert(liste_6, -10, "blub")
check(liste_6, ["blub", 1, 2, 3, 4, 5, 6, 7, 8, 9])
