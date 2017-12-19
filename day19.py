
def find_start(maze):
    w, h = len(maze[0]), len(maze)
    for x, ch in enumerate(maze[0]):
        if ch == '|':
            return (0, x)
    for x, ch in enumerate(maze[-1]):
        if ch == '|':
            return (h-1, x)
    for y, line in enumerate(maze):
        if line[0] == '-':
            return (y, 0)
        if line[-1] == '-':
            return (y, w-1)

def walk(maze, y, x):
    w, h = len(maze[0]), len(maze)
    if   y == 0:   dy, dx = +1,  0
    elif x == 0:   dy, dx =  0, +1
    elif y == h-1: dy, dx = -1,  0
    elif x == w-1: dy, dx =  0, -1

    yield (y, x, None)

    while True:
        y += dy
        x += dx

        yield (y, x, maze[y][x] if maze[y][x].isalpha() else None)

        if maze[y][x] == '+':
            if dx == 0:
                if x > 0   and maze[y][x-1] != ' ': dy, dx = 0, -1
                if x < w-1 and maze[y][x+1] != ' ': dy, dx = 0, +1

            elif dy == 0:
                if y > 0   and maze[y-1][x] != ' ': dy, dx = -1, 0
                if y < h-1 and maze[y+1][x] != ' ': dy, dx = +1, 0

        if not (0 <= x < w) or not (0 <= y < h) or (maze[y][x] == ' '):
            break

def one(maze):
    y,x = find_start(maze)
    return ''.join(p for (_, _, p) in walk(maze, y, x) if p)

def two(maze):
    y,x = find_start(maze)
    return sum(1 for _ in walk(maze, y, x))-1

EX = [
    '     |          ',
    '     |  +--+    ',
    '     A  |  C    ',
    ' F---|----E|--+ ',
    '     |  |  |  D ',
    '     +B-+  +--+ '
]

def test_19a_ex0(): assert find_start(EX) == (0,5)

def test_19a_ex(): assert one(EX) == 'ABCDEF'
def test_19b_ex(): assert two(EX) == 38

def test_19a_answer(day19_raw): assert one(day19_raw.split('\n')) == 'HATBMQJYZ'
def test_19b_answer(day19_raw): assert two(day19_raw.split('\n')) == 16332
