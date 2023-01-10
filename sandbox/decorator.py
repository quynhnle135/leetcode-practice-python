def say(text):
    return text.lower()

def shout(text):
    return text.upper()

def greet(func):
    greeting = func("""Hi, I am created by another function""")
    print(greeting)

my_string = "Yo what is up QUinn"
print(say(my_string))
print(shout(my_string))
greet(shout)
greet(say)