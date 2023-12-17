import math
import sys
from dataclasses import dataclass, fields
from typing import Self


@dataclass(order=True)
class GameSet():
    red: int = 0
    green: int = 0
    blue: int = 0

    @classmethod
    def from_string(cls, string: str) -> Self:
        kwargs = {}
        drafts = [draft for draft in string.split(", ")]
        for draft in drafts:
            data = draft.split(" ")
            kwargs.update({data[1]: int(data[0])})
        return cls(**kwargs)


@dataclass()
class Game():
    id: int
    sets: list[GameSet]

    @classmethod
    def from_string(cls, string: str) -> Self:
        colon_index = string.index(":")
        metadata, set_data = string[:colon_index], string[colon_index+2:]
        id = int(metadata.split(" ")[1])
        sets = [GameSet.from_string(set.strip()) for set in set_data.split(";")]
        return cls(id, sets)

    def is_possible(self, config: GameSet) -> bool:
        return all(
            getattr(set, field.name) <= getattr(config, field.name)
            for set in self.sets
            for field in fields(set)
        )

    def get_power(self) -> int:
        return math.prod(
            max(getattr(set, field.name) for set in self.sets)
            for field in fields(GameSet)
        )


def solve_possible(lines: list[str], config: GameSet) -> int:
    sum = 0
    for line in lines:
        game = Game.from_string(line)
        if game.is_possible(config):
            sum += game.id
    return sum


def solve_max(lines: list[str]) -> int:
    sum = 0
    for line in lines:
        game = Game.from_string(line)
        sum += game.get_power()
    return sum


def main() -> None:
    file = sys.argv[1]
    with open(file, "r") as f:
        lines = [s.strip() for s in f.readlines()]
    print("Part One:", solve_possible(lines, GameSet(red=12, green=13, blue=14)))
    print("Part Two:", solve_max(lines))


if __name__ == "__main__":
    main()
