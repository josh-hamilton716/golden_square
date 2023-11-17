from lib.string_builder import *

def test_string_builder_length():
    string_class1 = StringBuilder()
    string_class1.add("a string of length 21")
    result = string_class1.size()
    assert result == 21

def test_string_builder_text():
    string_class1 = StringBuilder()
    string_class1.add("a string of length 21")
    result = string_class1.output()
    assert result == "a string of length 21"

def test_string_builder_two_strings():
    string_class1 = StringBuilder()
    string_class1.add("first string")
    string_class1.add(" and second string")
    result = string_class1.output()
    assert result == "first string and second string"
