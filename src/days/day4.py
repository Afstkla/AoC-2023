from src.utils import AdventOfCodeSolver


class Day4Solver(AdventOfCodeSolver):
    test = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
    cards = []
    copies = []

    def __init__(self):
        super().__init__(4)
        self._prepare_input(self.input_txt)

    def _prepare_input(self, input_txt: str) -> None:
        lines = input_txt.split("\n")

        for line in lines:
            line_without_card = line.split(": ")[1]
            (winning, ours) = line_without_card.split("|")

            card = {
                "winning": [
                    int(x.strip()) for x in winning.split(" ") if x.strip() != ""
                ],
                "ours": [int(x.strip()) for x in ours.split(" ") if x.strip() != ""],
            }

            self.cards.append(card)
            self.copies.append(1)

    def solve_first_part(self, input_txt: str) -> str:
        total_sum = 0

        for card in self.cards:
            total_matching = set(card["winning"]).intersection(set(card["ours"]))

            if len(total_matching) > 0:
                extra_points = pow(2, len(total_matching) - 1)
                total_sum += extra_points

        return str(total_sum)

    def solve_second_part(self, input_txt: str) -> str:
        for idx, card in enumerate(self.cards):
            count_matching = len(set(card["winning"]).intersection(set(card["ours"])))

            for card_copies in range(count_matching):
                self.copies[idx + card_copies + 1] += self.copies[idx]

        return str(sum(self.copies))


if __name__ == "__main__":
    Day4Solver().solve_and_print()
