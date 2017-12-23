from collections import defaultdict
from day18 import execute
from itertools import count, islice

def one(program):
    code = [line.split() for line in program]
    reg = defaultdict(int, COUNT={}, V=3)
    execute(reg, code)
    return reg['COUNT'].get('mul', 0)

def two(N):
    n1 = N * 100 + 100000
    n2 = N * 100 + 100000 + 17000
    is_prime = lambda n: all(n % i for i in range(2, int(n ** 0.5)+1))
    composites = [n for n in range(n1, n2+1, 17) if not is_prime(n)]
    return len(composites)

def test_23a_answer(day23_lines): assert one(day23_lines) == 9409

def test_23b_ex():     assert two(57) == 915
def test_23b_answer(): assert two(99) == 913
