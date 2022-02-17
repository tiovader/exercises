import re
from typing import Iterable
CHILDREN = ('Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny',
            'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry')
TABLE = {71: ' Grass ', 67: ' Clover ', 82: ' Radishes ', 86: ' Violets'}


def pattern(seq: Iterable[str]) -> list[str]:
    return (re.findall(r'[GCRV]{2}', i) for i in seq)


def translate(seq: Iterable[str]) -> list[str]:
    return ''.join(seq).translate(TABLE).strip().split()


class Garden:
    def __init__(self, diagram: str, students: list[str] = CHILDREN) -> None:
        self.diagram = diagram.upper().splitlines()
        self.students = sorted(students)

    def plants(self, student: str) -> list[str]:
        return self.garden[student]

    @property
    def garden(self) -> dict[str, list[str]]:
        plants = (translate(i) for i in zip(*pattern(self.diagram)))
        return dict(zip(self.students, plants))
