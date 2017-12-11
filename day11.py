# https://www.redblobgames.com/grids/hexagons/#distances

from functools import reduce

DIR = {
    'ne': ( 1,  0, -1),
    'se': ( 1, -1,  0),
    's' : ( 0, -1,  1),
    'sw': (-1,  0,  1),
    'nw': (-1,  1,  0),
    'n' : ( 0,  1, -1)
}

def move(c, d):
    return (c[0] + DIR[d][0], c[1] + DIR[d][1], c[2] + DIR[d][2])

def travel(c, steps):
    yield c
    for step in steps.split(','):
        c = move(c, step)
        yield c

def dist(a, b):
    return (abs(a[0]-b[0]) + abs(a[1]+b[1]) + abs(a[2]+b[2])) // 2

def last_distance(steps):
    return reduce(lambda _, d: d, (dist((0, 0, 0), c) for c in travel((0, 0, 0), steps)))

def max_distance(steps):
    return reduce(max, (dist((0, 0, 0), c) for c in travel((0, 0, 0), steps)))
    
def test_11a_ex1(): assert last_distance('ne,ne,ne') == 3
def test_11a_ex2(): assert last_distance('ne,ne,sw,sw') == 0
def test_11a_ex3(): assert last_distance('ne,ne,s,s') == 2
def test_11a_ex4(): assert last_distance('se,sw,se,sw,sw') == 3

def test_11b_ex1(): assert max_distance('ne,ne,ne') == 3
def test_11b_ex2(): assert max_distance('ne,ne,sw,sw') == 2
def test_11b_ex3(): assert max_distance('ne,ne,s,s') == 2
def test_11b_ex4(): assert max_distance('se,sw,se,sw,sw') == 3

def test_11a_answer(day11): assert last_distance(day11) == 707
def test_11b_answer(day11): assert max_distance(day11) == 1490

