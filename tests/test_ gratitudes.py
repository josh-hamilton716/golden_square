from lib.gratitudes import *

# test empty
def test_gratitudes_emplty():
    grat1 = Gratitudes()
    assert grat1.format() == "Be grateful for: "

# test when there is 2 in list
def test_gratitudes_two_list():
    grat1 = Gratitudes()
    grat1.add("jam")
    grat1.add("basketball")
    assert grat1.format() == "Be grateful for: jam, basketball"


