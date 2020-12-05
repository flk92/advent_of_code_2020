import sys
from itertools import count
from math import prod


def hits(trajectory):
    return sum(1 for obj in trajectory if obj == "#")


def get(line, position):
    return line[position % len(line)]


def traverse(full_map, slope):
    lines = map(
        lambda pair: pair[1],
        filter(lambda pair: pair[0] % slope[1] == 0, enumerate(full_map)),
    )
    return (get(line[0], line[1]) for line in zip(lines, count(0, slope[0])))


def solution(lines):
    full_map = list(lines)
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return prod(map(hits, (traverse(full_map, slope) for slope in slopes)))


if __name__ == "__main__":
    print(solution((line[:-1] for line in sys.stdin)))
