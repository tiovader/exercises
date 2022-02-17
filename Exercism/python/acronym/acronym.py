import re


def abbreviate(words: str) -> str:
    return ''.join(w[0] for w in re.findall(r"[A-Z']+", words.upper()))
