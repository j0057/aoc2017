def parse(lines):
    return [ (int(p[0]), int(q))
             for p in (line.split(' <-> ') for line in lines)
             for q in p[1].split(', ') ]

def find_group(links, group, result):
    for (p, q) in links:
        if p != group:
            continue
        if q in result:
            continue
        result.add(q)
        find_group(links, q, result)

def plumber(links, group):
    result = set()
    find_group(links, group, result)
    return len(result)

def find_groups(links):
    groups = []
    for (p, q) in links:
        for g in groups:
            if p in g:
                if q not in g:
                    g.add(q)
                    find_group(links, q, g)
                break
        else:
            G = {p, q}
            groups.append(G)
            find_group(links, q, G)
    return len(groups)

EX12 = [
    '0 <-> 2',
    '1 <-> 1',
    '2 <-> 0, 3, 4',
    '3 <-> 2, 4',
    '4 <-> 2, 3, 6',
    '5 <-> 6',
    '6 <-> 4, 5'
]

def test_12a_ex(): assert plumber(parse(EX12), 0) == 6
def test_12b_ex(): assert find_groups(parse(EX12)) == 2

def test_12a_answer(day12_lines): assert plumber(parse(day12_lines), 0) == 152
def test_12b_answer(day12_lines): assert find_groups(parse(day12_lines)) == 186

