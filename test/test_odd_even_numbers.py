from odd_even_numbers import *

def test_odd_numbers_one():
    assert check_odd(13) == True


def test_odd_numbers_two():
    assert check_odd(4) == False


def test_even_numbers_one():
    assert check_even(4) == True


def test_even_numbers_two():
    assert check_even(5) == False


