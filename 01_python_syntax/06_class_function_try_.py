"""
    Functions

    A function is a block of code which only runs when it is called.

    You can pass data, known as parameters, into a function.

    A function can return data as a result.
"""


def my_function():
  print("Hello from a function")


# def my_function(fname):
#   print("name: " + fname)


def return_two_things():
    return 1, 2

my_function()
a ,b = return_two_things()
print(a, b)

# Lambda Functions

x = lambda a : a + 10



"""
    Classes

    Python is an object oriented programming language.

    Almost everything in Python is an object, with its properties and methods.

    A Class is like an object constructor, or a "blueprint" for creating objects.
"""

class NullStack:
  services = 'awesome'

p1 = NullStack()
print(p1.services)


class NullStackTwo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = NullStackTwo("Sayema Fatema", 26)
p1.myfunc()

"""
    The try block lets you test a block of code for errors.

    The except block lets you handle the error.

    The finally block lets you execute code, regardless of the result of the try- and except blocks.
"""

try:
    print(x)
except:
    print("An exception occurred")



