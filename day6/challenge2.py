import sys
from functools import reduce


def accumulate_answers(acc, answers):
    if acc is None:
        return answers
    return acc & answers


def get_questions(lines):
    return reduce(accumulate_answers, map(set, map(str.strip, lines)))


def gather_answers(lines):
    acc = []
    groups = []
    for line in lines:
        if line != "":
            acc.append(line)
        else:
            groups.append(acc)
            acc = []
    if len(acc) > 0:
        groups.append(acc)
    return map(get_questions, groups)


def solution(lines):
    return sum(len(group) for group in gather_answers(lines))


if __name__ == "__main__":
    print(solution((line[:-1] for line in sys.stdin)))
