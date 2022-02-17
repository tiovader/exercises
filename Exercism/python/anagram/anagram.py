def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    word = word.casefold()

    return [c for c in candidates
            if c.lower() != word
            and sorted(word) == sorted(c.lower())]

