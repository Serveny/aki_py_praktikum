from wypp import *


def eventTrueOddFalls(n: int) -> list[bool]:
    return [i % 2 == 0 for i in range(n)]


check(eventTrueOddFalls(4), [True, False, True, False])


def prime(n: int) -> list[int]:
    isPrime = [False, False] + ([True] * (n - 1))
    result = []
    for i in range(2, len(isPrime)):
        if isPrime[i]:
            result.append(i)
            for j in range(i * 2, len(isPrime), i):
                isPrime[j] = False
    return result


check(prime(11), [2, 3, 5, 7, 11])


def incByOneInPlace(l: list[int]) -> None:
    for i in range(l):
        l[i] = l[i] + 1


myList = [1, 2, 3]
incByOneInPlace(myList)
check(myList, [2, 3, 4])
