from typing import Callable


def EQUAL(x: int, y: int) -> bool: return x == y
def SUBLIST(x: int, y: int) -> bool: return x in y
def SUPERLIST(x: int, y: int) -> bool: return y in x
def UNEQUAL(x: int, y: int) -> bool: return x != y


def sublist(x: int, y: int) -> Callable:
    x = ','.join(map(str, x))
    y = ','.join(map(str, y))

    for func in (EQUAL, SUBLIST, SUPERLIST, UNEQUAL):
        if func(x, y):
            return func
