from functools import reduce
from operator import xor

def knot_hash(buf, data, rounds=1):
    i, s = 0, 0
    C = len(buf)
    for _ in range(rounds):
        for v in data:
            e = i+v
            r1 = buf[i:min(C, e)]
            r2 = [] if e<C else buf[0:e%C]
            for (j, x) in enumerate((r1+r2)[::-1]):
                buf[(i+j)%C] = x
            i = (i + v + s) % C
            s += 1
    return buf

def knot_hash_prod(buf, data):
    buf = list(range(buf))
    buf = knot_hash(buf, data)
    return buf[0] * buf[1]

def knot_ascii(data):
    data = [ord(x) for x in data] + [17, 31, 73, 47, 23]
    buf = list(range(256))
    buf = knot_hash(buf, data, rounds=64)
    result = [reduce(xor, buf[i:i+16], 0) for i in range(0, 256, 16)]
    return ''.join('{:02x}'.format(v) for v in result)

def test_10a_ex(): assert knot_hash_prod(5, [3, 4, 1, 5]) == 12

def test_10b_ex1(): assert knot_ascii('') == 'a2582a3a0e66e6e86e3812dcb672a272'
def test_10b_ex2(): assert knot_ascii('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
def test_10b_ex3(): assert knot_ascii('1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d'
def test_10b_ex4(): assert knot_ascii('1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e'

def test_10a_answer(day10): assert knot_hash_prod(256, [int(x) for x in day10.split(',')]) == 9656
def test_10b_answer(day10): assert knot_ascii(day10) == '20b7b54c92bf73cf3e5631458a715149'
