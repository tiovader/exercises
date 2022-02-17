k = ('eggs', 'peanuts', 'shellfish', 'strawberries',
     'tomatoes', 'chocolate', 'pollen', 'cats')
v = (1 << i for i in range(8))
ALLERGIES = dict(zip(k, v))


class Allergies:

    def __init__(self, score: int) -> None:
        self.score = score

    def allergic_to(self, item: int) -> bool:
        return bool(self.score & ALLERGIES[item])

    @property
    def lst(self) -> list[str]:
        return list(filter(self.allergic_to, ALLERGIES))
