from collections import defaultdict
from threading import Thread
from time import sleep

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
    reg = defaultdict(lambda: 0, S=queue, R=queue, X=1)
    execute(reg, code)
    return reg['L']

def two(program):
    code = list(parse(program))
    q0, q1 = [], []
    r0, r1 = [defaultdict(lambda: 0, p=0, B=0, S=q0, R=q1),
              defaultdict(lambda: 0, p=1, B=0, S=q1, R=q0)]
    t0 = Thread(target=execute, args=(r0, code)) ; t0.start()
    t1 = Thread(target=execute, args=(r1, code)) ; t1.start()
    while 1:
        sleep(0.1)
        if r0['B'] and r1['B']:
            print('deadlocked!')
            r0['K'] = r1['K'] = 1
            break
        if not t0.is_alive() and not t1.is_alive():
            print('both ended!')
            break
    #t0.join()
    #t1.join()
    #print(' '.join('{0}={1}'.format(k, v) for (k, v) in sorted(r0.items())))
    #print(' '.join('{0}={1}'.format(k, v) for (k, v) in sorted(r1.items())))
    return r1['C']

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
    if reg['X']:
        value = tgt if isinstance(tgt, int) else reg[tgt]
        if value:
            reg[tgt] = reg['L'] = reg['R'].pop()
            reg['ip'] = -1
        else:
            reg['ip'] += 1
    else:
        while not reg['R']:
            if reg['K']:
                0/0
                reg['ip'] = -1
                return
            reg['B'] = 1
            sleep(0.1)
        reg['B'] = 0
        reg['C'] += 1
        reg['ip'] += 1

def op_jgz(reg, tgt, src):
    value = tgt if isinstance(tgt, int) else reg[tgt]
    reg['ip'] += src if value else 1

def test_18_ops():
    queue = []
    reg = defaultdict(lambda: 0, S=queue, R=queue, X=1)
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

def test_18b_ex():  assert two('snd 1|snd 2|snd p|rcv a|rcv b|rcv c|rcv d'.split('|')) == 4

def test_18a_answer(day18_lines): assert run(day18_lines) == 8600
def test_18b_answer(day18_lines): assert two(day18_lines) == None
