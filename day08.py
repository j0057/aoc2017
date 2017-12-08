import operator

def parse(prog):
    return [ (op[0], op[1], int(op[2]), op[-3], op[-2], int(op[-1])) for op in [ line.split() for line in prog ] ]

def run(code):
    CMP = { '<': operator.lt, '>': operator.gt, '<=': operator.le, '>=': operator.ge, '==': operator.eq, '!=': operator.ne }
    reg = {}
    M = 0
    for (tgt, op, v, condvar, condcmp, condval) in code:
        reg[condvar] = reg.get(condvar, 0)
        if not CMP[condcmp](reg.get(condvar, 0), condval):
            continue
        if op == 'inc':
            reg[tgt] = reg.get(tgt, 0) + v
        elif op == 'dec':
            reg[tgt] = reg.get(tgt, 0) - v
        M = max(M, max(reg.values()))
    return max(reg.values()), M

def test_8_ex():
    assert run(parse([
        'b inc 5 if a > 1',
        'a inc 1 if b < 5',
        'c dec -10 if a >= 1',
        'c inc -20 if c == 10'
    ])) == (1, 10)

def test_8_answer(day08_lines):
    assert run(parse(day08_lines)) == (3880, 5035)
