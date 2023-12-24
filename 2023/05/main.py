import sys
from dataclasses import dataclass
from typing import Self


@dataclass()
class Range():
    destination_start: int
    source_start: int
    length: int

    @classmethod
    def from_string(cls, string: str) -> Self:
        values = [int(value) for value in string.split(" ") if value]
        return cls(
            destination_start=values[0],
            source_start=values[1],
            length=values[2]
        )

    def contains(self, source: int) -> bool:
        return source in range(self.source_start, self.source_start + self.length)


@dataclass()
class Map():
    ranges: list[Range]

    @classmethod
    def from_string(cls, string: str, name: str) -> Self:
        chunks = string.split("\n\n")
        raw_map = ""
        for chunk in chunks:
            if chunk.startswith(f"{name} map"):
                raw_map = chunk
        if not raw_map:
            raise ValueError(f"Map {name!r} not found.")
        ranges = [Range.from_string(line) for line in raw_map.split("\n")[1:]]
        return cls(ranges)

    def convert(self, value: int) -> int:
        for rng in self.ranges:
            if value in range(rng.source_start, rng.source_start + rng.length):
                return value - (rng.source_start - rng.destination_start)
        return value


@dataclass()
class Almanac():
    seed_to_soil: Map
    soil_to_fertilizer: Map
    fertilizer_to_water: Map
    water_to_light: Map
    light_to_temperature: Map
    temperature_to_humidity: Map
    humidity_to_location: Map

    @classmethod
    def from_string(cls, string: str) -> Self:
        return cls(
            Map.from_string(string, "seed-to-soil"),
            Map.from_string(string, "soil-to-fertilizer"),
            Map.from_string(string, "fertilizer-to-water"),
            Map.from_string(string, "water-to-light"),
            Map.from_string(string, "light-to-temperature"),
            Map.from_string(string, "temperature-to-humidity"),
            Map.from_string(string, "humidity-to-location"),
        )

    def get_location_for_seed(self, seed: int) -> int:
        soil = self.seed_to_soil.convert(seed)
        fertilizer = self.soil_to_fertilizer.convert(soil)
        water = self.fertilizer_to_water.convert(fertilizer)
        light = self.water_to_light.convert(water)
        temperature = self.light_to_temperature.convert(light)
        humidity = self.temperature_to_humidity.convert(temperature)
        return self.humidity_to_location.convert(humidity)


def solve_part_one(content: str) -> int:
    seeds = [int(s) for s in content.split("\n")[0].split(": ")[1].split(" ") if s]
    almanac = Almanac.from_string(content)
    return min(almanac.get_location_for_seed(s) for s in seeds)


def solve_part_two(content: str) -> int:
    seed_data = [int(s) for s in content.split("\n")[0].split(": ")[1].split(" ") if s]
    almanac = Almanac.from_string(content)
    return min(
        almanac.get_location_for_seed(j)
        for i in range(0, len(seed_data), 2)
        for j in range(seed_data[i], seed_data[i]+seed_data[i+1])
    )


def main() -> None:
    file = sys.argv[1]
    with open(file, "r") as f:
        content = f.read()
    print("Part One:", solve_part_one(content))
    print("Part Two:", solve_part_two(content))


if __name__ == "__main__":
    main()
