def read_input(data: str) -> list:
    return [list(x) for x in data.split('\n')]


def count_trees(trees: list, dx: int, dy: int) -> int:
    x, y, total, length, mod = 0, 0, 0, len(trees) - dy, len(trees[0])
    while y < length:
        x = (x + dx) % mod
        y += dy
        if trees[y][x] == '#':
            total += 1
    return total


def part_one(trees: list) -> int:
    return count_trees(trees, 3, 1)


def part_two(trees: list) -> int:
    slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    solution = 1
    for slope in slopes:
        solution *= count_trees(trees, slope[0], slope[1])
    return solution


def tests():
    _test = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""
    _data = read_input(_test)
    assert part_one(_data) == 7
    assert part_two(_data) == 336


if __name__ == '__main__':
    tests()
    _input = read_input(open(f"{__file__.rstrip('solution.py')}input.txt", "r").read())
    print(f'Day 03')
    print(f'> Puzzle 1: {part_one(_input)}')
    print(f'> Puzzle 2: {part_two(_input)}')
