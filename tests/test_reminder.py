import pytest
from lib.reminder import *

def test_reminds_the_user_to_do_a_task():
    reminder = Reminder("Kay")
    reminder.remind_me_to("Walk the dog")
    result = reminder.remind()
    assert result == "Walk the dog, Kay!"
    
def test_empty_reminder():
    reminder = Reminder("Kay")
    with pytest.raises(Exception) as e: # deals with an exception
        reminder.remind()
    error_message = str(e.value) # returns the error message to a sting variable
    assert error_message == "No reminder set!"
