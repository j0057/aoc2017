def parse(lines):
    f = { int(t[0]): int(t[1]) for t in [ line.split(': ') for line in lines ] }
    return [ f.get(i, 0) for i in range(max(f)+1) ]

def traverse(firewall, delay=0):
    r = 0
    i = 0
    for t in range(delay, delay+len(firewall)):
        if firewall[i]:
            p = t % (2*(firewall[i]-1)) if firewall[i] else 0
            if delay and not p:
                return 1
            if not p:
                r += i * firewall[i] + delay
        i += 1
    return r

def delay_traversal(firewall):
    d = 1
    while traverse(firewall, d):
        d += 1
    return d

def test_13a_ex1(): assert traverse(parse(['0: 3', '1: 2', '4: 4', '6: 4'])) == 24
def test_13b_ex1(): assert delay_traversal(parse(['0: 3', '1: 2', '4: 4', '6: 4'])) == 10

def test_13a_answer(day13_lines): assert traverse(parse(day13_lines)) == 3184
def test_13b_answer(day13_lines): assert delay_traversal(parse(day13_lines)) == 3878062
