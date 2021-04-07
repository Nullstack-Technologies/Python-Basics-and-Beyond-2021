# class Person:    
#     first_name = "John"
#     last_name = "Doe"


# person_1 = Person()
# person_2 = Person()

# person_1.first_name = 'Joe'
# print(person_1.first_name)
# print(person_1.last_name)

# print(person_2.first_name)
# print(person_2.last_name)


# class Person:
#     first_name = ""
#     last_name = ""

#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name

#     def full_name(self):
#         print(self.first_name + " "  + self.last_name)


# person_1 = Person("John", "Doe")
# person_1.full_name()

# person_2 = Person("Mr", "Coder")
# person_2.full_name()

# # print(person_1.first_name)
# # print(person_2.first_name)



# class Car:

#     def ignition(self):
#         pass

#     def breaking(self):
#         pass

# car = Car()
# car.igniton()


# class Person:
#     name = ""
#     age = ""

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"Person<{self.name}>"

#     # def __eq__(self, value):
#     #     return self.age == value.age

#     # def __lt__(self, value):
#     #     return self.age < value.age


# person_1 = Person("John", "100")
# person_2 = Person("Doe", "99")
# print(person_1)
# print(person_2)

# print(person_1 == person_2)



class Car:
    price = 0
    name = ""

    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name} - Price {self.price}"
    
    def __lt__(self, value):
        return self.price < value.price
    
    def __gt__(self, value):
        return self.price > value.price

bmw = Car("BMW", "3000000")
lambo = Car("BMW", "30000000")
print(bmw)
print(lambo)

print(bmw < lambo)
