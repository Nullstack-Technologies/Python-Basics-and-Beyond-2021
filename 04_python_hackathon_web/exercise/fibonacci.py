"""
    Print the first n Fibonacci Numbers
    Fibonacci Series -> 0,1,1,2,3....
"""

def fibonacci_normal(n):
    """
        Compute the first n fibonacci numbers
    """
    n1, n2, = 0, 1

    for i in range(n):
        print(n1)
        temp = n1 + n2
        n1 = n2
        n2 = temp


def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


n = int(input("How many fibonacci numbers do you need? "))
# fibonacci_normal(n)

for i in range(n):
    print(fibonacci_recursive(i))


# 0, 1 ,2 ,3 ,4 , 5 
# 0 > if "0 is printed"
# 1 > if "1 is printed"
# 2 > else fibo(1) + fibo(0) > 1 + 0 > "1 is printed"
# 3 > else fibo(2) + fibo(1) > 1 + 1 > "2 is printed"
#..

