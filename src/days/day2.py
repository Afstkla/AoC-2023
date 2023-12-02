from src.utils import AdventOfCodeSolver


class Day2Solver(AdventOfCodeSolver):
    minimal_cubes_per_game = []
    
    def __init__(self):
        super().__init__(2)

        self.minimal_cubes_per_game = self._get_minimal_cubes_per_game(self.input_txt)

    def _get_minimal_cubes_per_game(self, input_txt: str) -> list[dict[str, int]]:
        minimal_cubes_per_game = []

        games = input_txt.split("\n")

        for game in games:
            max_cubes = {}

            rounds = game.split(": ")[1]

            for game_round in rounds.split("; "):
                for cube in game_round.split(", "):
                    cube_value, cube_name = cube.split(" ")
                    if cube_name not in max_cubes:
                        max_cubes[cube_name] = int(cube_value)
                    else:
                        max_cubes[cube_name] = max(max_cubes[cube_name], int(cube_value))
            
            minimal_cubes_per_game.append(max_cubes)
    
        return minimal_cubes_per_game


    def solve_first_part(self, input_txt: str) -> str:
        sum_of_game_numbers = 0

        for idx, game in enumerate(self.minimal_cubes_per_game):
            if game["red"] <= 12 and game["green"] <= 13 and game["blue"] <= 14:
                sum_of_game_numbers += idx + 1

        return str(sum_of_game_numbers)

    def solve_second_part(self, input_txt: str) -> str:
        sum_of_game_powers = 0

        for game in self.minimal_cubes_per_game:
            sum_of_game_powers += game.get("red", 0) * game.get("green", 0) * game.get("blue", 0)

        return str(sum_of_game_powers)


if __name__ == "__main__":
    Day2Solver().solve_and_print()
