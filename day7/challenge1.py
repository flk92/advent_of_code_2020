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


def flip(in_bags):
    out_bags = {}
    for container_bag, contents in in_bags.items():
        if container_bag not in out_bags:
            out_bags[container_bag] = []
        for amount, bag in contents:
            entry = (amount, container_bag)
            if bag not in out_bags:
                out_bags[bag] = [entry]
            else:
                out_bags[bag].append(entry)
    return out_bags


def walk_up(root_name, bags):
    found = set([root_name])
    root = bags[root_name]
    for amount, name in root:
        found |= walk_up(name, bags)
    return found


def solution(lines):
    target = "shiny gold"
    bags = flip(read_in(lines))
    return len(walk_up(target, bags) ^ set([target]))


if __name__ == "__main__":
    print(solution((line[:-1] for line in sys.stdin)))
