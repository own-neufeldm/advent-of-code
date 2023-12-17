import sys


NAMES = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_first_digit(string: str, names: dict[str, str], step: int = 1) -> str:
    first_digit = None
    first_index = len(string) - 1
    string = string[::step]
    for name in names:
        index = string.find(name[::step])
        if index >= 0 and index < first_index:
            first_index = index
            first_digit = names[name]
    for index, char in enumerate(string):
        if char.isdigit() and index <= first_index:
            first_digit = char
            break
    if first_digit is not None:
        return first_digit
    raise ValueError(f"String {string!r} has no digits.")


def solve(lines: list[str]) -> int:
    sum = 0
    for line in lines:
        first_digit = get_first_digit(line, NAMES)
        last_digit = get_first_digit(line, NAMES, -1)
        sum += int(first_digit + last_digit)
    return sum


def main() -> None:
    file = sys.argv[1]
    with open(file, "r") as f:
        lines = [s.strip() for s in f.readlines()]
    print(solve(lines))
    return None


if __name__ == "__main__":
    main()
