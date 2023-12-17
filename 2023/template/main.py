import sys


def solve_part_one(lines: list[str]) -> int:
    sum = 0
    return sum


def solve_part_two(lines: list[str]) -> int:
    sum = 0
    return sum


def main() -> None:
    file = sys.argv[1]
    with open(file, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    print("Part One:", solve_part_one(lines))
    print("Part Two:", solve_part_two(lines))


if __name__ == "__main__":
    main()
