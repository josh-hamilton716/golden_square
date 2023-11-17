from lib.report_length import *

def test_report_length_of_8():
    result = report_length("12345678")
    assert result == "This string was 8 characters long."

