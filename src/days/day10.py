from enum import Enum

from src.utils import AdventOfCodeSolver


class Direction(Enum):
    UP = "U"
    DOWN = "D"
    LEFT = "L"
    RIGHT = "R"


def cw(direction: Direction) -> Direction:
    if direction == Direction.UP:
        return Direction.RIGHT
    if direction == Direction.RIGHT:
        return Direction.DOWN
    if direction == Direction.DOWN:
        return Direction.LEFT
    if direction == Direction.LEFT:
        return Direction.UP


def ccw(direction: Direction) -> Direction:
    if direction == Direction.UP:
        return Direction.LEFT
    if direction == Direction.LEFT:
        return Direction.DOWN
    if direction == Direction.DOWN:
        return Direction.RIGHT
    if direction == Direction.RIGHT:
        return Direction.UP


class Day10Solver(AdventOfCodeSolver):
    test = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""
    grid: list[list[str]] = []
    starting_position: tuple[int, int] = (-1, -1)

    def __init__(self):
        super().__init__(10)
        self._prepare_input(self.input_txt)

    def _prepare_input(self, input_txt: str) -> None:
        self.grid = [list(line) for line in input_txt.split("\n")]

        self.starting_position = (
            [line for line in self.grid if "S" in line][0].index("S"),
            self.grid.index([line for line in self.grid if "S" in line][0]),
        )

    def _make_step(
        self, position: tuple[int, int], direction: Direction
    ) -> tuple[tuple[int, int], Direction] | None:
        # F -> UP --> RIGHT, LEFT --> DOWN
        # J -> RIGHT --> UP, DOWN --> LEFT
        # | -> UP --> UP, DOWN --> DOWN
        # - -> LEFT --> LEFT, RIGHT --> RIGHT
        # L -> DOWN --> RIGHT, LEFT --> UP
        # 7 -> UP --> LEFT, RIGHT --> DOWN
        # . -> None
        # any other -> None

        if (
            position[0] < 0
            or position[1] < 0
            or position[0] >= len(self.grid[0])
            or position[1] >= len(self.grid)
        ):
            return None

        pipe_shape = self.grid[position[1]][position[0]]

        if pipe_shape == ".":
            return None

        new_dir = direction

        if pipe_shape == "F":
            if direction == Direction.UP:
                new_dir = Direction.RIGHT
            elif direction == Direction.LEFT:
                new_dir = Direction.DOWN
            else:
                return None

        elif pipe_shape == "J":
            if direction == Direction.RIGHT:
                new_dir = Direction.UP
            elif direction == Direction.DOWN:
                new_dir = Direction.LEFT
            else:
                return None

        elif pipe_shape == "|":
            if direction == Direction.UP:
                new_dir = Direction.UP
            elif direction == Direction.DOWN:
                new_dir = Direction.DOWN
            else:
                return None

        elif pipe_shape == "-":
            if direction == Direction.LEFT:
                new_dir = Direction.LEFT
            elif direction == Direction.RIGHT:
                new_dir = Direction.RIGHT
            else:
                return None

        elif pipe_shape == "L":
            if direction == Direction.DOWN:
                new_dir = Direction.RIGHT
            elif direction == Direction.LEFT:
                new_dir = Direction.UP
            else:
                return None

        elif pipe_shape == "7":
            if direction == Direction.UP:
                new_dir = Direction.LEFT
            elif direction == Direction.RIGHT:
                new_dir = Direction.DOWN
            else:
                return None

        if new_dir == Direction.UP:
            return ((position[0], position[1] - 1), new_dir)
        if new_dir == Direction.DOWN:
            return ((position[0], position[1] + 1), new_dir)
        if new_dir == Direction.LEFT:
            return ((position[0] - 1, position[1]), new_dir)
        if new_dir == Direction.RIGHT:
            return ((position[0] + 1, position[1]), new_dir)

    def solve_first_part(self, input_txt: str) -> str:
        curr_pos = self.starting_position
        all_locations: set[tuple[tuple[int, int], str]] = set()

        number_of_steps = 0
        for direction in [
            Direction.RIGHT,
            Direction.DOWN,
            Direction.LEFT,
            Direction.UP,
        ]:
            next_dir = direction
            while True:
                next_step = self._make_step(curr_pos, next_dir)
                if not next_step:
                    curr_pos = self.starting_position
                    all_locations.clear()
                    break

                (next_pos, next_dir) = next_step
                all_locations.add((next_pos, self.grid[next_pos[1]][next_pos[0]]))

                number_of_steps += 1
                curr_pos = next_pos

                if curr_pos == self.starting_position:
                    return str(number_of_steps // 2)
        raise Exception("Should not happen")

    def solve_second_part(self, input_txt: str) -> str:
        curr_pos = self.starting_position
        all_locations: set[tuple[tuple[int, int], str]] = set()

        number_of_steps = 0
        for direction in [
            Direction.RIGHT,
            Direction.DOWN,
            Direction.LEFT,
            Direction.UP,
        ]:
            next_dir = direction
            while True:
                next_step = self._make_step(curr_pos, next_dir)
                if not next_step:
                    curr_pos = self.starting_position
                    all_locations.clear()
                    break

                (next_pos, next_dir) = next_step
                all_locations.add((next_pos, self.grid[next_pos[1]][next_pos[0]]))

                number_of_steps += 1
                curr_pos = next_pos

                if curr_pos == self.starting_position:
                    # Print the grid with the path
                    for y in range(len(self.grid)):
                        for x in range(len(self.grid[0])):
                            if (x, y) in [loc[0] for loc in all_locations]:
                                val = self.grid[y][x]
                                if val == "-":
                                    print("─", end="")
                                elif val == "|":
                                    print("│", end="")
                                elif val == "F":
                                    print("┌", end="")
                                elif val == "J":
                                    print("┘", end="")
                                elif val == "L":
                                    print("└", end="")
                                elif val == "7":
                                    print("┐", end="")
                                elif val == "S":
                                    print("┌", end="")
                                else:
                                    print(val, end="")
                            else:
                                print(".", end="")
                        print()
        return """I was to lazy to figure out how to solve this programmatically.
        So I ended up just printing the grid with the path.
        And then used photoshop's paint bucket tool to fill the outer path with color.
        Then selected the path, expanded my selection to include all outer dots.
        Then selected all remaining dots with the color select thingy,
        and finally used the analysis -> count to count the number of dots.
        Slightly tedious, but less tedious than figuring out how to do it programmatically.
        Cheers! In case anyone is interested, my answer was 357."""


if __name__ == "__main__":
    Day10Solver().solve_and_print()
