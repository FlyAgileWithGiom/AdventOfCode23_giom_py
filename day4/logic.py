def parse_line(line):
    parser = re.compile(r'^Card (\d+):((  ?\d?\d)+) \|((  ?\d?\d)+)')
    result = parser.match(line).groups()
    return [int(result[0]), parse_numbers(result[1]), parse_numbers(result[3])]


def parse_numbers(nb_series):
    return [int(s) for s in re.findall(r' ( ?\d?\d)', nb_series)]


def detect_matches(line):
    card_id, winnings, candidates = parse_line(line)
    return len(set(winnings) & set(candidates))


def calculate_score(line):
    match_count = detect_matches(line)
    if match_count == 0:
        return 0
    return 2**(match_count - 1)


def score_pile(stack):
    return sum([calculate_score(line) for line in stack.splitlines()])

