from math import sqrt
from itertools import count, islice


def is_prime(num):
    if num < 2:
        return False
    return all(num % i for i in range(2, int(sqrt(num) + 1)))


def prime(num):
    return next(islice(filter(is_prime, count()), num - 1, None))
