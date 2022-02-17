from functools import partial
from math import sqrt
def factors(num, min_factor, max_factor):
    if not num:
        return []
    return [[i, num//i] for i in range(1, int(sqrt(num) + 1))
            if not num % i and min_factor <= i <= max_factor
            and min_factor <= num//i <= max_factor]
def is_palindrome(num):
    num = str(num)
    return num == num[::-1]
def palindrome(min_factor: int, max_factor: int, func: 'function' = None) -> int:
    if min_factor > max_factor:
        raise ValueError('Invalid arguments')
    palindromes = (num for i in range(min_factor, max_factor+1)
                   for j in range(min_factor, i + 1)
                   if is_palindrome(num := (i * j)))
    return (num := func(palindromes, default=None)), factors(num, min_factor, max_factor)
smallest = partial(palindrome, func=min)
largest = partial(palindrome, func=max)