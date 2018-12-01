
def score(s):
    S, G = 0, 0
    d, i, g = 0, 0, 0
    while i < len(s):
        if s[i] == '!':
            i += 1
        elif not g and s[i] == '{':
            d += 1
        elif not g and s[i] == '}':
            S += d
            d -= 1
        elif not g and s[i] == '<':
            g = 1
        elif s[i] == '>':
            g = 0
        elif g:
            G += 1
        i += 1
    return (S, G)

def test_9a_ex1(): assert score('{}')[0] == 1
def test_9a_ex2(): assert score('{{{}}}')[0] == 6
def test_9a_ex3(): assert score('{{},{}}')[0] == 5
def test_9a_ex4(): assert score('{{{},{},{{}}}}')[0] == 16
def test_9a_ex5(): assert score('{<a>,<a>,<a>,<a>}')[0] == 1
def test_9a_ex6(): assert score('{{<ab>},{<ab>},{<ab>},{<ab>}}')[0] == 9
def test_9a_ex7(): assert score('{{<!!>},{<!!>},{<!!>},{<!!>}}')[0] == 9
def test_9a_ex8(): assert score('{{<a!>},{<a!>},{<a!>},{<ab>}}')[0] == 3

def test_9b_ex1(): assert score('<>')[1] == 0
def test_9b_ex2(): assert score('<random characters>')[1] == 17
def test_9b_ex3(): assert score('<<<<>')[1] == 3
def test_9b_ex4(): assert score('<{!>}>')[1] == 2
def test_9b_ex5(): assert score('<!!>')[1] == 0
def test_9b_ex6(): assert score('<!!!>>')[1] == 0
def test_9b_ex7(): assert score('<{o"i!a,<{i<a>')[1] == 10

def test_9_answer(day09_text): assert score(day09_text) == (12505, 6671)
