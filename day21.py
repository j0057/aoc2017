from math import sqrt
from itertools import chain

def tuplify(grid):
    return tuple(tuple(row) for row in grid)

def rotate(M):
    return [[M[y][x] for y in range(len(M)-1,-1,-1)] for x in range(len(M))]

def flip_v(M):
    return [[*reversed(row)] for row in M]

def flip_h(M):
    return [*reversed(M)]

def transpose(M):
    M = rotate(M) ; yield M ; yield flip_v(M) ; yield flip_h(M)
    M = rotate(M) ; yield M ; yield flip_v(M) ; yield flip_h(M)
    M = rotate(M) ; yield M ; yield flip_v(M) ; yield flip_h(M)
    M = rotate(M) ; yield M ; yield flip_v(M) ; yield flip_h(M)

def unpack(s):
    return [[1 if ch == '#' else 0 for ch in line] for line in s.split('/')]

def parse(patterns):
    for line in patterns:
        in_pattern, out_pattern = line.split(' => ')
        in_patterns = {tuplify(pattern) for pattern in transpose(unpack(in_pattern))}
        yield from ((pattern, unpack(out_pattern)) for pattern in in_patterns)

def get_pieces(grid, n):
    yield from [[row[x:x+n] for row in grid[y:y+n]]
                for y in range(0, len(grid), n)
                for x in range(0, len(grid), n)]

def put_pieces(pieces):
    R = int(sqrt(len(pieces)))
    s = len(pieces[0])
    return [[*chain(*[pieces[j][y] for j in range(i, i+R)])]
            for i in range(0, len(pieces), R)
            for y in range(s)]

def expand(grid, patterns, iterations):
    patterns = dict(patterns)
    for _ in range(iterations):
        step = 2 if not len(grid)%2 else 3 if not len(grid)%3 else 0/0
        pieces = [tuplify(piece) for piece in get_pieces(grid, step)]
        grid = put_pieces([patterns[piece] for piece in pieces])
    return grid, sum(sum(row) for row in grid)

EX20 = ['../.# => ##./#../...',
        '.#./..#/### => #..#/..../..../#..#']

def test_21a_rotate_2(): assert rotate([[1,2],[3,4]])             == [[3,1],[4,2]]
def test_21a_rotate_3(): assert rotate([[1,2,3],[4,5,6],[7,8,9]]) == [[7,4,1],[8,5,2],[9,6,3]]

def test_21a_flip_v(): assert flip_v([[1,2],[3,4]]) == [[2,1],[4,3]]
def test_21a_flip_h(): assert flip_h([[1,2],[3,4]]) == [[3,4],[1,2]]

def test_21a_ex1a(): assert expand(unpack('.#./..#/###'), parse(EX20), 1)[0] == unpack('#..#/..../..../#..#')
def test_21a_ex2a(): assert expand(unpack('.#./..#/###'), parse(EX20), 2)[0] == unpack('##.##./#..#../....../##.##./#..#../......')
def test_21a_ex2b(): assert expand(unpack('.#./..#/###'), parse(EX20), 2)[1] == 12

def test_21a_answer(day21_lines): assert expand(unpack('.#./..#/###'), parse(day21_lines),  5)[1] == 123
def test_21b_answer(day21_lines): assert expand(unpack('.#./..#/###'), parse(day21_lines), 18)[1] == 1984683
