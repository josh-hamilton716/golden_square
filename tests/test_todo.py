from lib.todo import *


def test_setup_todo():
    item1 = Todo("walk the dog")
    assert item1.task == "walk the dog"

def test_completed():
    item1 = Todo("walk the dog")
    item1.mark_complete()
    assert item1.complete == True
    