from datetime import date
import os
import re

import requests

import pytest

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

    return { 
        match.groups()[0]: content,
        match.groups()[0] + '_lines': lines
    }

def download_inputs():
    with open('.cookie', 'r') as f:
        cookie = f.read().strip()
    today = min(25, (date.today() - date(2017, 11, 30)).days)
    if not os.path.isdir('input'):
        os.mkdir('input')
    for day in range(1, today + 1):
        if os.path.exists('input/day{0:02d}.txt'.format(day)):
            continue
        response = requests.get('https://adventofcode.com/2017/day/{0}/input'.format(day), cookies={'session': cookie})
        response.raise_for_status()
        with open('input/day{0:02d}.txt'.format(day), 'w') as f:
            f.write(response.text)

def generate_fixtures():
    for filename in os.listdir('input'):
        globals().update(gen_fixture(filename))

download_inputs()
generate_fixtures()
