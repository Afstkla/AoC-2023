from tqdm import tqdm

from src.utils import AdventOfCodeSolver


class Day5Solver(AdventOfCodeSolver):
    test = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
    maps: dict[str, str] = {}
    thing_to_values: dict[str, list[list[int]]] = {}
    seeds: list[int] = []

    def __init__(self):
        super().__init__(5)
        self._prepare_input(self.input_txt)

    def _save_map_part(self, map_part: str) -> None:
        lines = map_part.split("\n")
        (something, something_else) = lines[0].replace(" map:", "").split("-to-")
        self.maps[something] = something_else

        values = []
        for line in lines[1:]:
            values.append(list(map(int, line.split())))
        self.thing_to_values[something_else] = values

    def _prepare_input(self, input_txt: str) -> None:
        parts = input_txt.split("\n\n")

        self.seeds = list(map(int, parts[0].split(":")[1].strip().split()))

        for map_part in parts[1:]:
            self._save_map_part(map_part)

    def solve_first_part(self, input_txt: str) -> str:
        lowest_number = None
        for seed_number in self.seeds:
            source = "seed"
            value = seed_number
            while destination := self.maps.get(source):
                for line in self.thing_to_values[destination]:
                    if value >= line[1] and value < line[1] + line[2]:
                        value = line[0] + value - line[1]
                        break
                source = destination
            lowest_number = (
                value if lowest_number is None else min(lowest_number, value)
            )
        return str(lowest_number)

    def solve_second_part(self, input_txt: str) -> str:
        new_seeds = []
        for idx in tqdm(range(len(self.seeds) // 2)):
            new_seeds.extend(
                list(
                    range(
                        self.seeds[2 * idx],
                        self.seeds[2 * idx] + self.seeds[2 * idx + 1],
                    )
                )
            )
        self.seeds = new_seeds
        lowest_number = None
        for seed_number in tqdm(self.seeds):
            source = "seed"
            value = seed_number
            while destination := self.maps.get(source):
                for line in self.thing_to_values[destination]:
                    if value >= line[1] and value < line[1] + line[2]:
                        value = line[0] + value - line[1]
                        break
                source = destination
            lowest_number = (
                value if lowest_number is None else min(lowest_number, value)
            )
        return str(lowest_number)


if __name__ == "__main__":
    Day5Solver().solve_and_print()
