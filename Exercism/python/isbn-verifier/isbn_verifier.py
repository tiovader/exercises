import re


def is_valid(isbn: str):
    if (m := re.match(r'(\d{9})([\dX])$', isbn.replace('-', ''))):
        isbn = (*m.group(1), m.group(2).replace('X', '10'))[::-1]
        return sum(i * j for i, j in enumerate(map(int, isbn), 1)) % 11 == 0
    return False


