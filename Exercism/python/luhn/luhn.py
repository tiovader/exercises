def double(n: int) -> int:
    if n in (0, 9):
        return n
    return n * 2 % 9


class Luhn:

    def __init__(self, card_num: str) -> None:
        self.card_num = card_num.replace(' ', '')

    def valid(self) -> bool:
        if len(self.card_num) <= 1 or not self.card_num.isnumeric():
            return False

        num, i = list(map(int, self.card_num)), (len(self.card_num) % 2)
        luhn = [double(x) for x in num[i::2]] + num[not i::2]
        return not sum(luhn) % 10
