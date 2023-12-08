import datetime
import logging
from abc import abstractmethod

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(message)s")


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
        log.info(f"{'=' * 30}\nSTART DAY {self.day}\n{'=' * 30}")
        start = datetime.datetime.now()
        log.info(f"Day {self.day}a: {self.solve_first_part(self.input_txt)}")
        after_part_one = datetime.datetime.now()
        log.info(f"Day {self.day}b: {self.solve_second_part(self.input_txt)}")
        total_time = datetime.datetime.now()

        log.info(
            f"""

Times:
Part 1: {after_part_one - start}
Part 2: {total_time - after_part_one}
Total: {total_time - start}

END DAY {self.day}
{"=" * 30}
"""
        )

    def get_input(self, day: int) -> str:
        with open(f"inputs/input-{day}.txt") as f:
            input_txt = f.read()
        return input_txt.strip()
