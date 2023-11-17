1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.



2. Design the Class Interface
The interface of a class includes:

The name of the class.
The design of its initializer, the parameters it takes, and their data types
The design of any properties the user will need to read or write, and their data types
The design of its public methods, including:
Their names and purposes
What parameters they take and the data types
What they return and that data type
Any other side effects they might have
Steps 3 and 4 then operate as a cycle.


class name = todo_tasks
no parameters

method = add_task
one parameter = a string that represents the task
does not return

method = show_tasks
no parameters
returns a list of the tasks


method = remove_task
one parameter = a string that represents the task
does not return

3. Create Examples as Tests
These are examples of the class being used with different initializer arguments, method calls, and how it should behave.

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

For complex challenges you might want to come up with a list of examples first and then test-drive them one by one. For simpler ones you might just dive straight into writing a test for the first example you want to address.

4. Implement the Behaviour
For each example you create as a test, implement the behaviour that allows the class to behave according to your example.

At this point you may wish to apply small-step test-driving to manage the complexity. This means you only write the minimum lines of the example to get the test to fail (red), then make it pass (green) and refactor, before adding another line to the test until it fails, then continue.

Then return to step 3 until you have addressed the problem you were given. You may also need to revise your design, for example if you realise you made a mistake earlier.

