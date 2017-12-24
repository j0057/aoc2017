from collections import defaultdict

def parse(lines):
    c = defaultdict(set)
    for line in lines:
        a, b = [int(x) for x in line.split('/')]
        c[a].add(b)
        c[b].add(a)
    return c

def bridges(components, bridge):
    if not bridge:
        bridge = [(0, 0)]
    last = bridge[-1][1]
    for c in components[last]:
        if (last, c) in bridge:
            continue
        if (c, last) in bridge:
            continue
        new = bridge + [(last, c)]
        yield new
        yield from bridges(components, new)

def one(components):
    return max(sum(a+b for (a,b) in bridge) for bridge in bridges(components, None))

def two(components):
    return max((len(bridge), sum(a+b for (a,b) in bridge))
               for bridge in bridges(components, None))[1]

EX = '0/2 2/2 2/3 3/4 3/5 0/1 10/1 9/10'.split()

def test_24a_ex(): assert one(parse(EX)) == 31
def test_24b_ex(): assert two(parse(EX)) == 19

def test_24a_answer(day24_lines): assert one(parse(day24_lines)) == 1511
def test_24b_answer(day24_lines): assert two(parse(day24_lines)) == 1471
