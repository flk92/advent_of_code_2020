import sys


def split_records(lines):
    acc = []
    for line in lines:
        if line != "":
            acc.append(line)
        else:
            yield acc
            acc = []
    if len(acc) > 0:
        yield acc


def get_answers(lines):
    return set(str.join("", lines))


def solution(lines):
    groups = split_records(lines)
    answers = map(get_answers, groups)
    return sum(map(len, answers))


if __name__ == "__main__":
    print(solution((line[:-1] for line in sys.stdin)))
