# {{PROBLEM}} Function Design Recipe

As a user so that I can improve my gramar.
I want to varify that a text starts with a captial letter and ends in a sutible sentence ending puntiation. 

## 1. Describe the Problem

The promblem is they don't have a way to check that there grammar is using correct puncuation. 



## 2. Design the Function Signature

func name = check_sentence
takes a string of text

returns true or false (a booloian)

```python
# EXAMPLE

def check_sentence(text):
    """ tests structure of sentence

    Parameters: (list all parameters and their types)
        text: a string containing all words 


    Returns: (a boolian)
        True if the first letter is captilised and the last is "." or "?" or "!"

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
check_sentence("") = True 

"""
takes a short string of 5 words with no capital letter at start or puntuation at end
"""
read_time("a short string of five") == False
"""
takes a short string of 5 words with a capital letter at the start and correct punctiation at the end
"""
read_time("A short string of five.") == True


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


