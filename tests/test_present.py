import pytest
from lib.present import *

def test_present_wrap_none():
    pres1 = Present()
    with pytest.raises(Exception) as e:
        pres1.wrap("1")
        pres1.wrap("2")
    error = str(e.value)
    assert error == "A contents has already been wrapped."


def test_present_unwrap_none():
    pres1 = Present()
    with pytest.raises(Exception) as e:
        pres1.unwrap()
    error = str(e.value)
    assert error == "No contents have been wrapped."
