from itertools import groupby
import re


def decode(string: str):
    return ''.join(int(num or 1) * char 
                   for num, char in re.findall(r'(\d+)?(.)', string))


def encode(string):
    return ''.join(f'{(str(), n := len([*group]))[n > 1]}{char}'
                   for char, group in groupby(string))
