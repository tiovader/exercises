from string import ascii_lowercase as lower


def is_isogram(string: str) -> bool:
    return all(string.casefold().count(n) <= 1 for n in lower)
