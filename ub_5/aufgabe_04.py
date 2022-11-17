from wypp import *

# Alle erlaubten Operatoren: +, *, or, and, <, >=
Operator = Literal["+", "*", "or", "and", "<", ">="]


# Operatorknoten bestehend aus einem Operator und zwei Knoten
@record
class Op:
    el_1: "Knoten"
    operator: Operator
    el_2: "Knoten"


# Ein Knoten ist entweder ein Wert als String oder ein Operatorknoten
Knoten = Union[str, Op]

# Zaehlt die Elemente in einer Knotenstruktur
# Eingang: Knoten
# Ausgang: Anzahl Knoten: int
def countElems(k: Knoten) -> int:
    if isinstance(k, Op):
        return countElems(k.el_1) + countElems(k.el_2) + 1
    return 1


# Checkt, ob String in Nodekonstrukt vorkommt
# Eingang: Knoten, Gesuchter String: str
# Ausgang: Kommt vor?: bool
def containsString(k: Knoten, s: str) -> bool:
    if isinstance(k, Op):
        return k.operator == s or containsString(k.el_1, s) or containsString(k.el_2, s)
    return k == s


# True or (8 > x)
bsp = Op("True", "or", Op("8", "<", "x"))

# i: 5 + 7 * 4 * 2
b_1 = Op("5", "+", Op(Op("7", "*", "4"), "*", "2"))

# ii: (4 + 8) * -3 < 42 + 1
b_2 = Op(Op(Op("4", "+", "8"), "*", "-3"), "<", Op("42", "+", "1"))

# iii: True or 4 + 3 < x and z >= 7*10
z = 3
b_3 = Op(
    "True",
    "or",
    Op(Op(Op("4", "+", "3"), "<", "x"), "and", Op("z", ">=", Op("7", "*", "10"))),
)

# Tests
check(countElems(bsp), 5)
check(countElems(b_1), 7)
check(countElems(b_2), 9)
check(countElems(b_3), 13)

check(containsString(b_3, "True"), True)
check(containsString(b_3, "<"), True)
check(containsString(b_3, "Foo"), False)
check(containsString(b_3, "7"), True)
check(containsString(b_2, "43"), False)
