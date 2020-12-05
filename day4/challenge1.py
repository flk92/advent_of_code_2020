import sys
from dataclasses import dataclass


@dataclass
class Passport:
    byr: str = None
    iyr: str = None
    eyr: str = None
    hgt: str = None
    hcl: str = None
    ecl: str = None
    pid: str = None
    cid: str = None

    def is_valid(self):
        items = filter(lambda item: item[0] != "cid", vars(self).items())
        return len(list(filter(lambda item: item[1] is None, items))) == 0


def passport(lines):
    input_str = map(str.split, lines)
    values = dict(item.split(":") for items in input_str for item in items)
    return Passport(**values)


def passports(lines):
    acc = []
    passports = []
    for line in lines:
        if line != "":
            acc.append(line)
        else:
            passports.append(passport(acc))
            acc = []
    if len(acc) > 0:
        passports.append(passport(acc))
    return passports


def solution(lines):
    return sum((1 for passport in passports(lines) if passport.is_valid()))


if __name__ == "__main__":
    print(solution((line[:-1] for line in sys.stdin)))
