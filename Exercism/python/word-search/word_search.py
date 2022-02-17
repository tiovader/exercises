from itertools import combinations_with_replacement

combination = tuple(combinations_with_replacement((-1, 0, 1), 2))
r_combination = tuple(map(lambda e: e[::-1], combination))

MODE = set(filter(any, combination + r_combination))


class Point:
    def __init__(self, *args):
        self.coord = tuple(args[0:2])

    def __eq__(self, other):
        return self.coord == tuple(other) if not isinstance(other, Point) \
            else self.coord == other.coord

    def __repr__(self) -> str:
        return f'{self.coord}'

    @staticmethod
    def add(self, other):
        return tuple(i + j for i, j in zip(self, other))


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = tuple(puzzle)
        self.points = [(x, y)
                       for y in range(len(puzzle))
                       for x in range(len(puzzle[y]))]

    def search(self, word):
        def find(start, dx, dy):
            word = ''
            for i in range(lenght):
                if (p := Point.add(start, (dx * i, dy * i))) not in self.points:
                    break
                word += self.puzzle[p[1]][p[0]]
            else:
                return (start, p), word

        lenght = len(word)
        for point in filter(lambda p: self.puzzle[p[1]][p[0]] == word[0], self.points):
            for mode in MODE:
                if (match := find(point, *mode)) and match[1] == word:
                    return match[0]
