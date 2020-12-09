import sys
from dataclasses import dataclass
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


def assemble(lines):
    ops = dict(map(reversed, enumerate(["acc", "jmp", "nop"])))

    def asm(line):
        (op, x) = line.split(" ")
        return (ops[op], int(x))

    return list(map(asm, lines))


def break_on_loop(game, code):
    history = util.take_until_repeat(run(game, code), lambda state: state.pc)
    return list(history)


def solution(lines):
    game = Game()
    code = assemble(lines)
    history = break_on_loop(game, code)
    return history[-1].acc


if __name__ == "__main__":
    print(solution((line[:-1] for line in sys.stdin)))
