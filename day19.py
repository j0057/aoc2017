def parse(maze):
    return ({ complex(x, y): v
              for (y, xs) in enumerate(maze)
              for (x, v) in enumerate(xs) },
            len(maze[0]),
            len(maze))

def find_start(maze, w, h):
    for x in range(w):
        if maze[x+0j] == '|':
            return (x+0j, 1j)
    for x in range(w):
        if maze[x+1j*(h-1)] == '|':
            return (x+1j*(h-1), -1j)
    for y in range(h):
        if maze[y*1j] == '-':
            return (y*1j, +1+0j)
    for y in range(h):
        if maze[w-1 + y*1j] == '-':
            return (w-1+y*1j, -1+0j)

def walk(maze, w, h, p, d):
    yield (p, None)

    while (0 <= p.real < w) and (0 <= p.imag < h) and (maze[p] != ' '):
        p += d

        yield (p, maze[p] if maze[p].isalpha() else None)

        if maze[p] == '+':
            if not d.real:
                if p.real > 0   and maze[p-1] != ' ': d = -1+0j
                if p.real < w-1 and maze[p+1] != ' ': d =  1+0j
            elif not d.imag:
                if p.imag > 0   and maze[p-1j] != ' ': d = -1j
                if p.imag < h-1 and maze[p+1j] != ' ': d =  1j

def one(maze, w, h):
    return ''.join(p for (_, p) in walk(maze, w, h, *find_start(maze, w, h)) if p)

def two(maze, w, h):
    return sum(1 for _ in walk(maze, w, h, *find_start(maze, w, h)))-1

EX = [
    '     |          ',
    '     |  +--+    ',
    '     A  |  C    ',
    ' F---|----E|--+ ',
    '     |  |  |  D ',
    '     +B-+  +--+ '
]

def test_19a_ex0(): assert find_start(*parse(EX)) == (5+0j, 1j)

def test_19a_ex(): assert one(*parse(EX)) == 'ABCDEF'
def test_19b_ex(): assert two(*parse(EX)) == 38

def test_19a_answer(day19_raw): assert one(*parse(day19_raw.split('\n'))) == 'HATBMQJYZ'
def test_19b_answer(day19_raw): assert two(*parse(day19_raw.split('\n'))) == 16332
