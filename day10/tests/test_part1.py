from unittest import skip

EXAMPLE_MAP = '''..F7.
.FJ|.
SJ.L7
|F--J
LJ...'''
EXAMPLE_MAP_TABLE = EXAMPLE_MAP.splitlines()
NORTH_WEST = [[-1,0],[0, -1]]
NORTH_NORTH = [[-1, 0],[-1,0]]
NORTH_EAST = [[-1,0],[0, 1]]
WEST_NORTH = [[0,-1],[-1,0]]
WEST_WEST = [[0,-1],[0,-1]]
WEST_SOUTH = [[0,-1],[1,0]]
SOUTH_EAST = [[1,0],[0,-1]]
SOUTH_SOUTH = [[1,0],[1,0]]
SOUTH_WEST = [[1,0],[0,1]]
EAST_NORTH = [[0,1],[-1,0]]
EAST_EAST = [[0,1],[0,1]]
EAST_SOUTH = [[0,1],[1,0]]


def detect_pipe(map, pos, direction):
    if direction == 'north':
        if pos[0] <= 0:
            return None
        good_pipes = {'7': NORTH_WEST, '|': NORTH_NORTH, 'F': NORTH_EAST}
        try:
            return good_pipes[map[pos[0] - 1][pos[1]]]
        except KeyError:
            return None
    elif direction == 'west':
        if pos[1] <= 0:
            return None
        good_pipes = {'L': WEST_NORTH, '-': WEST_WEST, 'F': WEST_SOUTH}
        try:
            return good_pipes[map[pos[0]][pos[1] - 1]]
        except KeyError:
            return None
    elif direction == 'south':
        if pos[0] > len(map) - 2:
            return None
        good_pipes = {'J': SOUTH_WEST, '|': SOUTH_SOUTH, 'L': SOUTH_EAST}
        try:
            return good_pipes[map[pos[0] + 1][pos[1]]]
        except KeyError:
            return None
    elif direction == 'east':
        if pos[1] > len(map[pos[0]]) - 2:
            return None
        good_pipes = {'J': EAST_NORTH, '-': EAST_EAST, '7': EAST_SOUTH}
        try:
            return good_pipes[map[pos[0]][pos[1] + 1]]
        except KeyError:
            return None


def update_path(path, connected_pipe):
    pos = path[-1]
    for step in connected_pipe:
        pos = [pos[0] + step[0], pos[1] + step[1]]
        path.append(pos)
    return path


def detect_start_point(map:[str]):
    for y in range(0, len(map)):
        x = map[y].find('S')
        if x != -1:
            return [y, x]


def track_loop(map):
    path = [detect_start_point(map)]
    path = follow_loop(map, path)
    return path


def follow_loop(map, path, last_direction = None):
    connected_pipe = detect_connected_pipe(map, path, last_direction)

    path = update_path(path, connected_pipe)
    return path

def reverse_direction(direction):
    reverse = {'south':'north','west':'east','east':'west','north':'south', None:None}
    return reverse[direction]

def detect_connected_pipe(map, path, last_direction):
    connected_pipe = None

    possible_directions = ['north', 'west', 'south', 'east']

    for direction in possible_directions:
        if direction != reverse_direction(last_direction):
            connected_pipe = detect_pipe(map, path[-1], direction)
            if connected_pipe is not None:
                break
    return connected_pipe


