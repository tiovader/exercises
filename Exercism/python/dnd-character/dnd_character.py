from random import randint, seed
from heapq import nlargest
ABILITIES: tuple[str] = ('strength', 'dexterity', 'constitution',
                         'intelligence', 'wisdom', 'charisma')


class Character:
    def __init__(self) -> None:
        [setattr(self, ability, self.ability()) for ability in ABILITIES]
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self) -> int:
        seed()
        return sum(nlargest(3, [randint(1, 6) for _ in range(4)]))


def modifier(score) -> int: return (score - 10) // 2
