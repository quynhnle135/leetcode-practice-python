from prime_numbers import *

def test_prime_numbers_one():
    assert check_prime_number(5) == True


def test_prime_numbers_two():
    assert check_prime_number(7) == True


def test_prime_numbers_three():
    assert check_prime_number(4) == False


def test_prime_numbers_four():
    assert check_prime_number(1) == False

