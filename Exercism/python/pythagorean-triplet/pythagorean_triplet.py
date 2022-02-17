import math


def triplets_with_sum(num: int) -> list[list[int]]:
    def delta(c): return math.sqrt(c**2 - num**2 + 2*num * c)
    def root(c): return ((num - c + (delta(c) * i)) / 2 for i in (-1, 1))

    n = int((math.sqrt(2) - 1) * num)
    return [[*root(c), c] for c in range(n + 1, num//2) if not delta(c) % 1]
