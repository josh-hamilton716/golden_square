from lib.check_sentence import *


"""takes an empty string
"""
def test_check_empty_sentence():
    assert check_sentence("") == True 

"""
takes a short string of 5 words with no capital letter at start or puntuation at end
"""
def test_check_when_no_caps_or_punctiation():
    assert check_sentence("a short string of five") == False
"""
takes a short string of 5 words with a capital letter at the start and correct punctiation at the end
"""
def test_check_when_has_caps_and_punctiation_at_end():
    assert check_sentence("A short string of five.") == True
