k = 'AEIOULNRSTDGBCMPFHVWYKJXQZ'
v = [1] * 10 + [2] * 2 + [3] * 4 + [4] * 5 + [5] + [8] * 2 + [10] * 2

SCORE = dict(zip(k, v))


def score(word: str) -> int:
    return sum(SCORE[n] for n in word.upper())
