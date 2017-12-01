import os
import re

import pytest

def gen_fixture(filename):
    match = re.match(r'^(day\d\d).txt$', filename)
    if not match:
        return {}

    @pytest.fixture
    def fixture():
        with open('input/' + filename, 'r') as f:
            return f.read()

    return { match.groups()[0]: fixture }

def generate_fixtures():
    for filename in os.listdir('input'):
        globals().update(gen_fixture(filename))

generate_fixtures()
