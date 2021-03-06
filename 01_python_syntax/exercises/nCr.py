"""
    Use Functions to Calculate the Factorial of a number
"""


def factorial(n):
    """
        This Function computes the factorial of a number.
        3! = 3 * 2 *1 = 6
        input: integer
        outputs: factorial of it
    """
    fact = 1

    # looping over n then multiplying by factorial 
    # and decrementing it by 1
    # while n > 1:
    #     print(n, fact)
    #     fact *= n
    #     n -= 1

    # while True:
    #     fact *= n
    #     n -= 1 
    #     if n == 1:
    #         break 

    for i in range(1, n + 1):
        fact *= i

    return fact


# nCr (Combination)
# nCr = n!/((n-r)!* r!)
# 8C2

def nCr(n, r):
    """
        Calculates the nCr of given values
    """
    result = factorial(n)/(factorial(n - r) * factorial(r))
    return result

number_of_matches = nCr(8, 2)
print(number_of_matches)

