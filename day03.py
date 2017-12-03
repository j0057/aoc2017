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

def number_spiral_sums():
    sums = { (0, 0): 1 }
    for (y, x) in number_spiral_coords():
        sums[y, x] = sum(sums.get((y+dy, x+dx), 0)
                         for dy in [-1, 0, +1]
                         for dx in [-1, 0, +1])
        yield sums[y, x]

def number_spiral_sum(n):
    return next(islice(number_spiral_sums(), n-1, n))

def number_spiral_sum_answer(n):
    return next(v for v in number_spiral_sums() if v > n)

def test_3a_ex1(): assert number_spiral_manhattan(1) == 0
def test_3a_ex2(): assert number_spiral_manhattan(12) == 3
def test_3a_ex3(): assert number_spiral_manhattan(23) == 2
def test_3a_ex4(): assert number_spiral_manhattan(1024) == 31

def test_3b_ex1(): assert number_spiral_sum(1) == 1
def test_3b_ex2(): assert number_spiral_sum(2) == 1
def test_3b_ex3(): assert number_spiral_sum(3) == 2
def test_3b_ex4(): assert number_spiral_sum(4) == 4
def test_3b_ex4(): assert number_spiral_sum(5) == 5

def test_3a_answer(day03_number): assert number_spiral_manhattan(day03_number) == 480
def test_3b_answer(day03_number): assert number_spiral_sum_answer(day03_number) == 349975
