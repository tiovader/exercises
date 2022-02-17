class Queen:
    def __init__(self, row: int, column: int) -> None:
        if any(idx not in range(8) for idx in (row, column)):
            raise ValueError('Error')

        self.x = row
        self.y = column

    def can_attack(self, o: 'Queen') -> bool:
        if self.x == o.x and self.y == o.y:
            raise ValueError('Error')

        return self.x == o.x \
            or self.y == o.y \
            or abs(self.x - o.x) == abs(self.y - o.y)
