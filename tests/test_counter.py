from lib.counter import *

def test_counter():
    counter1 = Counter()
    counter1.add(1)
    counter1.add(2)
    result = counter1.report()
    assert result == "Counted to 3 so far."