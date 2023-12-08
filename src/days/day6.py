import math

from src.utils import AdventOfCodeSolver


class Day6Solver(AdventOfCodeSolver):
    times_and_distances = []
    test = """Time:      7  15   30
Distance:  9  40  200"""

    def __init__(self):
        super().__init__(6)
        self.prepare_input(self.test)

    def prepare_input(self, input_txt: str) -> None:
        self.times_and_distances = []
        (times_str, distances_str) = input_txt.split("\n")
        times = list(map(int, times_str.split(":")[1].strip().split()))
        distances = list(map(int, distances_str.split(":")[1].strip().split()))

        for idx in range(len(times)):
            self.times_and_distances.append((times[idx], distances[idx]))

    def solve_first_part(self, input_txt: str) -> str:
        total_product = 1
        for idx in range(len(self.times_and_distances)):
            (time, distance) = self.times_and_distances[idx]
            total_product *= (
                time - 2 * ((time - math.sqrt((time**2) - 4 * distance)) // 2) - 1
            )
        return str(int(total_product))

    def solve_second_part(self, input_txt: str) -> str:
        self.prepare_input(input_txt.replace(" ", ""))
        return self.solve_first_part("")


if __name__ == "__main__":
    Day6Solver().solve_and_print()
