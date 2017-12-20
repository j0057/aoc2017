from collections import Counter
import math
import re

def parse(lines):
    for line in lines:
        px, py, pz, vx, vy, vz, ax, ay, az = [int(x) for x in re.findall(r'-?\d+', line)]
        yield (px, py, pz), (vx, vy, vz), (ax, ay, az)

def pythagoras(x, y, z):
    return math.sqrt(x**2 + y**2 + z**2)

def add(ax, ay, az, bx, by, bz):
    return (ax+bx, ay+by, az+bz)

def one(particles):
    return min(enumerate(particles), key=lambda t: pythagoras(*t[1][2]))[0]

def two(particles):
    count = len(particles)
    same = 0
    while same < 11:
        positions = Counter(p for (p, _, _) in particles)
        particles = [(add(*p, *add(*v, *a)), add(*v, *a), a)
                     for (p, v, a) in particles
                     if positions[p] == 1]
        same = same+1 if len(particles) == count else 0
        count = len(particles)
    return len(particles)
    
EX20A = ['p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>', 'p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>']
EX20B = ['p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>', 'p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>',
         'p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>', 'p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>']

def test_20a_ex(): assert one([*parse(EX20A)]) == 0
def test_20b_ex(): assert two([*parse(EX20B)]) == 1

def test_20a_answer(day20_lines): assert one([*parse(day20_lines)]) == 91
def test_20b_answer(day20_lines): assert two([*parse(day20_lines)]) == 567
