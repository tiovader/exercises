from string import ascii_lowercase as az
from random import seed, choices
from itertools import cycle
NUM = dict(zip(az, range(0, 26)))


class Cipher:
    def __init__(self, key: str = ''):
        seed()
        self.key = key.lower() or ''.join(choices(az, k=255))

    def encode(self, text: str, *, reverse=False):
        direction = -1 if reverse else 1
        return ''.join(
            [az[(NUM[n] + (NUM[m]) * direction) % 26] for n, m in zip(text, cycle(self.key))]
        )

    def decode(self, text: str):
        return self.encode(text, reverse = True)
