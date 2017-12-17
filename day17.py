def spin_lock(step, count):
    i, L = 0, [0]
    for v in range(1, count+1):
        i = (i + step) % len(L) + 1
        L.insert(i, v)
    return i, L

def spin_lock_1(step):
    i, L = spin_lock(step, 2017)
    return L[(i+1) % len(L)]

def spin_lock_2(step):
    r, i, j = -1, 0, 1
    for v in range(1, 50000001):
        i = (i + step) % j + 1
        if i == 1:
            r = v
        j += 1
    return r

def test_17a_ex1(): assert spin_lock_1(3) == 638

def test_17a_answer(day17_number): assert spin_lock_1(day17_number) == 772
def test_17b_answer(day17_number): assert spin_lock_2(day17_number) == 42729050
