from collections import Counter
import re


def flush(*args):
    return 2e5 + sum(args[0]), len(set(args[1])) == 1


def straight(*args):
    a, b = min(args[0]), max(args[0])
    return 2e4 + sum(args[0]), args[0] == tuple(range(a, b + 1))


def straight_flush(*args):
    if args[0] == (1, 10, 11, 12, 13):
        return 2e10, True

    return 2e8 + sum(args[0]), straight(*args)[1] and flush(*args)[1]


def four_of_a_kind(*args):
    return 2e7 + sum(args[0]), Counter(args[0]).most_common(1)[0][1] == 4


def full_house(*args):
    return 2e6 + sum(args[0]), len(set(args[0])) == 2


def three_of_a_kind(*args):
    return 2e3 + sum(args[0]), Counter(args[0]).most_common(1)[0][1] == 3


def two_pair(*args):
    p1, p2 = Counter(args[0]).most_common(2)
    return 2e2 + p1[0] + p2[0], (p1[1], p2[1]) == (2, 2)


def one_pair(*args):
    return 2e1 + sum(args[0]), Counter(args[0]).most_common(1)[0][1] == 2


def high_card(*_):
    return 2e0, True


class PokerHand:

    def __init__(self, hand: str):
        self.hand = sorted(hand.split(), key=self.__rank)

    def __gt__(self, other: 'PokerHand'):
        if self.category == other.category:
            return self.ranks > other.ranks
        return self.category > other.category

    def __eq__(self, other: 'PokerHand') -> bool:
        if isinstance(other, PokerHand):
            return self.category == other.category \
                and self.ranks == other.ranks
        return repr(self) == repr(other)

    def __repr__(self) -> str:
        return ' '.join(self.hand)

    @staticmethod
    def __rank(card: str) -> int:
        table = {ord('J'): '11', ord('Q'): '12',
                 ord('K'): '13', ord('A'): '1'}
        num = re.sub(r'\D', '', card.translate(table))

        return int(num)

    @property
    def ranks(self) -> tuple[int]:
        _ranks = list(map(self.__rank, self.hand))
        if _ranks.count(1) > 1:
            while(_ranks.count(1)):
                _ranks.remove(1)
                _ranks.append(14)
        return tuple(_ranks)

    @property
    def suits(self) -> tuple[str]:
        return tuple(c[-1] for c in self.hand)

    @property
    def category(self):
        categories = (straight_flush, four_of_a_kind, full_house, flush, straight,
                      three_of_a_kind, two_pair, one_pair, high_card)
        for c in categories:
            points, is_category = c(*self)
            if is_category:
                return int(points), c.__name__
        pass

    def __iter__(self):
        yield from (self.ranks, self.suits)


def best_hands(hands):
    _hands = list(map(PokerHand, hands))
    return [hand for hand, i in zip(hands, _hands) if i == max(_hands)]
