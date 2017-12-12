import networkx as nx

def parse(lines):
    g = nx.Graph()
    g.add_edges_from((int(p[0]), int(q))
                     for p in (line.split(' <-> ') for line in lines)
                     for q in p[1].split(', '))
    return g

def group_len(g, n):
    return next(len(s) for s in nx.connected_components(g) if n in s)

def group_count(g):
    return len(list(nx.connected_components(g)))

EX12 = [
    '0 <-> 2',
    '1 <-> 1',
    '2 <-> 0, 3, 4',
    '3 <-> 2, 4',
    '4 <-> 2, 3, 6',
    '5 <-> 6',
    '6 <-> 4, 5'
]

def test_12a_ex(): assert group_len(parse(EX12), 0) == 6
def test_12b_ex(): assert group_count(parse(EX12)) == 2

def test_12a_answer(day12_lines): assert group_len(parse(day12_lines), 0) == 152
def test_12b_answer(day12_lines): assert group_count(parse(day12_lines)) == 186

