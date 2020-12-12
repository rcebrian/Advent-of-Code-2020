def read_input(data: str) -> list:
    cleaned_data = []
    for line in data.split('\n'):
        txt = line.split()
        nums = txt[0].split("-")
        cleaned_data.append((int(nums[0]), int(nums[1]), txt[1][:1], txt[2]))
    return cleaned_data


def part_one(data: list) -> int:
    total = 0
    for val in data:
        n_min, n_max, letter, passwd = val
        n_char = passwd.count(letter)
        if n_min <= n_char <= n_max:
            total += 1
    return total


def part_two(data: list) -> int:
    total = 0
    for val in data:
        n_min, n_max, letter, passwd = val
        if (passwd[n_min - 1] == letter) ^ (passwd[n_max - 1] == letter):
            total += 1
    return total


def tests():
    _test = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""
    data = read_input(_test)
    assert part_one(data) == 2
    assert part_two(data) == 1


if __name__ == '__main__':
    tests()
    _input = read_input(open(f"{__file__.rstrip('solution.py')}input.txt", "r").read())
    print(f'Puzzle 1: {part_one(_input)}')
    print(f'Puzzle 2: {part_two(_input)}')
