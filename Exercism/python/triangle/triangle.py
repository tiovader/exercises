from heapq import nsmallest


def is_triangle(sides: list[int], kind: str):
    return (not any(n == 0 for n in sides)
            and sum(nsmallest(2, sides)) >= max(sides)
            and len(set(sides)) in {1: [1], 2: [1, 2], 3: [3]}[kind])


def equilateral(sides: list[int]) -> bool:
    return is_triangle(sides, 1)


def isosceles(sides):
    return is_triangle(sides, 2)


def scalene(sides):
    return is_triangle(sides, 3)
