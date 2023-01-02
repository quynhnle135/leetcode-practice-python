from prime_numbers import check_prime_number


def test_check_prime_numbers_one():
    assert check_prime_number(5) == True


def test_check_prime_numbers_two():
    assert check_prime_number(4) == False


def test_check_prime_numbers_three():
    assert check_prime_number(7) == True

