from lib.countwords import *

def test_countwords_blank():
    assert countwords("") == 0

def test_countwords_few():
    assert countwords("a few words") == 3