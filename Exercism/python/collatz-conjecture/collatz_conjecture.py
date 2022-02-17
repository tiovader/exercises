def steps(num: int, stps: int = 0) -> int:
    if num <= 0:
        raise ValueError("Only positive numbers are allowed")
    elif num == 1:
        return stps

    return steps(num/2 if not num % 2 else num * 3 + 1, stps + 1)

