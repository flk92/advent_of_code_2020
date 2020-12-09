import sys
from dataclasses import dataclass
from itertools import dropwhile
import util


@dataclass
class Game:
    pc: int = 0
    acc: int = 0


def acc(game, x):
    return Game(pc=game.pc + 1, acc=game.acc + x)


def jmp(game, x):
    return Game(pc=max(0, game.pc + x), acc=game.acc)


def nop(game, x):
    return Game(pc=game.pc + 1, acc=game.acc)


def dispatch(game, code):
    ops = [acc, jmp, nop]
    (op, x) = code[game.pc]
    return ops[op](game, x)


def run(game, code):
    code_len = len(code)

    def step(game):
        if game:
            if game.pc < code_len:
                yield game
                yield from step(dispatch(game, code))
            else:
                yield game

    return step(game)


def assemble(ops):
    def asm(line):
        (op, x) = line.split(" ")
        return (ops[op], int(x))

    return asm


def break_on_loop(game, code):
    history = util.take_until_repeat(run(game, code), lambda state: state.pc)
    return list(history)


def flip(instruction):
    (op, x) = instruction
    if op == 0:
        return instruction
    return (op ^ 0b11, x)


def pc_is_not_eof(code_len):
    return lambda history: history[-1].pc < code_len


def generate_backtracked_fixes(history, code):
    reverse_history = reversed(history)

    def possibly_corrupted(item):
        return code[item.pc][0] != 0

    for item in reverse_history:
        if possibly_corrupted(item):
            modified_code = code[:]
            modified_code[item.pc] = flip(code[item.pc])
            yield break_on_loop(item, modified_code)


def solution(lines):
    ops = ["acc", "jmp", "nop"]
    asm_ops = dict(map(reversed, enumerate(ops)))
    game = Game()
    code = list(map(assemble(asm_ops), lines))

    history = break_on_loop(game, code)
    is_infinite_loop = pc_is_not_eof(len(code))

    if is_infinite_loop(history):
        try:
            attempt = generate_backtracked_fixes(history, code)
            result = next(dropwhile(is_infinite_loop, attempt))
            return result[-1].acc
        except StopIteration:
            return None
    return history[-1].acc


if __name__ == "__main__":
    print(solution((line[:-1] for line in sys.stdin)))
