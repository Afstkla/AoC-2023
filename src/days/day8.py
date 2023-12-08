import math

from src.utils import AdventOfCodeSolver


class Day8Solver(AdventOfCodeSolver):
    test = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""
    test_2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

    test_part_2 = """LR

AAA = (ZZZ, ZZZ)
ZZZ = (ZZZ, ZZZ)
11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""
    moves: str
    maps: dict[str, list[str]] = {}

    def __init__(self):
        super().__init__(8)
        self._prepare_input(self.input_txt)

    def _prepare_input(self, input_txt: str) -> None:
        self.maps = {}

        (self.moves, lines) = input_txt.split("\n\n")
        for line in lines.split("\n"):
            (key, value) = line.split(" = ")
            self.maps[key] = value.replace("(", "").replace(")", "").split(", ")

    def solve_first_part(self, input_txt: str) -> str:
        current_loc = "AAA"
        move_count = 0
        while True:
            if current_loc == "ZZZ":
                return str(move_count)
            if self.moves[move_count % len(self.moves)] == "R":
                current_loc = self.maps[current_loc][1]
            else:
                current_loc = self.maps[current_loc][0]
            move_count += 1

    def _find_periodicity_in_sequence(self, starting_point: str) -> int:
        visited_locations_with_index: dict[str, int] = {}

        idx = 0

        current_loc = starting_point
        while True:
            if self.moves[idx % len(self.moves)] == "R":
                current_loc = self.maps[current_loc][1]
            else:
                current_loc = self.maps[current_loc][0]

            idx += 1

            if period_idx := visited_locations_with_index.get(
                current_loc + str(idx % len(self.moves)), None
            ):
                period_length = idx - period_idx
                return period_length

            visited_locations_with_index[current_loc + str(idx % len(self.moves))] = idx

    def solve_second_part(self, input_txt: str) -> str:
        starting_locs = filter(lambda x: x.endswith("A"), self.maps.keys())

        periodicities: list[int] = []
        for loc in starting_locs:
            periodicities.append(self._find_periodicity_in_sequence(loc))
        return str(math.lcm(*periodicities))


if __name__ == "__main__":
    Day8Solver().solve_and_print()
