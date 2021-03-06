"""
    CONDITIONAL AND LOOPING LOGIC:
"""

# a = 200
# b = 20
# if a > b:
#   if a > 100:
#     print("A is also greater than 100")
#   else:
#     print("A is not greater than 100")
#   print("A is greater than B")
# elif a == b:
#   print("A is equal to B")
# else:
#   print("Nothing matched")



# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")

# one line if else
# a = 2
# b = 330

# if a > b:
#   print("A")
# else:
#   print("B")

# print("A") if a > b else print("B")
# # do this   if (this is true) else do this

# # one line 3 conditions
# a = 330
# b = 330

# if a > b:
#   print("A")
# elif a == b:
#   print("=")
# else:
#   print("B")

# print("A") if a > b else print("=") if a == b else print("B")
# # do this if (this is true) else (do this if (this true) else do this)


# and, or and not
# salary = 4.5 # in Lakhs per Annum
# experience = 2 # in years

# I will take  a job which has minimum 4.2LPA and  experience of 3 years

# if salary >= 4.2 and experience <= 3:
#   print("I can give a thought about your offer ❤️")
# elif salary >= 4.2 and experience > 3:
#   print("I cannot continue as I don't have the no of years required")
# elif salary <= 4.2 and experience <= 3:
#   print("I cannot continue as I am not getting my desired salary")
# else:
#   print("I cannot continue as I am not getting my desired salary as well I don't have the no of years required ")

# I will take if either of  the salary is minimum 4.2LPA  or  experience of 3 years

# if salary >= 4.2 or experience <= 3:
#   print("I can give a thought about your offer ❤️")
# else:
#   print("I cannot continue as I am not getting my desired salary as well I don't have the no of years required ")


# salary = 4.5 # in Lakhs per Annum
# experience = 2 # in years

# # I will take the job if the salary is NOT less than equal to 2.8 and the experience is NOT greater than 2 years

# if not (salary <= 2.8 and experience > 2):
#   # true and true
#   print("Okay")
# else:
#   print("Not Okay")






 

# i = 1
# while i < 6:
#   print(i)
#   i += 1


# With the break statement we can stop the loop even if the while condition is true
i = 1
while i < 6:  #  loop until i is less than 6
  print(i) # print i
  if i == 3: 
    break
  i += 1  # incrementing


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
