import pytest

import names
from first_names_male import first_names_male
from first_names_female import first_names_female
from last_names import last_names

def test_get_weights():
    w = names.get_weights(3)
    assert w == [3, 2, 1]

def test_get_weights_popularity():
    w = names.get_weights(4, popularity=2)
    assert w == [16, 9, 4, 1]

def test_get_name():
    f, l = names.get_name()
    assert f in first_names_female + first_names_male
    assert l in last_names

    f, l = names.get_name(gender='male')
    assert f in first_names_male
    assert l in last_names

    f, l = names.get_name(gender='female')
    assert f in first_names_female
    assert l in last_names