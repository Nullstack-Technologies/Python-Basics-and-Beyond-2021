# Function for nth Fibonacci number
def Fibonacci(n):
    if(n<=0):
        print("Invalid Input")
        raise Exception("Sorry, no numbers below zero")
    if n==1:
        print("0")
    elif n==2:
        print("0, 1")
    else:
        a = 0
        b = 1
        print(a, end=", ")
        n-=1
        while(n>0):
            print(a+b,end="")
            a,b = b,a+b
            n-=1
            if n != 0:
                print(end=", ")


# Driver Program

while True:
    try:
        limit = int(input("Enter The Limit : "))
        Fibonacci(limit)
        break
    except:
        print("Give a Proper input.")
        continue

