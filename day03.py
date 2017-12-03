from itertools import count, islice

def number_spiral_coords():
    y, x = (0, 0)
    yield (0, 0)
    for L in count(start=1, step=2):
        for _ in range(L):
            x += 1
            yield (y, x)
        for _ in range(L):
            y += 1
            yield (y, x)
        for _ in range(L+1):
            x -= 1
            yield (y, x)
        for _ in range(L+1):
            y -= 1
            yield (y, x)

def number_spiral_coord(n):
    return next(islice(number_spiral_coords(), n-1, n))

def number_spiral_manhattan(n):
    y, x = number_spiral_coord(n)
    return abs(y) + abs(x)

def test_3a_ex1(): assert number_spiral_manhattan(1) == 0
def test_3a_ex2(): assert number_spiral_manhattan(12) == 3
def test_3a_ex3(): assert number_spiral_manhattan(23) == 2
def test_3a_ex4(): assert number_spiral_manhattan(1024) == 31

def test_3a_answer(day03): assert number_spiral_manhattan(int(day03)) == 480
