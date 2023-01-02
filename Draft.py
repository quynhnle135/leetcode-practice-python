def say_my_name(name):
    print('Hi my name is', name)

def basic_sum(a, b):
    return a + b


def print_values(array):
    for i in array:
        print(i, end=" ")


def print_numbers():
    for i in range(2, 11, 2):
        print(i, end=" ")


say_my_name('Hoshi')
basic_sum(1, 2)
print(basic_sum(1, 2))
my_arr = [1, 2, 3, 4]
print_values(my_arr)
print()
print_numbers()