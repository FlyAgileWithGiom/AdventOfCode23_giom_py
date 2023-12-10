from unittest import skip
from logic import to_xy_map, scan_part_numbers, has_symbol, is_adjacent, detect_parts_in_line, sum_part_numbers, is_symbol

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


class TestDay3:

	def test_can_turn_input_into_lines(self):
		assert len(to_xy_map(SCHEMATIC_EXAMPLE)) == 10
		assert len(to_xy_map(SCHEMATIC_EXAMPLE)[0]) == 10

	def test_is_symbol_detects_star_dollar_hashtag_plus(self):
		assert has_symbol('617*..', 3, 1)
		assert has_symbol('617$..', 3, 1)
		assert has_symbol('617#..', 3, 1)
		assert has_symbol('617+..', 3, 1)
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

	def test_detect_string_border_right(self):
		assert not is_adjacent(['*..617'], 0, 3, '617')

	def test_detect_string_under_a_symbol(self):
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
		assert not is_adjacent(['..*....', '.......', '..617..'], 0, 2, '617')

	def test_detect_string_over_right_diagonal_symbol(self):
		assert is_adjacent(['617..', '...*.'], 0, 0, '617')

	def test_can_scan_numbers_on_a_line(self):
		assert list(m.group(0)
		            for m in scan_part_numbers("467..114..")) == ['467', '114']

	def test_detect_adjacent_or_not_on_first_line(self):
		assert is_adjacent(SCHEMATIC_AS_TABLE, 0, 0, '467')
		assert not is_adjacent(SCHEMATIC_AS_TABLE, 0, 5, '114')

	def test_detect_all_parts_on_line(self):
		assert detect_parts_in_line(SCHEMATIC_AS_TABLE, 0) == [467]
		assert [
		 detect_parts_in_line(SCHEMATIC_AS_TABLE, i)
		 for i in range(0, len(SCHEMATIC_AS_TABLE))
		] == [[467], [], [35, 633], [], [617], [], [592], [755], [], [664, 598]]

	def test_sum_all_part_numbers(self):
		assert sum_part_numbers(SCHEMATIC_EXAMPLE) == 4361

	def test_detect_all_input_symbols(self):
		for s in r'!@&*$%*/+=#-':
			assert is_symbol(str(s), 0), f'{s} is detected as symbol'

