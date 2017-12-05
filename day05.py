def jump(N, b):
    i = 0
    c = 0
    while 0 <= i < len(N):
        v = N[i]
        N[i] += b if v >= 3 else 1
        i += v
        c += 1
    return c

def test_5a_example(): assert jump([0, 3, 0, 1, -3], +1) == 5
def test_5b_example(): assert jump([0, 3, 0, 1, -3], -1) == 10

def test_5a_answer(day05_numbers): assert jump(day05_numbers, +1) == 318883
def test_5b_answer(day05_numbers): assert jump(day05_numbers, -1) == 23948711
