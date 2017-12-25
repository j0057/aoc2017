from collections import defaultdict

def parse(lines):
    begin = str(lines[0][:-1].split()[-1])
    count = int(lines[1][:-1].split()[-2])
    chunks = lambda s, L: [L[i:i+s] for i in range(0, len(L), s)]
    states = {}
    for chunk in chunks(9, [line[:-1].split()[-1] for line in lines[3:] if line]):
        states[chunk[0], int(chunk[1])] = (int(chunk[2]), -1 if chunk[3]=='left' else +1, chunk[4])
        states[chunk[0], int(chunk[5])] = (int(chunk[6]), -1 if chunk[7]=='left' else +1, chunk[8])
    return begin, count, states

def run(state, count, states):
    tape = defaultdict(int)
    head = 0
    for _ in range(count):
        write, move, cont = states[state, tape[head]]
        tape[head] = write
        head += move
        state = cont
    return sum(tape.values())

def test_25a_parse0(): assert parse(EX)[0] == 'A'
def test_25a_parse1(): assert parse(EX)[1] == 6
def test_25a_parse2(): assert parse(EX)[2]['A', 0] == (1, 1, 'B')

def test_25a_ex1(): assert run(*parse(EX)) == 3

def test_25a_answer(day25_lines): assert run(*parse(day25_lines)) == 4385

def test_25b_answer(): assert 2

EX = [
    'Begin in state A.',
    'Perform a diagnostic checksum after 6 steps.',
    '',
    'In state A:',
    '  If the current value is 0:',
    '    - Write the value 1.',
    '    - Move one slot to the right.',
    '    - Continue with state B.',
    '  If the current value is 1:',
    '    - Write the value 0.',
    '    - Move one slot to the left.',
    '    - Continue with state B.',
    '',
    'In state B:',
    '  If the current value is 0:',
    '    - Write the value 1.',
    '    - Move one slot to the left.',
    '    - Continue with state A.',
    '  If the current value is 1:',
    '    - Write the value 1.',
    '    - Move one slot to the right.',
    '    - Continue with state A.',
]
