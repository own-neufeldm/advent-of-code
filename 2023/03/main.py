import math
import re
import sys


def get_gear_ratio(match: re.Match, index: int, lines: list[str]) -> int:
    pattern = r"\d+"
    start_column = max(0, match.start()-1)
    end_column = min(len(match.string)-1, match.end())
    valid_range = list(range(start_column, end_column+1))
    start_row = max(0, index-1)
    end_row = min(len(lines)-1, index+1)
    adjacent_part_numbers: list[int] = []
    for row in range(start_row, end_row+1):
        string = lines[row]
        for part_number in re.finditer(pattern, string):
            if part_number.start() in valid_range or part_number.end()-1 in valid_range:
                adjacent_part_numbers.append(int(part_number.group(0)))
    if len(adjacent_part_numbers) != 2:
        return 0
    return math.prod(adjacent_part_numbers)


def is_part_number(match: re.Match, index: int, lines: list[str]) -> bool:
    pattern = r"[^a-zA-Z0-9_.]"
    start_column = max(0, match.start()-1)
    end_column = min(len(match.string)-1, match.end())
    start_row = max(0, index-1)
    end_row = min(len(lines)-1, index+1)
    for row in range(start_row, end_row+1):
        string = lines[row][start_column:end_column+1]
        if re.search(pattern, string) is not None:
            return True
    return False


def solve_part_one(lines: list[str]) -> int:
    sum = 0
    for index, line in enumerate(lines):
        for match in re.finditer(r"\d+", line):
            if is_part_number(match, index, lines):
                sum += int(match.group(0))
    return sum


def solve_part_two(lines: list[str]) -> int:
    sum = 0
    for index, line in enumerate(lines):
        for match in re.finditer(r"[*]", line):
            sum += get_gear_ratio(match, index, lines)
    return sum


def main() -> None:
    file = sys.argv[1]
    with open(file, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    print("Part One:", solve_part_one(lines))
    print("Part Two:", solve_part_two(lines))


if __name__ == "__main__":
    main()
