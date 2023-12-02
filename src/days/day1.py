import re

from src.utils import AdventOfCodeSolver


class Day1Solver(AdventOfCodeSolver):
    def __init__(self):
        super().__init__(1)

    def solve_first_part(self, input_txt: str) -> str:
        solution = 0

        for line in input_txt.split("\n"):
            first_digit = re.sub(r"[^\d]*(\d).*", r"\1", line)
            last_digit = re.sub(r".*(\d)[^\d]*", r"\1", line)

            solution += 10 * int(first_digit) + int(last_digit)

        return str(solution)

    def solve_second_part(self, input_txt: str) -> str:
        return str(self.solve_first_part(self.words_to_digits(input_txt)))

    def words_to_digits(self, input_txt: str) -> str:
        lookup = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
            "zero": 0,
        }

        for key, value in lookup.items():
            # re-add key again, as sometimes stuff like "eightwo" happens, and we want
            # to parse both "eight" and "two" in that case
            input_txt = re.sub(key, key + str(value) + key, input_txt)
        return input_txt


if __name__ == "__main__":
    Day1Solver().solve_and_print()
