from stdlib import *


def part_1(lines):
    increases = 0
    depth = int(lines[0])
    for line in lines[1:]:
        new_depth = int(line)
        if new_depth > depth:
            increases += 1
        depth = new_depth

    return increases


def part_2(lines):
    increases = 0
    iterable = windowed(map(int, lines), 3)
    depth = sum(next(iterable))
    for group in iterable:
        new_depth = sum(group)
        if new_depth > depth:
            increases += 1
        depth = new_depth

    return increases


if __name__ == "__main__":
    input_lines = read_input()
    print("Part 1:", part_1(input_lines) or "")
    print("Part 2:", part_2(input_lines) or "")
