from typing import Generator
import re


class Score:
    win = draw = loss = 0

    @property
    def points(self) -> int:
        return (self.win * 3) + self.draw

    @property
    def matches(self) -> int:
        return sum((self.win, self.draw, self.loss))


class Team:
    def __init__(self, name: str) -> None:
        self.name = name.title()
        self.score = Score()

    def __repr__(self) -> str:
        return self.table_format(self.name, self.score.matches,
                                 self.score.win, self.score.draw,
                                 self.score.loss, self.score.points)

    def __lt__(self, other: 'Team') -> bool:
        return \
            (-self.score.points, self.name) < (-other.score.points, other.name)

    @staticmethod
    def table_format(*args) -> str:
        return '{: <31}|{: >3} |{: >3} |{: >3} |{: >3} |{: >3}'.format(*args)

    @staticmethod
    def header() -> str:
        return Team.table_format('Team', 'MP', 'W', 'D', 'L', 'P')

    def win(self, other: 'Team') -> None:
        self.score.win += 1
        other.score.loss += 1

    def loss(self, other: 'Team') -> None:
        other.win(self)

    def draw(self, other: 'Team') -> None:
        self.score.draw += 1
        other.score.draw += 1


def tally(rows: list[str]) -> list[str]:
    return [*table(team_points(rows))]


def team_points(rows: list[str]) -> dict[str, Team]:
    teams: dict[str, Team] = {}
    for row in rows:
        t1_name, t2_name, result = re.split(';', row.lower())
        t1 = teams.setdefault(t1_name, Team(t1_name))
        t2 = teams.setdefault(t2_name, Team(t2_name))
        getattr(t1, result)(t2)
    return teams


def table(teams: dict[str, Team]) -> Generator[str, None, None]:
    yield Team.header()
    yield from map(str, sorted(teams.values()))
