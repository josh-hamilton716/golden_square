from lib.check_tasks import *


def test_without():
    assert check_task("A string of text") == False

def test_with():
    assert check_task("#TODO a short string of five") == True

