from lib.check_codeword import *

def test_codeword_horse():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_codeword_home():
    result = check_codeword("home")
    assert result == "Close, but nope."

def test_codeword_bat():
    result = check_codeword("bat")
    assert result == "WRONG!"

def test_codeword_hang():
    result = check_codeword("hang")
    assert result == "WRONG!"

def test_codeword_phone():
    result = check_codeword("phone")
    assert result == "WRONG!"

