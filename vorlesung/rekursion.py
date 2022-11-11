numbers = []


def rek(i: int) -> int:
    numbers.append(i)
    return i if i == 10 else rek(i + 1)


rek(1)
