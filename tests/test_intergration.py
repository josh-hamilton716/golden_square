from lib.diary import *
from lib.diary_entry2 import *

def test_add_and_recall():
    diary = Diary()
    entry1 = DiaryEntry("Title 1", "some text")
    entry2 = DiaryEntry("Title 2", "some text")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.all() == [entry1, entry2]

def test_count_words_sum_all_in_contents():
    diary = Diary()
    entry1 = DiaryEntry("Title 1", "some text")
    entry2 = DiaryEntry("Title 2", "more words")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.count_words() == 4

""" reading time set to 2 words per min
set 5 words
should be read in 2 and half mins, rounds up so returns 3 """
def test_reading_time_3_mins_5_words():
    diary = Diary()
    entry1 = DiaryEntry("Title 1", "some text")
    entry2 = DiaryEntry("Title 2", "some more words")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.reading_time(2) == 3


def test_diary_find_best_entry_returns_first_entry():
    diary = Diary()
    entry1 = DiaryEntry("Title 1", "some text")
    entry2 = DiaryEntry("Title 2", "some more words with a longer text string")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry1

def test_first_entry_returns_most_sutable():
    diary = Diary()
    entry1 = DiaryEntry("Title 1", "some test text")
    diary.add(entry1)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry1

def test_first_entry_not_enought_time():
    diary = Diary()
    entry1 = DiaryEntry("Title 2", "some more words with a longer text string")
    diary.add(entry1)
    assert diary.find_best_entry_for_reading_time(2, 3) == None

