import re
from collections import Counter


def count_words(text: str) -> dict[str, int]:
    return Counter(re.findall(r"[a-z0-9]+(?:'[a-z])?", text.lower()))
