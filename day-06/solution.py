import string


def read_input(data: str) -> list:
    return [line.split() for line in data.strip().split("\n\n")]


def count_groups(groups: list, everyone: bool) -> int:
    total = 0
    for group in groups:
        answers = dict.fromkeys(string.ascii_lowercase, 0)

        for answer in group:
            for letter in answer:
                answers[letter] += 1

        total += sum([1 for letter in answers if answers[letter] == len(group)]) if everyone \
            else sum([1 for letter in answers if answers[letter]])

    return total


def part_one(groups: list) -> int:
    return count_groups(groups, everyone=False)


def part_two(groups: list) -> int:
    return count_groups(groups, everyone=True)


def tests():
    _test = """abc

a
b
c

ab
ac

a
a
a
a

b"""
    _data = read_input(_test)
    assert part_one(_data) == 11
    assert part_two(_data) == 6


if __name__ == '__main__':
    tests()
    _input = read_input(open(f"{__file__.rstrip('solution.py')}input.txt", "r").read())
    print(f'Day 06')
    print(f'> Puzzle 1: {part_one(_input)}')
    print(f'> Puzzle 2: {part_two(_input)}')
