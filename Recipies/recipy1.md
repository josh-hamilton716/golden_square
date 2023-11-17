# {{PROBLEM}} Function Design Recipe

As a user so that I can manage my time I want to see an estimate of readding time for a text.
Assuming I can read 200 words per minuett

## 1. Describe the Problem

They do not have a way of getting the estimated reading time for some text.


## 2. Design the Function Signature

func name = read_time
takes a string of text
takes reading speed
returns a time in minuets and seconds
so int1 for minets and int2 for seconds

```python
# EXAMPLE

def read_time(string1, reading_speed):
    """ number of words in string devided by reading speed 

    Parameters: (list all parameters and their types)
        string1: a string containing all words 
        reading_speed: an int value of how many words user can read per minuett

    Returns: (one integer and one float)
        one int for the minuets and one float for the seconds

    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
takes an empty string
"""
read_time("", 200) => 0, 0.0

"""
takes a short string of 5 words, reading speed 200
"""
read_time("a short string of five", 200) => 0, 1.5
"""
takes a short string of 5 words, reading speed 100
"""
read_time("a short string of five", 200) => 0, 3


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


