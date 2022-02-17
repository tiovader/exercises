from functools import reduce


def classify(num: int) -> str:
    if num <= 0 or not isinstance(num, int):
        raise ValueError(f'Classification is only possible for positive integers.')

    factors = set(
        reduce(
            list.__add__,
            [[i, num//i] for i in range(1, int(num**0.5) + 1) if not num % i]))
    factors.remove(num)
    aliquote_sum = sum(factors)

    return 'abundant' if aliquote_sum > num \
        else 'perfect' if aliquote_sum == num \
        else 'deficient'

