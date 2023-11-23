from lib.todo_list import *
from lib.todo import *

def test_checks_two_added():
    item1 = Todo("walk the dog")
    item2 = Todo("go for a swim")
    my_todo_list = TodoList()
    my_todo_list.add(item1)
    my_todo_list.add(item2)
    assert my_todo_list.complete() == []

def test_checks_two_added_check_incomplete():
    item1 = Todo("walk the dog")
    item2 = Todo("go for a swim")
    my_todo_list = TodoList()
    my_todo_list.add(item1)
    my_todo_list.add(item2)
    assert my_todo_list.incomplete() == [item1, item2]


def test_checks_two_added_check_incomplete_when_one_changed():
    item1 = Todo("walk the dog")
    item1.complete = True
    item2 = Todo("go for a swim")
    my_todo_list = TodoList()
    my_todo_list.add(item1)
    my_todo_list.add(item2)
    assert my_todo_list.incomplete() == [item2]


def test_checks_two_added_check_incomplete_when_two_changed():
    item1 = Todo("walk the dog")
    item1.complete = True
    item2 = Todo("go for a swim")
    item2.complete = True
    my_todo_list = TodoList()
    my_todo_list.add(item1)
    my_todo_list.add(item2)
    assert my_todo_list.complete() == [item1, item2]

def test_checks_two_added_then_give_up():
    item1 = Todo("walk the dog")
    item2 = Todo("go for a swim")
    my_todo_list = TodoList()
    my_todo_list.add(item1)
    my_todo_list.add(item2)
    my_todo_list.give_up()
    assert my_todo_list.complete() == [item1, item2]
