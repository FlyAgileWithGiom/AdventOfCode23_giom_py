from unittest import skip
from day4.logic import parse_numbers, parse_line, detect_matches, calculate_score, score_pile

EXAMPLE = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''


REAL_LINE_EXAMPLE='Card   1: 58  6 71 93 96 38 25 29 17  8 | 79 33 93 58 53 96 71  8 67 90 17  6 46 85 64 25 73 32 18 52 77 16 63  2 38'
# shopping list
# 0. parse a line into its components
# 1. find how many wonning cards
# 2. make it the power of 2 to fet the score
# final. compare to the example for safety
# create a main() to run the full input


class TestPart1:

    def test_arse_double_digits_serie(self):
        assert parse_numbers(' 41 48 83 86 17') == [41, 48, 83, 86, 17]

    def test_parse_card_into_id_winnings_candidates(self):
        assert len(
            parse_line(
                'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53')) == 3

    def test_parse_card_picks_up_card_id(self):
        assert parse_line(
            'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53')[0] == 1

    def test_parse_card_picks_up_winnings_numbers(self):
        assert parse_line(
            'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53')[1] == [
                41, 48, 83, 86, 17
            ]

    def test_parse_card_picks_up_candidate_numbers(self):
        assert parse_line(
            'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53')[2] == [
                83, 86, 6, 31, 17, 9, 48, 53
            ]

    def test_detect_matches(self):
        assert detect_matches(
            'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53') == 4

    def test_calculate_score_zero_when_no_match(self):
        assert calculate_score('Card 1: 10 11 12 13 14 | 20 21 22 23 24') == 0

    def test_calculate_score_one_when_one_match(self):
        assert calculate_score('Card 1: 10 11 12 13 14 | 10 21 22 23 24') == 1

    def test_calculate_score_double_for_each_extra_match(self):
        assert calculate_score(
            'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53') == 8

    def test_score_card2(self):
        assert calculate_score(
            'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19') == 2

    def test_total_score_pile_on_example(self):
        assert score_pile(EXAMPLE) == 13
        
    def test_score_real_card(self):
        assert calculate_score(REAL_LINE_EXAMPLE) == 256

