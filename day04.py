
from collections import Counter

def check(s):
    c = Counter(s.split())
    n = c.most_common(1)[0][1]
    return n == 1

def count_acceptable(words):
    return sum(1 for word in words if check(word))

def check2(s):
    c = Counter(str(sorted(w)) for w in s.split())
    n = c.most_common(1)[0][1]
    return n == 1

def count_acceptable2(words):
    return sum(1 for word in words if check2(word))

def test_4a_ex1(): assert check('aa bb cc dd ee')
def test_4a_ex2(): assert not check('aa bb cc dd aa')
def test_4a_ex3(): assert check('aa bb cc dd aaa')

def test_4b_ex1(): assert check2('abcde fghij')
def test_4b_ex2(): assert not check2('abcde xyz ecdab')
def test_4b_ex3(): assert check2('a ab abc abd abf abj')
def test_4b_ex4(): assert check2('iiii oiii ooii oooi oooo')
def test_4b_ex5(): assert not check2('oiii ioii iioi iiio')

def test_4a_answer(day04_lines): assert count_acceptable(day04_lines) == 477
def test_4b_answer(day04_lines): assert count_acceptable2(day04_lines) == 167

# 06:11 .. #703 for 1st, #567 for 2nd
# (vim process started at 06:02:59 / >#100 for 1st star / #58 for 2nd star)
# 1st at 06:07:40 -> 4m41s (#1 in 0m37s, #100 in 1m53s)
# 2nd at 06:11:52 -> 8m53s (#1 in 1m10s, #100 in 3m40s)
# clearly can't afford the luxury of unit testing :-)
