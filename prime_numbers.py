def check_prime_number(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False

    return True

print(check_prime_number(5))
print(check_prime_number(4))
print(check_prime_number(7))