import sys
from functools import reduce
from itertools import combinations
from math import prod


def solution(lines):
    entries = (int(line) for line in lines)
    return reduce(
        lambda acc, pair: prod(list(pair)),
        filter(
            lambda pair: sum(list(pair)) == 2020,
            combinations(entries, 3),
        ),
        1,
    )


if __name__ == "__main__":
    print(solution((line[:-1] for line in sys.stdin)))
