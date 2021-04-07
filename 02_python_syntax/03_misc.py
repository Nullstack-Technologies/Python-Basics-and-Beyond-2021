# # list comprehension
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# # with list comprehension
# print([x for x in fruits if "ap" in x])

# # without list comprehension
# new_list = []
# for x in fruits:
#     if "ap" in x:
#         new_list.append(x)
# print(new_list)




# lambda Functions
add = lambda x, y: x + y 
total =  add(2, 3)
print(total)


# def call_me_anything(n):
#     return lambda a: a * n

# doubler = call_me_anything(2)
# tripler = call_me_anything(3)
# print(doubler(5))
# print(tripler(5))



# String Formatting

first_name = "Nauman"
last_name = "Arif"
age = 100

# print(first_name + " " + last_name)

# print("My Name is {} and my age is {}".format(first_name, age))

# print(f"My Name is {first_name} and my age is {age}")

