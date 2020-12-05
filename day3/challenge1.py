import sys
from itertools import count


def hits(trajectory):
    return sum(1 for obj in trajectory if obj == "#")


def get(line, position):
    return line[position % len(line)]


def solution(lines):
    trajectory = (get(line[0], line[1]) for line in zip(lines, count(0, 3)))
    return hits(trajectory)


if __name__ == "__main__":
    print(solution((line[:-1] for line in sys.stdin)))
