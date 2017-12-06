def process(bank):
    seen = []
    while tuple(bank) not in seen:
        seen.append(tuple(bank))
        i, v = max(enumerate(bank), key=lambda t: t[1])
        bank[i] = 0
        for x in range(v):
            bank[(i+x+1) % len(bank)] += 1
    return (len(seen), len(seen)-seen.index(tuple(bank)))

def test_6a_ex1(): assert process([0, 2, 7, 0])[0] == 5
def test_6b_ex1(): assert process([0, 2, 7, 0])[1] == 4

def test_6a_answer(day06_number_grid): assert process(day06_number_grid[0])[0] == 14029
def test_6b_answer(day06_number_grid): assert process(day06_number_grid[0])[1] == 2765
