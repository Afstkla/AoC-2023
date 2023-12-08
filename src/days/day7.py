from src.utils import AdventOfCodeSolver


class Day7Solver(AdventOfCodeSolver):
    test = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
    hands: dict[str, int] = {}

    def __init__(self):
        super().__init__(7)
        self._prepare_input(self.input_txt)

    def _prepare_input(self, input_txt: str) -> None:
        for line in input_txt.split("\n"):
            hand, value = line.split(" ")
            self.hands[hand] = int(value)

    def hand_is_higher(self, hand_1: str, hand_2: str, with_jokers: bool) -> bool:
        character_count_1 = self.get_character_count(hand_1)
        character_count_2 = self.get_character_count(hand_2)

        hand1_worth = self.get_hand_worth(character_count_1, with_jokers)
        hand2_worth = self.get_hand_worth(character_count_2, with_jokers)

        if hand1_worth > hand2_worth:
            return True
        if hand1_worth < hand2_worth:
            return False

        for idx in range(len(hand_1)):
            if hand_1[idx] != hand_2[idx]:
                return self._is_more_valuable(hand_1[idx], hand_2[idx], with_jokers)

        raise ValueError(f"This should never happen. Hand1: {hand_1}, Hand2: {hand_2}")

    def naive_sort_hands(self, hands: list[str], with_jokers: bool) -> list[str]:
        sorted_hands = []
        for hand in hands:
            if not sorted_hands:
                sorted_hands.append(hand)
                continue

            for idx, sorted_hand in enumerate(sorted_hands):
                if self.hand_is_higher(hand, sorted_hand, with_jokers):
                    sorted_hands.insert(idx, hand)
                    break
            else:
                sorted_hands.append(hand)

        return sorted_hands

    def get_hand_worth(self, character_count: dict, with_jokers: bool) -> int:
        if with_jokers:
            jokers = character_count.pop("J", 0)

            if jokers == 5:
                return 7

            if jokers > 0:
                character_count[max(character_count, key=character_count.get)] += jokers  # type: ignore

        if max(character_count.values()) == 5:
            return 7
        if max(character_count.values()) == 4:
            return 6
        if max(character_count.values()) == 3:
            if 2 in character_count.values():
                return 5
            return 4
        if max(character_count.values()) == 2:
            if len(character_count) == 3:
                return 3
            return 2
        return 1

    def get_character_count(self, hand: str) -> dict:
        character_count = {}
        for char in hand:
            character_count[char] = character_count.get(char, 0) + 1
        return character_count

    def _is_more_valuable(self, char_1: str, char_2: str, with_jokers: bool) -> bool:
        order = "AKQT98765432J" if with_jokers else "AKQJT98765432"
        return order.find(char_1) < order.find(char_2)

    def solve_first_part(self, input_txt: str) -> str:
        just_hands = list(self.hands.keys())
        sorted_hands = self.naive_sort_hands(just_hands, False)

        total_prod = 0
        for idx, hand in enumerate(reversed(sorted_hands)):
            total_prod += (1 + idx) * self.hands[hand]

        return str(total_prod)

    def solve_second_part(self, input_txt: str) -> str:
        just_hands = list(self.hands.keys())
        sorted_hands = self.naive_sort_hands(just_hands, True)

        total_prod = 0
        for idx, hand in enumerate(reversed(sorted_hands)):
            total_prod += (1 + idx) * self.hands[hand]

        return str(total_prod)


if __name__ == "__main__":
    Day7Solver().solve_and_print()
