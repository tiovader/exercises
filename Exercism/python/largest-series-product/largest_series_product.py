from functools import reduce
from operator import mul

def largest_product(series, k):
    if not 0 <= k <= (n:=len(series)):
        raise ValueError("Error: Some of arguments are invalid!")

    return max((reduce(mul, map(int, series[x: k + x]), 1)
                for x in range(n - k + 1)), default=1)
