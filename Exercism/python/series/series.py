def slices(seq: str, k: int) -> list[str]:
    if not (n := len(seq)):
        raise ValueError("series cannot be empty")
    elif k < 0:
        raise ValueError('slice length cannot be negative')
    elif k == 0:
        raise ValueError("slice length cannot be zero")
    elif k > n:
        raise ValueError("slice length cannot be greater than series length")


    return [seq[x: k + x] for x in range(n - k + 1)]

