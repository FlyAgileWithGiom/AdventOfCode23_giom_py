import re
from unittest import skip

SCHEMATIC_EXAMPLE = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''

SCHEMATIC_AS_TABLE = [
    '467..114..', '...*......', '..35..633.', '......#...', '617*......',
    '.....+.58.', '..592.....', '......755.', '...$.*....', '.664.598..'
]


def to_xy_map(input):
    return input.splitlines()


def scan_part_numbers(line):
    return re.findall(r'(\d+)', line)


def is_adjacent(table, line, character, number_str):
    if is_before_a_symbol(character, line, number_str, table):
        return True
    if is_after_a_symbol(character, line, table):
        return True
    if is_under_a_symbol(character, line, number_str, table):
        return True
    if is_over_a_symbol(character, line, number_str, table):
        return True
    return False


def is_under_a_symbol(character, line, number_str, table):
    if line <= 0:
        return False
    return has_symbol(table[line - 1], character - 1, len(number_str) + 2)


def is_last_line_or_beyond(table, line):
    last_line = len(table) - 1
    return line >= last_line


def is_over_a_symbol(character, line, number_str, table):
    if is_last_line_or_beyond(table, line):
        return False

    return has_symbol(table[line + 1], character - 1, len(number_str) + 2)


def is_after_a_symbol(character, line, table):
    return is_symbol(table[line], character - 1)


def is_before_a_symbol(character, line, number_str, table):
    return is_symbol(table[line], character + len(number_str))


SYMBOL_MATCHER = re.compile(r'[*$#]')


def has_symbol(line, start, length):
    if start < 0 or start + length >= len(line):
        return False

    return SYMBOL_MATCHER.search(line[start:start + length]) is not None


def is_symbol(line, pos):
    return has_symbol(line, pos, 1)


class TestDay3:

    def test_can_turn_input_into_lines(self):
        assert len(to_xy_map(SCHEMATIC_EXAMPLE)) == 10
        assert len(to_xy_map(SCHEMATIC_EXAMPLE)[0]) == 10 

    def test_can_pick_up_numbers_on_a_line(self):
        assert scan_part_numbers("467..114..") == ['467', '114']

    def test_is_symbol_detects_star_dollar_hashtag(self):
        assert has_symbol('617*..', 3, 1)
        assert has_symbol('617$..', 3, 1)
        assert has_symbol('617#..', 3, 1)
        assert not has_symbol('617..', 3, 1)

    def test_detect_string_not_before_a_symbol(self):
        assert not is_adjacent(['467..'], 0, 0, '467')

    def test_detect_string_not_after_a_symbol(self):
        assert not is_adjacent(['..617'], 0, 3, '617')

    def test_detect_string_not_under_a_symbol(self):
        assert not is_adjacent(['.....', '.617.'], 1, 2, '617')

    def test_detect_string_not_over_a_symbol(self):
        assert not is_adjacent(['.617.', '.....'], 0, 2, '617')

    def test_detect_string_not_adjacent_to_a_symbol(self):
        assert not is_adjacent(['.....', '.617.', '.....'], 1, 2, '617')

    def test_detect_string_before_a_symbol(self):
        assert is_adjacent(['..617*..'], 0, 2, '617')

    def test_detect_string_after_a_symbol(self):
        assert is_adjacent(['.*617..'], 0, 2, '617')

    def test_detect_string_border_left(self):
        assert not is_adjacent(['617..*'], 0, 0, '617')

    def test_detect_string_border_left(self):
        assert not is_adjacent(['*..617'], 0, 3, '617')

    def test_detect_string_border_right(self):
        assert is_adjacent(['.*.....', '..617..'], 1, 2, '617')
        assert is_adjacent(['..*....', '..617..'], 1, 2, '617')
        assert is_adjacent(['...*...', '..617..'], 1, 2, '617')
        assert is_adjacent(['....*..', '..617..'], 1, 2, '617')
        assert is_adjacent(['.....*.', '..617..'], 1, 2, '617')

    def test_detect_string_over_a_symbol(self):
        assert is_adjacent(['..617..', '.*.....'], 0, 2, '617')
        assert is_adjacent(['..617..', '..*....'], 0, 2, '617')
        assert is_adjacent(['..617..', '...*...'], 0, 2, '617')
        assert is_adjacent(['..617..', '....*..'], 0, 2, '617')
        assert is_adjacent(['..617..', '.....*.'], 0, 2, '617')

    def test_detect_string_only_directly_over_a_symbol(self):
        assert not is_adjacent(['..617..', '.......', '.*.....'], 0, 2, '617')

    def test_detect_string_only_directly_under_a_symbol(self):
        assert not is_adjacent(['..*....', '.......','..617..'], 0, 2, '617')

