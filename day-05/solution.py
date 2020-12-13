def read_input(data: str) -> list:
    return [int(line
                .replace('F', '0')
                .replace('B', '1')
                .replace('L', '0')
                .replace('R', '1'), 2)
            for line in data.split('\n')]


def part_one(decoded_seats: list) -> int:
    return max(decoded_seats)


def part_two(seats: list) -> int:
    for i in range(min(seats), max(seats)):
        if i not in seats and (i - 1) in seats and (i + 1) in seats:
            return i


def tests():
    assert part_one(read_input('FBFBBFFRLR')) == 357
    assert part_one(read_input('BFFFBBFRRR')) == 567
    assert part_one(read_input('FFFBBBFRRR')) == 119
    assert part_one(read_input('BBFFBBFRLL')) == 820


if __name__ == '__main__':
    tests()
    _input = read_input(open(f"{__file__.rstrip('solution.py')}input.txt", "r").read())
    print(f'Day 05')
    print(f'> Puzzle 1: {part_one(_input)}')
    print(f'> Puzzle 2: {part_two(_input)}')
