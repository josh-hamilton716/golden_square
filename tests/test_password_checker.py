import pytest
from lib.password_checker import *

def test_password_char():
    password_checker = PasswordChecker()
    assert password_checker.check("password1") == True

def test_error():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("pass")
    error_message = str(e.value)
    assert error_message == ("Invalid password, must be 8+ characters.")
    