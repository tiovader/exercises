def rows(letter: str) -> list[str]:
    def wrap(i, aux=None):
        return (' ' * (idx - i) + AZ[i] + ' ' * i)[:aux][::aux]

    idx = (AZ := 'ABCDEFGHIJKLMNOPQRSTUVWXYZ').index(letter.upper())
    res = [wrap(i) + wrap(i, -1) for i in range(idx+1)]
    return res + res[:-1][::-1]
