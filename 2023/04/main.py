import sys
from dataclasses import dataclass
from typing import Self


@dataclass()
class Card():
    id: int
    winning_numbers: set[int]
    drawn_numbers: set[int]

    @classmethod
    def from_string(cls, string: str) -> Self:
        data = string.split(": ")
        meta_data, number_data = data[0].split(" "), data[1].split(" | ")
        id = int(meta_data[-1])
        winning_numbers = set(int(number) for number in number_data[0].split(" ") if number)
        drawn_numbers = set(int(number) for number in number_data[1].split(" ") if number)
        return cls(id, winning_numbers, drawn_numbers)

    @property
    def drawn_winning_numbers(self) -> set[int]:
        return self.drawn_numbers - (self.drawn_numbers - self.winning_numbers)

    def get_worth(self) -> int:
        if not self.drawn_winning_numbers:
            return 0
        return 2**(len(self.drawn_winning_numbers)-1)


def solve_part_one(lines: list[str]) -> int:
    sum = 0
    for line in lines:
        card = Card.from_string(line)
        sum += card.get_worth()
    return sum


def solve_part_two(lines: list[str]) -> int:
    cards = [Card.from_string(line) for line in lines]
    copies = {card.id: 1 for card in cards}
    for i, card in enumerate(cards):
        start = i + 1
        end = start + len(card.drawn_winning_numbers)
        for j in range(start, end):
            copies[j+1] = copies[j+1] + copies[start]
    return sum(copies.values())


def main() -> None:
    file = sys.argv[1]
    with open(file, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    print("Part One:", solve_part_one(lines))
    print("Part Two:", solve_part_two(lines))


if __name__ == "__main__":
    main()
