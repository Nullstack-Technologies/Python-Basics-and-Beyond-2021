"""
    Use Functions to Calculate the Factorial of a number
"""


# def factorial(n):
#     """
#         This Function computes the factorial of a number.
#         3! = 3 * 2 *1 = 6
#         input: integer
#         outputs: factorial of it
#     """
#     fact = 1

#     for i in range(1, n + 1):
#         fact *= i

#     return fact


# def factorial(n):
#     """
#         Find the Factorial of a number n
#         using recursion
#     """

#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# # factorial(3)
# # else 
# # 3 * factorial(2)

# # factorial(2)
# # else
# # 2 * factorial(1)

# # factorial(1)
# # 1

# print(factorial(3))




# print numbers in reverse
a = [1,2,3]
n = len(a)
# a.reverse()
# for _  in a:
#     print(_)

print(f"n is {n}")

def reverse_print(n):
    """
        use recursion to reverse print 
        a list.
    """
    if n == 0:
        print(a[n])
        return 
    print(a[n])
    reverse_print(n -1)


reverse_print(n - 1)


# n =2
# 3

# n = 1






