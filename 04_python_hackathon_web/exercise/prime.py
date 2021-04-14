"""
    Check if a number is prime or not
"""

n = int(input("Provide the Number "))


def is_prime(n):
    for _ in range(2, n // 2):
        if n % _ == 0:
            return False
    return True


if is_prime(n):
    print("It is a prime number!")
else:
    print("Not a prime number!")


# 10 is prime?
# 2 to 5
# 2, 3, 4 ,5 