"""
    Functions

    A function is a block of code which only runs when it is called.

    You can pass data, known as parameters, into a function.

    A function can return data as a result.
"""


# def my_function():
#     """
#         Prints my name
#     """
#     print("Hello from a function")

# my_function()


# def my_function(first_name, last_name):
#   print(first_name + " " + last_name)

# my_function("Sayema", "Fatema")


# def calculate_power(a, b=0):
#     return a ** b

# result = calculate_power(2)
# print(result)

# def calculate_power_and_multiplication(a, b=0):
#     return a ** b, a * b

# power, multiplication = calculate_power_and_multiplication(2, 8)
# print(power)
# print(multiplication)



# # def my_function(fname):
# #   print("name: " + fname)


# def return_two_things():
#     return 1, 2

# my_function()
# a ,b = return_two_things()
# print(a, b)

# # Lambda Functions

# x = lambda a : a + 10



# """
#     Classes

#     Python is an object oriented programming language.

#     Almost everything in Python is an object, with its properties and methods.

#     A Class is like an object constructor, or a "blueprint" for creating objects.
# """                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

class Person:
    name = ""

    def __init__(self, name):
        self.name = name

    def print_name(self):
        print("My name is " + self.name)


p1 = Person(name="Sayema Fatema")
p1.print_name()

p2 = Person(name="Nauman Arif")
p2.print_name()







# class Company:
#   def __init__(self):
#     super().__init__()

# p1 = Company()
# print(p1.services)


# class NullStackTwo:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def myfunc(self):
#         print("Hello my name is " + self.name)

# p1 = NullStackTwo("Sayema Fatema", 26)
# p1.myfunc()

# """
#     The try block lets you test a block of code for errors.

#     The except block lets you handle the error.

#     The finally block lets you execute code, regardless of the result of the try- and except blocks.
# """

# try:
#     print(x)
# except:
#     print("An exception occurred")



