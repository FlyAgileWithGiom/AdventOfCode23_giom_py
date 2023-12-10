import re
from functools import reduce


def to_xy_map(input):
	return input.splitlines()


def scan_part_numbers(y):
	return re.finditer(r'(\d+)', y)


def is_adjacent(table: [str], y: int, x: int, str: str):
	if is_before_a_symbol(x, y, str, table):
		return True
	if is_after_a_symbol(x, y, table):
		return True
	if is_under_a_symbol(x, y, str, table):
		return True
	if is_over_a_symbol(x, y, str, table):
		return True
	return False


def is_first_line_or_upper(table, y):
	return y <= 0


def is_under_a_symbol(x, y, str, table):
	if is_first_line_or_upper(table, y):
		return False
	return has_symbol(table[y - 1], x - 1, len(str) + 2)


def is_last_line_or_beyond(table, y):
	last_y = len(table) - 1
	return y >= last_y


def is_over_a_symbol(x, y, str, table):
	if is_last_line_or_beyond(table, y):
		return False

	return has_symbol(table[y + 1], x - 1, len(str) + 2)


def is_after_a_symbol(x, y, table):
	return is_symbol(table[y], x - 1)


def is_before_a_symbol(x, y, str, table):
	return is_symbol(table[y], x + len(str))


SYMBOL_MATCHER = re.compile(r'[^\d.]')


def has_symbol(line, start, length):
	start = max(start, 0)  #dont search before left of line
	end = min(len(line), start + length)  #dont search after end of line

	return SYMBOL_MATCHER.search(line[start:end]) is not None


def is_symbol(line, x):
	return has_symbol(line, x, 1)


def detect_parts_in_line(table, y):
	parts = []
	for m in scan_part_numbers(table[y]):
		x = m.start()
		str = m.group(0)
		if is_adjacent(table, y, x, str):
			parts.append(int(str))
	return parts


def sum_part_numbers(schematic):
	schematic_table = to_xy_map(schematic)
	return sum(
	 reduce(lambda x, y: x + y, [
	  detect_parts_in_line(schematic_table, y)
	  for y in range(0, len(schematic_table))
	 ]))

