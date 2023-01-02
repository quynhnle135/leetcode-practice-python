from odd_even_numbers import *

def test_check_odd_one():
    assert check_odd(3) == True


def test_check_odd_two():
    assert check_odd(4) == False


def test_check_even_one():
    assert check_even(4) == True


def test_check_even_two():
    assert check_even(5) == False