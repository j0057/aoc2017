from collections import defaultdict
import re

def parse(lines):
    begin = re.match_groups(r'Begin in state (\w+)', lines[0])
    begin = begin[0]

    count = re.match_groups(r'^Perform a diagnostic checksum after (\d+) steps\.$', lines[1])
    count = int(count[0])

    states = {}
    i = 3
    for i in range(3, len(lines), 10):
        state = re.match_groups(r'In state (\w+):', lines[i+0])

        write0 = re.match_groups(r'^ *- Write the value (\d+)', lines[i+2])
        move0 = re.match_groups(r'^ *- Move one slot to the (left|right)', lines[i+3])
        cont0 = re.match_groups(r'^ *- Continue with state (\w+)\.', lines[i+4])

        write1 = re.match_groups(r'^ *- Write the value (\d+)', lines[i+6])
        move1 = re.match_groups(r'^ *- Move one slot to the (left|right)', lines[i+7])
        cont1 = re.match_groups(r'^ *- Continue with state (\w+)\.', lines[i+8])

        states[state[0], 0] = (int(write0[0]), -1 if move0[0] == 'left' else +1, cont0[0])
        states[state[0], 1] = (int(write1[0]), -1 if move1[0] == 'left' else +1, cont1[0])

    return begin, count, states

def run(state, count, states):
    tape = defaultdict(int)
    i = 0
    for _ in range(count):
        write, move, cont = states[state, tape[i]]
        tape[i] = write
        i += move
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
