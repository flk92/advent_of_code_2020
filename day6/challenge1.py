import sys
from functools import reduce


def get_questions(lines):
    return set(reduce(lambda acc, line: acc + line, map(str.strip, lines), ""))


def gather_answers(lines):
    acc = []
    groups = []
    for line in lines:
        if line != "":
            acc.append(line)
        else:
            groups.append(get_questions(acc))
            acc = []
    if len(acc) > 0:
        groups.append(get_questions(acc))
    return groups


def solution(lines):
    return sum(len(group) for group in gather_answers(lines))


if __name__ == "__main__":
    print(solution((line[:-1] for line in sys.stdin)))
