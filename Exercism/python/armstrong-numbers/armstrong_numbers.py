from math import log10


def is_armstrong_number(num):
    d = int(log10(num or 1)) + 1
    return sum(int(i) ** d for i in str(num)) == num

