import sys


def take_until_repeat(gen, accessor=lambda x: x):
    seen = set()
    for item in gen:
        value = accessor(item)
        if value not in seen:
            seen |= {value}
            yield item
        else:
            break


def disassemble(ops):
    def disasm(line):
        (op, x) = line
        return f"{ops[op]} {x:+d}"

    return disasm


def debug(history, code):
    ops = ["acc", "jmp", "nop"]
    disasm_ops = dict(enumerate(ops))
    string = "\n".join(
        f"{instruction}\t{item}"
        for instruction, item in zip(
            map(disassemble(disasm_ops), (code[item.pc] for item in history)),
            history,
        )
    )
    sys.stderr.write(f"{string}\n")
