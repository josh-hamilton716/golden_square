from lib.grammar_stats import GrammarStats

def test_check_starts_with_cap_ends_with_fullstop():
    grammer1 = GrammarStats()
    assert grammer1.check("A word.") == True

def test_check_starts_with_cap_ends_with_questonmark():
    grammer1 = GrammarStats()
    assert grammer1.check("A word?") == True


def test_check_starts_with_cap_ends_with_exlimation():
    grammer1 = GrammarStats()
    assert grammer1.check("A word!") == True

def test_check_starts_with_no_cap_ends_without_puntuation():
    grammer1 = GrammarStats()
    assert grammer1.check("a word") == False

def test_check_starts_with_no_cap_ends_with_no_punctiation():
    grammer1 = GrammarStats()
    assert grammer1.check("A word") == False

def test_zero_length_string():
    grammer1 = GrammarStats()
    assert grammer1.check("") == False


def test_checking_1_correct():
    grammer1 = GrammarStats()
    grammer1.check("A word!")
    assert grammer1.percentage_good() == 100

def test_checking_1_incorrect():
    grammer1 = GrammarStats()
    grammer1.check("A word")
    assert grammer1.percentage_good() == 0

def test_checking_1_correct_2_incorrect():
    grammer1 = GrammarStats()
    grammer1.check("A word!")
    grammer1.check("A word")
    grammer1.check("A word")
    assert grammer1.percentage_good() == 33


def test_percent_good_with_no_calls():
    grammer1 = GrammarStats()
    assert grammer1.percentage_good() == 0