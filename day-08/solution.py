_JMP, _NOP, _ACC = 'jmp', 'nop', 'acc'


def read_input(data: str) -> list:
    return [line.split() for line in data.strip().split('\n')]


def run(instructions: list) -> tuple:
    acc, pos, visited = 0, 0, []

    while pos not in visited and pos < len(instructions):
        visited.append(pos)
        instrc, val = instructions[pos][0], int(instructions[pos][1])
        if instrc == _ACC:
            acc += val
        if instrc == _JMP:
            pos += val - 1

        pos += 1

    return acc, pos


def part_one(instructions: list) -> int:
    return run(instructions)[0]


def part_two(instructions: list) -> int:
    for i in range(len(instructions)):
        if instructions[i][0] == _JMP:
            instructions[i][0] = _NOP
            acc, pos = run(instructions)
            instructions[i][0] = _JMP

        elif instructions[i][0] == _NOP:
            instructions[i][0] = _JMP
            acc, pos = run(instructions)
            instructions[i][0] = _NOP

        else:
            continue

        if pos == len(instructions):
            return acc


def tests():
    _test = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
    _data = read_input(_test)
    assert part_one(_data) == 5
    assert part_two(_data) == 8


if __name__ == '__main__':
    tests()
    _input = read_input(open(f"{__file__.rstrip('solution.py')}input.txt", "r").read())
    print(f'Day 08')
    print(f'> Puzzle 1: {part_one(_input)}')
    print(f'> Puzzle 2: {part_two(_input)}')
