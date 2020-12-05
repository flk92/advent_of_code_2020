import sys
import re
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

    BYR_RE = re.compile(r"\d{4}")
    IYR_RE = BYR_RE
    EYR_RE = BYR_RE
    HGT_RE = re.compile(r"\d+(cm|in)")
    HCL_RE = re.compile(r"#[0-9a-fA-F]{6}")
    ECL_RE = re.compile(r"(amb|blu|brn|gry|grn|hzl|oth)")
    PID_RE = re.compile(r"\d{9}")

    def is_valid(self):
        validators = [
            (self.byr, self.byr_valid),
            (self.iyr, self.iyr_valid),
            (self.eyr, self.eyr_valid),
            (self.hgt, self.hgt_valid),
            (self.hcl, self.hcl_valid),
            (self.ecl, self.ecl_valid),
            (self.pid, self.pid_valid),
        ]

        def validate(v_pair):
            return v_pair[0] is not None and v_pair[1]()

        num_invalid = sum(1 for v_pair in validators if not validate(v_pair))
        return num_invalid == 0

    def yr_valid(exp, field, year_range):
        match = exp.fullmatch(field)
        if match:
            value = int(match.group(0))
            return value >= year_range[0] and value <= year_range[1]
        return False

    def byr_valid(self):
        return Passport.yr_valid(Passport.BYR_RE, self.byr, (1920, 2002))

    def iyr_valid(self):
        return Passport.yr_valid(Passport.IYR_RE, self.iyr, (2010, 2020))

    def eyr_valid(self):
        return Passport.yr_valid(Passport.EYR_RE, self.eyr, (2020, 2030))

    def hgt_valid(self):
        match = Passport.HGT_RE.fullmatch(self.hgt)
        if match:
            string = match.group(0)
            value = int(string[:-2])
            metric = string[-2:]
            if metric == "cm":
                return value >= 150 and value <= 193
            else:
                return value >= 59 and value <= 76
        return False

    def hcl_valid(self):
        return Passport.HCL_RE.fullmatch(self.hcl) is not None

    def ecl_valid(self):
        return Passport.ECL_RE.fullmatch(self.ecl) is not None

    def pid_valid(self):
        return Passport.PID_RE.fullmatch(self.pid) is not None


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
