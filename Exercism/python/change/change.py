from itertools import combinations_with_replacement, count
NEGATIVE_ERROR = "target can't be negative"
NOT_POSSIBLE_ERROR = "can't make target with given coins"


def find_fewest_coins(coins, target):
    def fewest():
        for i in range(2, target):
            comb = combinations_with_replacement(coins, i)
            _filter = filter(lambda x: sum(x) == target, comb)
            if (fewest := min(_filter, default=False)):
                return list(fewest)

        raise ValueError(NOT_POSSIBLE_ERROR)

    if target < 0 or target < min(coins) and target != 0:
        raise ValueError(NEGATIVE_ERROR if target < 0 else NOT_POSSIBLE_ERROR)
    elif target == 0:
        return []
    elif target in coins:
        return [target]
    else:
        return fewest()

