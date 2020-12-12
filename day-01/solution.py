def read_input() -> list:
    with open(f"{__file__.rstrip('solution.py')}input.txt", "r") as f:
        return [int(line) for line in f.readlines()]


def part_one(data: list) -> int:
    for val in data:
        second = 2020 - val
        if second in data:
            return second * val


def part_two(data: list) -> int:
    for i in data:
        for j in data:
            third = 2020 - i - j
            if third in data:
                return i * j * third


def tests():
    data = [int(val) for val in """1721
979
366
299
675
1456""".split('\n')]
    assert part_one(data) == 514579
    assert part_two(data) == 241861950


if __name__ == '__main__':
    _input = read_input()
    tests()
    assert part_one(_input) == 539851
    assert part_two(_input) == 212481360
