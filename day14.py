from day10 import knot_ascii

def knot_grid(data):
    return [int(knot_ascii('{}-{}'.format(data, i)), 16) for i in range(128)]

def knot_grid_popcount(data):
    return sum(bin(h)[2:].count('1') for h in knot_grid(data))

def flood(seen, grid, y, x, i):
    if (y, x) in seen:
        return
    if not grid[y][x]:
        return
    seen.add((y, x))
    if y > 0: flood(seen, grid, y-1, x, i)
    if x > 0: flood(seen, grid, y, x-1, i)
    if y < 127: flood(seen, grid, y+1, x, i)
    if x < 127: flood(seen, grid, y, x+1, i)
        
def knot_grid_regions(data):
    grid = [[1 if b=='1' else 0 for b in '{:0128b}'.format(h)] for h in knot_grid(data)]
    seen = set()
    i = 1
    for y in range(128):
        for x in range(128):
            if (y, x) in seen:
                continue       
            if not grid[y][x]:
                continue
            flood(seen, grid, y, x, i)
            i += 1
    return i-1

def test_14a_ex(): assert knot_grid_popcount('flqrgnkx') == 8108
def test_14b_ex(): assert knot_grid_regions('flqrgnkx') == 1242

def test_14a_answer(day14): assert knot_grid_popcount(day14) == 8216
def test_14b_answer(day14): assert knot_grid_regions(day14) == 1139
