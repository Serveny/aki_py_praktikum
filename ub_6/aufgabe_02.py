from wypp import *

# Erzeugt eine neue umgedrehte Liste
# Eingang: Liste: list
# Ausgang: Umgedrehte Liste: list
def reverse(l: list) -> list:
    rl = []
    for el in l:
        rl = [el] + rl
    return rl


# Tests
check(reverse([1, 2, 3, 4, 5, 6]), [6, 5, 4, 3, 2, 1])
check(reverse([1, "asdf", 3, 4, True, 6]), [6, True, 4, 3, "asdf", 1])
check(reverse([1, 0, 0, 1]), [1, 0, 0, 1])
