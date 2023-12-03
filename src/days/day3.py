from src.utils import AdventOfCodeSolver


class Day3Solver(AdventOfCodeSolver):
    test = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
    numbers_with_coordinates = []
    special_characters_with_coordinates = {}
    max_x = 0
    max_y = 0

    def __init__(self):
        super().__init__(3)
        self._prepare_input(self.input_txt)

    def _prepare_input(self, input_txt: str) -> None:
        lines = input_txt.split("\n")

        self.max_x = len(lines[0])
        self.max_y = len(lines)

        for y, line in enumerate(lines):
            number = 0

            coordinate = (0,0)
            number_coordinates = []
            
            for x, character in enumerate(line):
                coordinate = (x, y)
                if character.isdigit():
                    number = number * 10 + int(character)
                    number_coordinates.append((x, y))
                    continue

                if character == ".":
                    pass
                elif character in self.special_characters_with_coordinates:
                    self.special_characters_with_coordinates[character].append(coordinate)
                else:
                    self.special_characters_with_coordinates[character] = [coordinate]

                self.numbers_with_coordinates.append({number: number_coordinates})
                number = 0
                number_coordinates = []
            
            if number != 0:
                self.numbers_with_coordinates.append({number: number_coordinates})
        

    def solve_first_part(self, input_txt: str) -> str:
        all_valid_coordinates_from_symbols = []
        for _, coordinates in self.special_characters_with_coordinates.items():
            for x_diff in range(-1, 2):
                for y_diff in range(-1, 2):
                    if x_diff == 0 and y_diff == 0:
                        continue

                    for coordinate in coordinates:
                        new_coordinate = (coordinate[0] + x_diff, coordinate[1] + y_diff)
                        if new_coordinate[0] < 0 or new_coordinate[0] >= self.max_x or new_coordinate[1] < 0 or new_coordinate[1] >= self.max_y:
                            continue
                        all_valid_coordinates_from_symbols.append(new_coordinate)

        total_sum = 0

        for number_with_coordinate in self.numbers_with_coordinates:
            number = list(number_with_coordinate.keys())[0]
            coordinates = list(number_with_coordinate.values())[0]
            for coordinate in coordinates:
                if coordinate in all_valid_coordinates_from_symbols:
                    total_sum += number
                    break

        return str(total_sum)

    def solve_second_part(self, input_txt: str) -> str:
        all_valid_coordinates_per_star = []
        coordinates = self.special_characters_with_coordinates["*"]
        for coordinate in coordinates:
            valid_coordinates = [].copy()
            for x_diff in range(-1, 2):
                for y_diff in range(-1, 2):
                    if x_diff == 0 and y_diff == 0:
                        continue

                    new_coordinate = (coordinate[0] + x_diff, coordinate[1] + y_diff)
                    if new_coordinate[0] < 0 or new_coordinate[0] >= self.max_x or new_coordinate[1] < 0 or new_coordinate[1] >= self.max_y:
                        continue
                    valid_coordinates.append(new_coordinate)
            all_valid_coordinates_per_star.append(valid_coordinates)

        total_sum = 0

        for valid_coordinates in all_valid_coordinates_per_star:
            matching_numbers = []
            for number_with_coordinate in self.numbers_with_coordinates:
                number = list(number_with_coordinate.keys())[0]
                coordinates = list(number_with_coordinate.values())[0]
                for coordinate in coordinates:
                    if coordinate in valid_coordinates:
                        matching_numbers.append(number)

                        if len(matching_numbers) > 2:
                            break
                        
                        break
                
            if len(matching_numbers) == 2:
                total_sum += matching_numbers[0] * matching_numbers[1]

        return str(total_sum)


if __name__ == "__main__":
    Day3Solver().solve_and_print()
