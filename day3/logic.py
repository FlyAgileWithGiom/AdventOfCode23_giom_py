import re

def to_xy_map(input):
    return input.splitlines()


def scan_part_numbers(y):
    return re.finditer(r'(\d+)', y)


def is_adjacent(table, y, x, str):
    if is_before_a_symbol(x, y, str, table):
        return True
    if is_after_a_symbol(x, y, table):
        return True
    if is_under_a_symbol(x, y, str, table):
        return True
    if is_over_a_symbol(x, y, str, table):
        return True
    return False


def is_under_a_symbol(x, y, str, table):
    if y <= 0:
        return False
    return has_symbol(table[y - 1], x - 1, len(str) + 2)


def is_last_y_or_beyond(table, y):
    last_y = len(table) - 1
    return y >= last_y


def is_over_a_symbol(x, y, str, table):
    if is_last_y_or_beyond(table, y):
        return False

    return has_symbol(table[y + 1], x - 1, len(str) + 2)


def is_after_a_symbol(x, y, table):
    return is_symbol(table[y], x - 1)


def is_before_a_symbol(x, y, str, table):
    return is_symbol(table[y], x + len(str))


SYMBOL_MATCHER = re.compile(r'[*$#]')


def has_symbol(line, start, length):
    start = max(start, 0) #dont search before left of line 
    end = min(len(line),start+length) -1 #dont search after end of line

    return SYMBOL_MATCHER.search(line[start:end]) is not None


def is_symbol(line, x):
    return has_symbol(line, x, 1)


def detect_parts(table, y):
    parts = []
    for m in scan_part_numbers(table[y]):
        x = m.start()
        str = m.group(0)
        if is_adjacent(table, y, x, str):
            parts.append(str)
    return parts


def sum_part_numbers(schematic):
    return sum(sum([detect_parts(l) for l in to_xy_map(schematic)]))
