from itertools import combinations


def maximum_value(maximum_weight: int, items: list[dict[str, int]]) -> int:
    MEM = []
    for i in range(1, len(items)):
        for c in combinations(items, i):
            weight = value = 0
            for x in c:
                if (weight := weight + x['weight']) > maximum_weight:
                    break
                value += x['value']
            MEM.append(value)

    return max(MEM, default=0)
