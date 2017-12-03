from datetime import date
import os
import re

import requests

import pytest

def get_cookie():
    with open('.cookie', 'r') as f:
        return f.read().strip()

def get_input(day):
    response = requests.get('https://adventofcode.com/2017/day/{0}/input'.format(day), cookies={'session': get_cookie()})
    response.raise_for_status()
    return response

def download_inputs():
    if not os.path.isdir('input'):
        os.mkdir('input')
    today = min(25, (date.today() - date(2017, 11, 30)).days)
    for day in range(1, today + 1):
        filename = 'input/day{0:02d}.txt'.format(day)
        if os.path.exists(filename):
            continue
        response = get_input(day)
        with open(filename, 'w') as f:
            f.write(response.text)

def gen_fixture(filename):
    match = re.match(r'^(day\d\d).txt$', filename)
    if not match:
        return {}

    @pytest.fixture
    def content():
        with open('input/' + filename, 'r') as f:
            return f.read().strip()

    @pytest.fixture
    def lines():
        with open('input/' + filename, 'r') as f:
            return [ line.strip() for line in f ]

    @pytest.fixture
    def number():
        with open('input/' + filename, 'r') as f:
            return int(f.read().strip())

    return { 
        match.groups()[0]: content,
        match.groups()[0] + '_lines': lines,
        match.groups()[0] + '_number': number
    }

def generate_fixtures():
    for filename in os.listdir('input'):
        globals().update(gen_fixture(filename))

download_inputs()
generate_fixtures()
