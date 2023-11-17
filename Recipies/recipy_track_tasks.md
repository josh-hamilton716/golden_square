# {{PROBLEM}} Function Design Recipe

As a user so that I can keep track of my tasks I want to check if a string includes the string "#TODO"


## 1. Describe the Problem

They do not currently have a way of tracking there tasks


## 2. Design the Function Signature

func name = ckeck_task
takes a string of text
returns a boolian
so return True if cotains "#TODO" and False if not

```python
# EXAMPLE

def ckeck_task(string1):
    """ check if #TODO is in string

    Parameters: (list all parameters and their types)
        string1: a string containing the text

    Returns: (one boolian)
        True for if text comtains "#TODO"
        False for if does not contain "#TODO"

    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
takes a string that does not contain #TODO 
"""
ckeck_task("A string of text") == False

"""
takes a short string that does contain #TODO 
"""
ckeck_task("#TODO a short string of five") == True
"""



```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

```

Ensure all test function names are unique, otherwise pytest will ignore them!


