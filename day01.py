
from itertools import cycle, islice

# The captcha requires you to review a sequence of digits (your puzzle input)
# and find the sum of all digits that match the next digit in the list. The
# list is circular, so the digit after the last digit is the first digit in the
# list.

def digit_sum(s, offset=1):
    return sum(int(a) for (a, b) in zip(s, islice(cycle(s), offset, None)) if a==b)

# Now, instead of considering the next digit, it wants you to consider the
# digit halfway around the circular list. That is, if your list contains 10
# items, only include a digit in your sum if the digit 10/2 = 5 steps forward
# matches it. Fortunately, your list has an even number of elements.

def digit_sum_halfway(s):
    return digit_sum(s, len(s) // 2)

def test_1a_ex1(): assert digit_sum('1122') == 3
def test_1a_ex2(): assert digit_sum('1111') == 4
def test_1a_ex3(): assert digit_sum('1234') == 0
def test_1a_ex4(): assert digit_sum('91212129') == 9

def test_1b_ex1(): assert digit_sum_halfway('1212') == 6
def test_1b_ex2(): assert digit_sum_halfway('1221') == 0
def test_1b_ex3(): assert digit_sum_halfway('123425') == 4
def test_1b_ex4(): assert digit_sum_halfway('123123') == 12
def test_1b_ex4(): assert digit_sum_halfway('12131415') == 4

def test_1a_answer(day01_text): assert digit_sum(day01_text) == 1136
def test_1b_answer(day01_text): assert digit_sum_halfway(day01_text) == 1092
