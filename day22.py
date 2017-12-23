from collections import defaultdict

def parse(lines):
    cell = [['.#'.index(ch) for ch in line] for line in lines]
    grid = {x+1j*y: v
            for (y, row) in enumerate(cell)
            for (x, v) in enumerate(row)
            if v == 1}
    w,h = len(cell[0]), len(cell)
    p = (w//2) + (h//2) * 1j
    d = -1j
    return defaultdict(int, grid), p, d

# 0=clean 1=infected 2=weakened 3=flagged
def infect(grid, p, d, N, states):
    turns = { 0: lambda d:  d * -1j,
              1: lambda d:  d *  1j,
              2: lambda d:  d,
              3: lambda d: -d }
    for _ in range(N):
        d = turns[grid[p]](d)
        grid[p] = states[grid[p]]
        yield (p, grid[p])
        p += d

def one(grid, p, d, N):
    return sum(v==1 for (_, v) in infect(grid, p, d, N, {0: 1, 1: 0}))

def two(grid, p, d, N):
    return sum(v==1 for (_, v) in infect(grid, p, d, N, {0:2, 2:1, 1:3, 3:0}))

def test_22a_ex1(): assert one(*parse(['..#', '#..', '...']),     7) == 5
def test_22a_ex2(): assert one(*parse(['..#', '#..', '...']),    70) == 41
def test_22a_ex3(): assert one(*parse(['..#', '#..', '...']), 10000) == 5587

def test_22b_ex1(): assert two(*parse(['..#', '#..', '...']),      100) == 26
def test_22b_ex2(): assert two(*parse(['..#', '#..', '...']), 10000000) == 2511944

def test_22a_answer(day22_lines): assert one(*parse(day22_lines),    10000) == 5399
def test_22b_answer(day22_lines): assert two(*parse(day22_lines), 10000000) == 2511776
