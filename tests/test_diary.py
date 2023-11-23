from lib.diary import *
import pytest


def test_diary_entry():
    diary = Diary()
    assert diary.all() == []

def test_inital_word_count_0():
    diary = Diary()
    assert diary.count_words() == 0

def test_words_per_min_nothing_in_diary():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.reading_time(2)
    assert str(e.value) == "no entry in diary"


def test_reading_time_raises_error():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.reading_time(0)
    assert str(e.value) == "you must read more that 0 words per minuett"


def test_best_entry_initally_raises_error():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.find_best_entry_for_reading_time(2,2)
    assert str(e.value) == "no entry in diary"
