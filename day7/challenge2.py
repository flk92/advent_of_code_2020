import sys
import re

NAME_RE = re.compile(r"([a-z ]+) bags")
CONTENTS_RE = re.compile(r"([0-9]+) ([a-z ]+) bags?[.,]?")


def get_bag_name(string):
    return NAME_RE.findall(string)[0]


def get_contents(string):
    return CONTENTS_RE.findall(string)


def read_in(lines):
    bags = {}
    for line in lines:
        (name, contents) = line.split("contain")
        bags[get_bag_name(name)] = get_contents(contents)
    return bags


def walk_up(root_name, bags):
    count = 1
    root = bags[root_name]
    for amount, name in root:
        count += int(amount) * walk_up(name, bags)
    return count


def solution(lines):
    target = "shiny gold"
    bags = read_in(lines)
    return walk_up(target, bags) - 1


if __name__ == "__main__":
    print(solution((line[:-1] for line in sys.stdin)))
