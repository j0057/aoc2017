from string import ascii_lowercase

def dance(size, program, iterations=1):
    state = list(ascii_lowercase[:size])
    seen = []
    for i in range(iterations):
        if ''.join(state) in seen:
            print(i) # 42 < 1000000000 ...
            return seen[iterations % i]
        seen.append(''.join(state))
        for move in program.split(','):
            if move[0] == 's':
                n = int(move[1:])
                state = state[-n:] + state[:-n]
            elif move[0] == 'x':
                a, b = move[1:].split('/')
                a, b = int(a), int(b)
                state[a], state[b] = state[b], state[a]
            elif move[0] == 'p':
                a, b = move[1], move[-1]
                a = state.index(a)
                b = state.index(b)
                state[a], state[b] = state[b], state[a]
            else:
                raise Exception(move)
    return ''.join(state)

def test_16a_ex1(): assert dance(5, 's1,x3/4,pe/b') == 'baedc'

def test_16a_answer(day16): assert dance(16, day16, 1)          == 'kgdchlfniambejop'
def test_16b_answer(day16): assert dance(16, day16, 1000000000) == 'fjpmholcibdgeakn'
