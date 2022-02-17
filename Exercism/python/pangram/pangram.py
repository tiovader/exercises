from string import ascii_lowercase as lower


def is_pangram(sentence: str) -> bool:
    return all(letter in sentence.casefold() for letter in lower)
