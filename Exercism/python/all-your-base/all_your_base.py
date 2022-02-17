def rebase(b1: int, digits: list[int], b2: int) -> list[int]:
    if not all(0 <= d < b1 for d in digits) or any(b <= 1 for b in (b1, b2)):
        raise ValueError("Error: invalid input args.")

    num = sum(n * pow(b1, idx) for idx, n in enumerate(digits[::-1]))
    res = [num % b2]

    while num := num // b2:
        res.insert(0, num % b2)

    return res
