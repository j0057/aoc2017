from collections import defaultdict

def execute(reg, code):
    get = lambda reg, x: reg[x] if x.isalpha() else int(x)
    while 0 <= reg['ip'] < len(code):
        op, *a = code[reg['ip']]
        if   op == 'set':   reg[a[0]] =  get(reg, a[1])
        elif op == 'add':   reg[a[0]] += get(reg, a[1])
        elif op == 'sub':   reg[a[0]] -= get(reg, a[1])
        elif op == 'mul':   reg[a[0]] *= get(reg, a[1])
        elif op == 'mod':   reg[a[0]] %= get(reg, a[1])
        elif op == 'jgz':   reg['ip'] += get(reg, a[1])-1 if get(reg, a[0]) > 0 else 0
        elif op == 'jnz':   reg['ip'] += get(reg, a[1])-1 if get(reg, a[0]) != 0 else 0
        elif op == 'snd':
                reg['SEND'].append(get(reg, a[0]))
                reg['C'] += 1
        elif op == 'rcv' and reg['V'] == 1:
            if get(reg, a[0]):
                reg[a[0]] = reg['LAST'] = reg['RECV'].pop(-1)
                break
        elif op == 'rcv' and reg['V'] == 2:
            if reg['RECV']:
                reg['WAIT'] = 0
                reg[a[0]] = reg['RECV'].pop(0)
            else:
                reg['WAIT'] = 1
                return
        else:
            raise ValueError(code[reg['ip']])
        reg['ip'] += 1
        reg['COUNT'][op] = reg['COUNT'].get(op, 0) + 1

def one(program):
    code = [line.split() for line in program]
    queue = []
    reg = defaultdict(lambda: 0, COUNT={}, SEND=queue, RECV=queue, V=1)
    execute(reg, code)
    return reg['LAST']

def two(program):
    code = [line.split() for line in program]
    q0, q1 = [[], []]
    reg = [defaultdict(lambda: 0, COUNT={}, SEND=q0, RECV=q1, p=0, P=0, V=2),
           defaultdict(lambda: 0, COUNT={}, SEND=q1, RECV=q0, p=1, P=1, V=2)]
    p = 1
    while True:
        p = 1-p
        execute(reg[p], code)
        if reg[p]['WAIT'] and reg[1-p]['WAIT'] and not reg[1-p]['RECV']:
            break
        if not (0 <= reg[0]['ip'] < len(code)) and not (0 <= reg[1]['ip'] < len(code)):
            break
    return reg[1]['COUNT'].get('snd', 0)

def test_18a_ex(): assert one('set a 1|add a 2|mul a a|mod a 5|snd a|set a 0|rcv a|jgz a -1|set a 1|jgz a -2'.split('|')) == 4
def test_18b_ex(): assert two('snd 1|snd 2|snd p|rcv a|rcv b|rcv c|rcv d'.split('|')) == 3

def test_18a_answer(day18_lines): assert one(day18_lines) == 8600
def test_18b_answer(day18_lines): assert two(day18_lines) == 7239
