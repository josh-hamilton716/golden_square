from lib.read_time import *

def test_read_time_empty_string():
    assert read_time("", 200) == "0 minniets and 0.0 seconds"

"""
takes a short string of 5 words, reading speed 200
"""
def test_read_time_when_5_string_and_speed_200():
    assert read_time("a short string of five", 200) == "0 minniets and 1.5 seconds"
"""
takes a short string of 5 words, reading speed 100
"""
def test_read_time_when_5_string_and_speed_100():
    assert read_time("a short string of five", 100) == "0 minniets and 3.0 seconds"

def test_return_2_for_mins():
    assert read_time("a string of text with a length of twenty words so it will return the number two for the minetts", 10) == "2 minniets and 0.0 seconds"
