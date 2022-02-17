def square(n):
    if n < 1 or n > 64:
        raise ValueError('Argument out of range.')
    return 2**(n-1)


def total():
    return sum([2**x for x in range(0, 64)])
