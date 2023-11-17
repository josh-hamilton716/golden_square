from lib.todo_tasks import *

def test_no_tasks_added():
    tasklist = todo_tasks()
    assert tasklist.show_tasks() == []

def test_one_added():
    tasklist = todo_tasks()
    tasklist.add_task("walk the dog")
    assert tasklist.show_tasks() == ["walk the dog"]


def test_2_added():
    tasklist = todo_tasks()
    tasklist.add_task("walk the dog")
    tasklist.add_task("go for a bike ride")
    assert tasklist.show_tasks() == ["walk the dog", "go for a bike ride"]

def test_add_then_remove():
    tasklist = todo_tasks()
    tasklist.add_task("go for a bike ride")
    tasklist.add_task("walk the dog")
    tasklist.remove_task("go for a bike ride")
    assert tasklist.show_tasks() == ["walk the dog"]