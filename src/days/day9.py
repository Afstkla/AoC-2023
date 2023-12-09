from src.utils import AdventOfCodeSolver


class Day9Solver(AdventOfCodeSolver):
    test = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""
    histories: list[list[int]] = []

    def __init__(self):
        super().__init__(9)
        self._prepare_input(self.input_txt)

    def _prepare_input(self, input_txt: str) -> None:
        self.histories = [
            [int(value) for value in line.split(" ")] for line in input_txt.split("\n")
        ]

    def _get_next_value(self, history: list[int], is_part_2: bool = False) -> int:
        if len(set(history)) == 1:
            return history[0]

        differences = [history[i] - history[i - 1] for i in range(1, len(history))]

        if is_part_2:
            return history[0] - self._get_next_value(differences, is_part_2)

        return self._get_next_value(differences, is_part_2) + history[-1]

    def solve_first_part(self, input_txt: str) -> str:
        return str(sum([self._get_next_value(history) for history in self.histories]))

    def solve_second_part(self, input_txt: str) -> str:
        return str(
            sum([self._get_next_value(history, True) for history in self.histories])
        )


if __name__ == "__main__":
    Day9Solver().solve_and_print()
