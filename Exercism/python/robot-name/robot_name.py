from random import seed, choices
from string import ascii_uppercase as AZ, digits as D


class Robot:
    def __init__(self):
        seed()
        self.name = ''.join([*choices(AZ, k=2), *choices(D, k=3)])

    def reset(self):
        self.__init__()
