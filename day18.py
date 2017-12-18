from collections import defaultdict

def parse(program):
    parser = { name.replace('op_', ''): func for (name, func) in globals().items() if name.startswith('op_') }
    for instruction in program:
        i = instruction.split()
        yield (parser[i[0]], tuple(int(v) if v.isdigit() or (v[0] == '-' and v[1:].isdigit()) else v for v in i[1:]))

def execute(reg, code):
    while 0 <= reg['ip'] < len(code):
        (op, args) = code[reg['ip']]
        op(reg, *args)

def run(program):
    code = list(parse(program))
    queue = []
    reg = defaultdict(lambda: 0, S=queue, R=queue, V=1)
    execute(reg, code)
    return reg['LAST']

def two(program):
    pass

def op_set(reg, tgt, src):
    reg[tgt] = src if isinstance(src, int) else reg[src]
    reg['ip'] += 1

def op_add(reg, tgt, src):
    reg[tgt] += src if isinstance(src, int) else reg[src]
    reg['ip'] += 1

def op_mul(reg, tgt, src):
    reg[tgt] *= src if isinstance(src, int) else reg[src]
    reg['ip'] += 1

def op_mod(reg, tgt, src):
    reg[tgt] %= src if isinstance(src, int) else reg[src]
    reg['ip'] += 1

def op_snd(reg, src):
    reg['S'] += [src] if isinstance(src, int) else [reg[src]]
    reg['ip'] += 1

def op_rcv(reg, tgt):
    if reg['V'] == 1:
        value = tgt if isinstance(tgt, int) else reg[tgt]
        if value:
            reg[tgt] = reg['LAST'] = reg['R'].pop()
            reg['ip'] = -1
        else:
            reg['ip'] += 1
    else:
        0/0

def op_jgz(reg, tgt, src):
    value = tgt if isinstance(tgt, int) else reg[tgt]
    reg['ip'] += src if value else 1

def test_18_ops():
    queue = []
    reg = defaultdict(lambda: 0, S=queue, R=queue, V=1)
    op_set(reg, 'a', 1)     ; assert reg['a'] == 1 ; assert reg['ip'] == 1
    op_add(reg, 'a', 2)     ; assert reg['a'] == 3 ; assert reg['ip'] == 2
    op_mul(reg, 'a', 'a')   ; assert reg['a'] == 9 ; assert reg['ip'] == 3
    op_mod(reg, 'a', 5)     ; assert reg['a'] == 4 ; assert reg['ip'] == 4
    op_snd(reg, 'a')        ; assert reg['R'] ==[4]; assert reg['ip'] == 5
    op_set(reg, 'a', 0)     ; assert reg['a'] == 0 ; assert reg['ip'] == 6
    op_rcv(reg, 'a')        ; assert reg['a'] == 0 ; assert reg['ip'] == 7
    op_jgz(reg, 'a', -1)                           ; assert reg['ip'] == 8
    op_set(reg, 'a', 1)     ; assert reg['a'] == 1 ; assert reg['ip'] == 9
    op_jgz(reg, 'a', -2)                           ; assert reg['ip'] == 7
    op_jgz(reg, 'a', -1)                           ; assert reg['ip'] == 6
    op_rcv(reg, 'a')        ; assert reg['a'] == 4 ; assert reg['ip'] == -1

def test_18a_ex(): assert run('set a 1|add a 2|mul a a|mod a 5|snd a|set a 0|rcv a|jgz a -1|set a 1|jgz a -2'.split('|')) == 4

def test_18a_answer(day18_lines): assert run(day18_lines) == 8600
