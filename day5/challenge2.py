import sys
from itertools import product


def row_value(row):
    if row[1] == "B":
        return 64 >> row[0]
    return 0


def col_value(col):
    if col[1] == "R":
        return 4 >> col[0]
    return 0


def calc_line(line):
    rows = line[:-3]
    cols = line[-3:]
    row = sum(map(row_value, enumerate(rows)))
    col = sum(map(col_value, enumerate(cols)))
    return row * 8 + col


def prod_to_str(tup):
    return "".join(list(tup))


def generate_all_cols(row_str):
    return (row_str + prod_to_str(col) for col in product("LR", repeat=3))


def solution(lines):
    seats = set(map(calc_line, lines))
    low = min(seats)
    high = max(seats)
    full_range = set(range(low, high + 1))
    return full_range - seats


if __name__ == "__main__":
    print(solution((line[:-1] for line in sys.stdin)))
