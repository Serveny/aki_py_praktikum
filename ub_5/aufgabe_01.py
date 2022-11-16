from wypp import *

#  Gibt das  Element zurueck, das am selben Index steht, wie der String lang ist
# Eingang: Zu pruefendes Element in der Liste: str, Liste: list[str]
# Ausgang: Rueckgabeelement aus Liste: str
def strangeIndex(input: str, l: list[str]) -> str:
    if input in l:
        i = len(input)
        return l[i] if i < len(l) else l[-1]
    return min(l)


liste = ["bla", "blub", "", "lel", "lol", "soos", "muuuulm", "abcdefghi"]

# Tests
check(strangeIndex("bla", liste), "lel")
check(strangeIndex("", liste), "bla")
check(strangeIndex("ruuuar", liste), "")
check(strangeIndex("abcdefghi", liste), "abcdefghi")
check(strangeIndex("muuuulm", liste), "abcdefghi")