class TestPart1:
    def test_detect_connected_pipe_north(self):
        map = ['.7.', 'SSS', '...']
        assert detect_pipe(map, (1, 1), 'north') == NORTH_WEST
        map = ['.|.', 'SSS', '...']
        assert detect_pipe(map, (1, 1), 'north') == NORTH_NORTH
        map = ['.F.', 'SSS', '...']
        assert detect_pipe(map, (1, 1), 'north') == NORTH_EAST

    def test_no_north_pipe_for_first_line(self):
        map = [
            'SSS', '...'
        ]  # S represented for clarity
        assert detect_pipe(map, (0, 0), 'north') == None
        assert detect_pipe(map, (0, 1), 'north') == None
        assert detect_pipe(map, (0, 2), 'north') == None

    def test_no_west_pipe_for_first_column(self):
        map = [
            'S..', 'S..', 'S..'
        ]
        assert detect_pipe(map, (0, 0), 'west') == None
        assert detect_pipe(map, (1, 0), 'west') == None
        assert detect_pipe(map, (2, 0), 'west') == None

    def test_detect_connected_west_pipe(self):
        map = ['...', '-S.', '...']
        assert detect_pipe(map, (1, 1), 'west') == WEST_WEST
        map = ['...', 'LS.', '...']
        assert detect_pipe(map, (1, 1), 'west') == WEST_NORTH
        map = ['...', 'FS.', '...']
        assert detect_pipe(map, (1, 1), 'west') == WEST_SOUTH

    def test_detect_connected_south_pipe(self):
        map = ['...', '.S.', '.J.']
        assert detect_pipe(map, (1, 1), 'south') == SOUTH_WEST
        map = ['...', '.S.', '.|.']
        assert detect_pipe(map, (1, 1), 'south') == SOUTH_SOUTH
        map = ['...', '.S.', '.L.']
        assert detect_pipe(map, (1, 1), 'south') == SOUTH_EAST

    def test_no_south_pipe_for_last_line(self):
        map = [
            '...', '...', 'SSS'
        ]
        assert detect_pipe(map, (2, 0), 'south') == None
        assert detect_pipe(map, (2, 1), 'south') == None
        assert detect_pipe(map, (2, 2), 'south') == None

    def test_detect_connected_east_pipe(self):
        map = ['...', '.SJ', '...']
        assert detect_pipe(map, (1, 1), 'east') == EAST_NORTH
        map = ['...', '.S-', '...']
        assert detect_pipe(map, (1, 1), 'east') == EAST_EAST
        map = ['...', '.S7', '...']
        assert detect_pipe(map, (1, 1), 'east') == EAST_SOUTH

    def test_no_east_pipe_for_last_column(self):
        map = [
            '..S', '..S', '..S'
        ]
        assert detect_pipe(map, (0, 2), 'east') == None
        assert detect_pipe(map, (1, 2), 'east') == None
        assert detect_pipe(map, (2, 2), 'east') == None

    def test_update_path_extends_path(self):
        path = update_path([[1, 1]], NORTH_NORTH)
        assert len(path) == 3

    def test_update_path_connected_north_updates_position(self):
        path = update_path([[1, 1]], NORTH_WEST)
        assert path == [[1,1],[0,1],[0,0]]
        path = update_path([[1, 1]], NORTH_NORTH)
        assert path[-1] == [-1, 1]
        path = update_path([[1, 1]], NORTH_EAST)
        assert path[-1] == [0, 2]

    def test_update_path_connected_west_updates_position(self):
        path = update_path([[1, 1]], WEST_NORTH)
        assert path[-1] == [0,0]
        path = update_path([[1, 1]], WEST_WEST)
        assert path[-1] == [1,-1]
        path = update_path([[1, 1]], WEST_SOUTH)
        assert path[-1] == [2,0]

    def test_update_path_connected_east_updates_position(self):
        path = update_path([[1, 1]], EAST_NORTH)
        assert path[-1] == [0,2]
        path = update_path([[1, 1]], EAST_EAST)
        assert path[-1] == [1,3]
        path = update_path([[1, 1]], EAST_SOUTH)
        assert path[-1] == [2,2]

    def test_detect_start_point(self):
        map = ['...', '.SJ', '...']
        assert detect_start_point(map) == [1,1]
        map = ['...', '...', '..S']
        assert detect_start_point(map) == [2, 2]


    def test_track_loop_start_at_animal_postion(self):
        assert track_loop(EXAMPLE_MAP_TABLE)[0] == [2, 0]

    def test_follow_loop_tolerates_no_starting_direction(self):
        assert follow_loop(EXAMPLE_MAP_TABLE, [[2, 0]])[1] in ([3, 0],[2,1])

    def test_follow_loop_follow_first_connected_pipe_south(self):
        assert follow_loop(EXAMPLE_MAP_TABLE,[[2,0]],'west')[1] == [3, 0]
        assert follow_loop(EXAMPLE_MAP_TABLE,[[2,0]],'west')[2] == [4, 0]

    def test_follow_loop_follow_first_connected_pipe_east(self):
        assert follow_loop(EXAMPLE_MAP_TABLE, [[4, 0]], 'south')[1] == [4, 1]
        assert follow_loop(EXAMPLE_MAP_TABLE, [[4, 0]], 'south')[2] == [3, 1]

    def test_follow_loop_follow_first_connected_pipe_north(self):
        assert follow_loop(EXAMPLE_MAP_TABLE, [[4, 1]], 'east')[1] == [3, 1]

    def test_follow_loop_follow_first_connected_pipe_west(self):
        assert follow_loop(EXAMPLE_MAP_TABLE, [[2, 4]], 'west')[2] == [1, 3]

    def test_follow_loop_keep_following_pipe(self):
        assert track_loop(EXAMPLE_MAP_TABLE)[1] == [3, 0]
