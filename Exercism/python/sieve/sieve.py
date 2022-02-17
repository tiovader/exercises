def primes(n):
    return list(set(range(2, n + 1)).difference(
        j for i in range(2, n + 1) for j in range(i*2, n + 1, i)))
