#!/usr/bin/python3.5

from itertools import cycle, islice

def digit_sum(s):
    numbers = list(map(int, s))
    return sum(a for (a, b) in zip(numbers, islice(cycle(numbers), 1, None)) if a==b)

def test_1a_ex1(): assert digit_sum('1122') == 3
def test_1a_ex2(): assert digit_sum('1111') == 4
def test_1a_ex3(): assert digit_sum('1234') == 0
def test_1a_ex4(): assert digit_sum('91212129') == 9

def test_1a_answer():
    with open('input/day01.txt') as f:
        assert digit_sum(f.read().strip()) == 1136
