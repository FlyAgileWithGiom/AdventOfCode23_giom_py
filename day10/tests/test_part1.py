def detect_pipe(map, pos, direction):
    if direction == 'north':
        if pos[0] <= 0:
            return None
        good_pipes = {'7':'north-west','|':'north-north', 'F':'north-east'}
        try:
            return good_pipes[map[pos[0]-1][pos[1]]]
        except KeyError:
            return None
    elif direction == 'west':
        if pos[1] <= 0:
            return None
        good_pipes = {'L': 'west-north', '-': 'west-west', 'F': 'west-south'}
        try:
            return good_pipes[map[pos[0]][pos[1]-1]]
        except KeyError:
            return None
    elif direction == 'south':
        if pos[0] > len(map) -2:
            return None
        good_pipes = {'J': 'south-west', '|':'south-south', 'L': 'south-east'}
        try:
            return good_pipes[map[pos[0]+1][pos[1]]]
        except KeyError:
            return None
    elif direction == 'east':
        if pos[1] > len(map[pos[0]]) -2 :
            return None
        good_pipes = {'J': 'east-north', '-': 'east-east', '7': 'east-south'}
        try:
            return good_pipes[map[pos[0]][pos[1]+1]]
        except KeyError:
            return None


class TestPart1:
    def test_detect_connected_pipe_north(self):
        map = ['.7.', 'SSS', '...']
        assert detect_pipe(map, (1, 1), 'north') == 'north-west'
        map = ['.|.', 'SSS', '...']
        assert detect_pipe(map, (1, 1), 'north') == 'north-north'
        map = ['.F.', 'SSS', '...']
        assert detect_pipe(map, (1, 1), 'north') == 'north-east'

    def test_no_north_pipe_for_first_line(self):
        map = [
            'SSS', '...'
        ] # S represented for clarity
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
        assert detect_pipe(map, (1, 1), 'west') == 'west-west'
        map = ['...', 'LS.', '...']
        assert detect_pipe(map, (1, 1), 'west') == 'west-north'
        map = ['...', 'FS.', '...']
        assert detect_pipe(map, (1, 1), 'west') == 'west-south'

    def test_detect_connected_south_pipe(self):
        map = ['...', '.S.', '.J.']
        assert detect_pipe(map, (1,1), 'south') == 'south-west'
        map = ['...', '.S.', '.|.']
        assert detect_pipe(map, (1,1), 'south') == 'south-south'
        map = ['...', '.S.', '.L.']
        assert detect_pipe(map, (1,1), 'south') == 'south-east'

    def test_no_south_pipe_for_last_line(self):
        map = [
            '...', '...', 'SSS'
        ]
        assert detect_pipe(map, (2, 0), 'south') == None
        assert detect_pipe(map, (2, 1), 'south') == None
        assert detect_pipe(map, (2, 2), 'south') == None

    def test_detect_connected_east_pipe(self):
        map = ['...', '.SJ', '...']
        assert detect_pipe(map, (1,1), 'east') == 'east-north'
        map = ['...', '.S-', '...']
        assert detect_pipe(map, (1,1), 'east') == 'east-east'
        map = ['...', '.S7', '...']
        assert detect_pipe(map, (1,1), 'east') == 'east-south'

    def test_no_east_pipe_for_last_column(self):
        map = [
            '..S', '..S', '..S'
        ]
        assert detect_pipe(map, (0, 2), 'east') == None
        assert detect_pipe(map, (1, 2), 'east') == None
        assert detect_pipe(map, (2, 2), 'east') == None
