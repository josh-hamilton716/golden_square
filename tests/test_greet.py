from unittest import result
from lib.greet import *

def test_greet_with_ted():
    result = greet("ted")
    assert result == "Hello, ted!"

