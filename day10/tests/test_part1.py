NORTH_WEST = [-1, -1]
NORTH_NORTH = [-1, 0]
NORTH_EAST = [-1, 1]
WEST_NORTH = [-1,-1]
WEST_WEST = [0,-1]
WEST_SOUTH = [1,-1]
SOUTH_EAST = [1,-1]
SOUTH_SOUTH = [1,0]
SOUTH_WEST = [1,1]
EAST_NORTH = [-1,1]
EAST_EAST = [0,1]
EAST_SOUTH = [1,1]


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
    new_pos = [pos[0] + connected_pipe[0], pos[1] + connected_pipe[1]]
    path.append(new_pos)
    return path


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
        assert len(path) == 2

    def test_update_path_connected_north_updates_position(self):
        path = update_path([[1, 1]], NORTH_WEST)
        assert path == [[1,1],[0,0]]
        path = update_path([[1, 1]], NORTH_NORTH)
        assert path[-1] == [0, 1]
        path = update_path([[1, 1]], NORTH_EAST)
        assert path[-1] == [0, 2]

    def test_update_path_connected_west_updates_position(self):
        path = update_path([[1, 1]], WEST_NORTH)
        assert path[-1] == [0,0]
        path = update_path([[1, 1]], WEST_WEST)
        assert path[-1] == [1,0]
        path = update_path([[1, 1]], WEST_SOUTH)
        assert path[-1] == [2,0]

    def test_update_path_connected_east_updates_position(self):
        path = update_path([[1, 1]], EAST_NORTH)
        assert path[-1] == [0,2]
        path = update_path([[1, 1]], EAST_EAST)
        assert path[-1] == [1,2]
        path = update_path([[1, 1]], EAST_SOUTH)
        assert path[-1] == [2,2]
