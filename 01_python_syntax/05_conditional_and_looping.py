"""
    CONDITIONAL AND LOOPING LOGIC:
"""

a = 200
b = 20
if a > b:
  if a > 100:
    print("A is also greater than 100")
  else:
    print("A is not greater than 100")
  print("A is greater than B")
elif a == b:
  print("A is equal to B")
else:
  print("Nothing matched")



# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")

# # one line if else
# a = 2
# b = 330
# print("A") if a > b else print("B")

# # one line 3 conditions
# a = 330
# b = 330
# print("A") if a > b else print("=") if a == b else print("B")



# i = 1
# while i < 6:
#   print(i)
#   i += 1


# # With the break statement we can stop the loop even if the while condition is true
# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1


# # With the continue statement we can stop the current iteration, and continue with the next:
# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)



# # A for loop is used for iterating over a sequence

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
