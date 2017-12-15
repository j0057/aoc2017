def parse(s):
    return [int(v[-1]) for v in (r.split() for r in s)]

def gen(s, m, r):
    while True:
        s *= m
        s %= 0x7fffffff
        if s % r == 0:
            yield s

def duel(n, A, B):
    return sum((a ^ b) & 0xffff == 0 for (a, b, _) in zip(A, B, range(n)))

def gen1(a, b): return gen(a, 16807, 1), gen(b, 48271, 1)
def gen2(a, b): return gen(a, 16807, 4), gen(b, 48271, 8)

def test_15a_ex1(): assert duel(       5, *gen1(65, 8921)) == 1
def _est_15a_ex2(): assert duel(40000000, *gen1(65, 8921)) == 588
def test_15b_ex1(): assert duel(    1056, *gen2(65, 8921)) == 1
def _est_15b_ex2(): assert duel( 5000000, *gen2(65, 8921)) == 309

def test_15a_answer(day15_lines): assert duel(40000000, *gen1(*parse(day15_lines))) == 619
def test_15b_answer(day15_lines): assert duel( 5000000, *gen2(*parse(day15_lines))) == 290

# dedicated to baby Zea :-)
