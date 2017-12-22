from collections import defaultdict

def parse(lines):
    grid = [['.#'.index(ch) for ch in line] for line in lines]
    return defaultdict(int, {(y,x): v
                             for (y, row) in enumerate(grid)
                             for (x, v) in enumerate(row)
                             if grid[y][x] == 1 }), len(grid), len(grid[0])

# 0=clean 1=infected 2=weakened 3=flagged
def iterate(grid, h, w, N, states):
    turns = { 0: lambda dy,dx: d[(d.index((dy,dx))-1)%len(d)],
              1: lambda dy,dx: d[(d.index((dy,dx))+1)%len(d)],
              2: lambda dy,dx: (dy,dx),
              3: lambda dy,dx: (-dy,-dx) }
    y,x = h//2, w//2
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dy,dx = d[0]
    c = 0
    for _ in range(N):
        dy,dx = turns[grid[y,x]](dy,dx)
        if states[grid[y,x]] == 1:
            c += 1
        grid[y,x] = states[grid[y,x]]
        y,x = y+dy, x+dx
    return c

def one(grid, h, w, N):
    return iterate(grid, h, w, N, {0: 1, 1: 0})

def two(grid, h, w, N):
    return iterate(grid, h, w, N, {0: 2, 2: 1, 1: 3, 3: 0})

def test_22a_ex1(): assert one(*parse(['..#', '#..', '...']),     7) == 5
def test_22a_ex2(): assert one(*parse(['..#', '#..', '...']),    70) == 41
def test_22a_ex3(): assert one(*parse(['..#', '#..', '...']), 10000) == 5587

def test_22b_ex1(): assert two(*parse(['..#', '#..', '...']),      100) == 26
def test_22b_ex2(): assert two(*parse(['..#', '#..', '...']), 10000000) == 2511944

def test_22a_answer(day22_lines): assert one(*parse(day22_lines),    10000) == 5399
def test_22b_answer(day22_lines): assert two(*parse(day22_lines), 10000000) == 2511776
