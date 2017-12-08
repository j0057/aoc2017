from collections import Counter
import re

def parse(lines):
    parsed = [re.match_groups(r'^(\w+) \((\d+)\)(?: -> (.*))?$', line) for line in lines]
    return ({ name: refs.split(', ') if refs else [] for (name, _, refs) in parsed },
            { name: int(weight) for (name, weight, _) in parsed })

def find_bottom(d, w):
    return next(k for k in d if not any(k in L for L in d.values()))

def get_weight(d, w, n):
    return w[n] + sum(get_weight(d, w, n2) for n2 in d[n])

def rebalance(d, w, n=None):
    bottom = n or find_bottom(d, w)
    totals = [get_weight(d, w, n2) for n2 in d[bottom]]
    counts = [v for (v, _) in Counter(totals).most_common()]
    if len(counts) != 1:
        right, *_, wrong = [v for (v, _) in Counter(totals).most_common()]
        result = rebalance(d, w, d[bottom][totals.index(wrong)])
        return result or w[d[bottom][totals.index(wrong)]] - (wrong - right)

EX7 = [
    'pbga (66)',
    'xhth (57)',
    'ebii (61)',
    'havc (66)',
    'ktlj (57)',
    'fwft (72) -> ktlj, cntj, xhth',
    'qoyq (66)',
    'padx (45) -> pbga, havc, qoyq',
    'tknk (41) -> ugml, padx, fwft',
    'jptl (61)',
    'ugml (68) -> gyxo, ebii, jptl',
    'gyxo (61)',
    'cntj (57)'
]

def test_7a_ex(): assert find_bottom(*parse(EX7)) == 'tknk'
def test_7b_ex(): assert rebalance(*parse(EX7)) == 60

def test_7a_answer(day07_lines): assert find_bottom(*parse(day07_lines)) == 'cyrupz'
def test_7b_answer(day07_lines): assert rebalance(*parse(day07_lines)) == 193
