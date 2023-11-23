from lib.todo_list import *

def test_non_added_incomplete():
    my_list1 = TodoList()
    assert my_list1.incomplete() == []


def test_non_added_complete():
    my_list1 = TodoList()
    assert my_list1.complete() == []
