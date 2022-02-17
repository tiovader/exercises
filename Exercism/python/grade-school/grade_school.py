from bisect import insort
from itertools import chain


class School:
    def __init__(self) -> None:
        self.lst = [[] for _ in range(19)]

    def add_student(self, name: str, grade: int) -> None:
        insort(self.lst[grade], name)

    def roster(self) -> list[str]:
        return list(chain(*self.lst))

    def grade(self, grade: int) -> list[str]:
        return self.lst[grade].copy()
