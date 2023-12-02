from abc import abstractmethod


class AdventOfCodeSolver:
    def __init__(self, day: int):
        self.day = day
        self.input_txt = self.get_input(day)

    @abstractmethod
    def solve_first_part(self, input_txt: str) -> str:
        pass

    @abstractmethod
    def solve_second_part(self, input_txt: str) -> str:
        pass

    def solve_and_print(self):
        print(f"Day {self.day}a: {self.solve_first_part(self.input_txt)}")
        print(f"Day {self.day}b: {self.solve_second_part(self.input_txt)}")

    def get_input(self, day: int) -> str:
        with open(f"inputs/input{day}.txt") as f:
            input_txt = f.read()
        return input_txt.strip()
