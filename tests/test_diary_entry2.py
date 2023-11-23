from lib.diary_entry2 import *
import pytest

def test_reading_time_when_wpm_is_2():
    entry = DiaryEntry("title1","some text length four")
    assert entry.reading_time(2) == 2


def test_reading_time_when_0_wpm_is_passed():
    entry = DiaryEntry("title1","some text length four")
    with pytest.raises(Exception) as e:
        entry.reading_time(0)
    assert str(e.value) == "you must read more that 0 words per minuett"

def test_diary_entry_count_words():
    entry = DiaryEntry("title1","some text length four")
    assert entry.count_words() == 4

def test_readable_first_chunck():
    entry = DiaryEntry("title1","some text length four")
    assert entry.reading_chunk(2, 1) == "some text"

def test_readable_second_chunck():
    entry = DiaryEntry("title1","some text length four")
    entry.reading_chunk(2, 1)
    assert entry.reading_chunk(2, 1) == "length four"


def test_readable_first_chunck_second_time():
    entry = DiaryEntry("title1","some text length four")
    entry.reading_chunk(2, 1)
    entry.reading_chunk(2, 1)
    assert entry.reading_chunk(2, 1) == "some text"