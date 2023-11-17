from lib.diary_entry import *
import pytest

def test_check_entry_created():
    diary = DiaryEntry("day1","went for a walk")
    assert diary.title == "day1"
    assert diary.contents == "went for a walk"

def test_format_correctly_formats():
    diary = DiaryEntry("day1","went for a walk") 
    assert diary.format() == "day1: went for a walk"

def test_numbeer_of_words():
    diary = DiaryEntry("day1","went for a walk") 
    assert diary.count_words() == 5

def test_numbeer_of_words_zero_legth():
    diary = DiaryEntry("","") 
    assert diary.count_words() == 0

def test_reading_time():
    diary = DiaryEntry("day one","went for a walk")
    assert diary.reading_time(2) == 3

def test_reading_time_fraction():
    diary = DiaryEntry("day one","went for a walk today")
    assert diary.reading_time(2) == 4

def test_reading_time_zero():
    diary = DiaryEntry("day one","went for a walk")
    with pytest.raises(Exception) as e:
        diary.reading_time(0)
    assert str(e.value) == "You must read more than 0 words per minute"

def test_read_first_chunck():
    diary = DiaryEntry("day one","went for a walk")
    assert diary.reading_chunk(3,1) == "went for a" 

def test_read_2_chuncks_of_text():
    diary = DiaryEntry("day one","went for a walk")
    diary.reading_chunk(2,1)
    assert diary.reading_chunk(2,1) == "a walk"

def test_read_3_chuncks_of_text():
    diary = DiaryEntry("day one","went for a walk")
    diary.reading_chunk(2,1)
    diary.reading_chunk(2,1)
    assert diary.reading_chunk(2,1) == "went for"

def test_read_chuncks_no_reading_speed():
    diary = DiaryEntry("day one","went for a walk")
    assert diary.reading_chunk(0,0) == ""

