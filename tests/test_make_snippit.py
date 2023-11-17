from lib.make_snippet import *

def test_make_snippet_when_blank():
    assert make_snippet("") == ""

def test_make_snippet_when_less_5_words():
    assert make_snippet("some words of text") == "some words of text"

def test_make_snippet_when_more_5_words():
    assert make_snippet("some more words of text with a longer length") == "some more words of text..."

