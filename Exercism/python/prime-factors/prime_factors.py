def factors(n):
    i, f = 2, []
    while n > 1:
        i = i + 1 if n % i != 0 else i
        if n % i == 0:
            f.append(i)
            n /= i
    return f
