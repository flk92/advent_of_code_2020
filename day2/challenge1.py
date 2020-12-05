import sys


def count(character, string):
    return sum((1 for c in string if c == character))


def validate(line):
    (spec, password) = map(str.strip, line.split(":"))
    (times, character) = spec.split(" ")
    (low, high) = map(int, times.split("-"))
    times_in = count(character, password)
    return times_in >= low and times_in <= high


def solution(lines):
    return sum((int(validate(line)) for line in lines))


if __name__ == "__main__":
    print(solution((line[:-1] for line in sys.stdin)))
