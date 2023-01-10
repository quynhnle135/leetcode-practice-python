class Car:
    wheels = 4
    noise = "Vroom Vroom"

    def __str__(self):
        return f"Car sounds {self.noise}"


class MyClass:
    x = " "
    y = 0
    def __init__(self, anyNumber, anyString):
        self.x = anyNumber
        self.y = anyString

    def __str__(self):
        return f"My class is {self.x} and my name is {self.y}"


my_car = Car()
print(str(my_car))
print(my_car.__str__())

mimi_class = MyClass(17, "Mimi")
print(mimi_class.__str__())
print(mimi_class.__repr__())
print(str(mimi_class))


x = 1234
y = str(x)
print(type(x))
print(type(str(x)))
print(str(x) + " is my ID")
print(type(y))