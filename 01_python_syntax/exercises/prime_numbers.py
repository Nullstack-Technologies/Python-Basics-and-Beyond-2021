def check_prime(n):
    for i in range(2,n):
        if(n%i==0): return False
    return True

def print_prime_Inrange(l,u):
    if l<=0 or l>u:
        print("Invalid Input")
    else:
        for i in range(l,u+1):
            if check_prime(i):
                print(i, end=", ")

def print_prime_range(n):
    if n<=0:
        print("Invalid Input")
    else:
        i = 1
        count=0
        while count<n:
            if check_prime(i):
                print(i, end=", ")
                count+=1
            i+=1

# Driver Circuit

while True:
    try:
        print("1) See If a Number is Prime or not : ")
        print("2) Print All the Prime numbers in a range : ")
        print("3) Print a Certain Number of Prime Numbers : ")
        choice = int(input("Enter Choice : "))
        if(choice==1): 
            if check_prime(int(input("Enter The Testing Number : "))): print("It Is a Prime Number")
            else: print("It Is NOT a Prime Number")
        elif(choice==2):
            print_prime_Inrange(int(input("Enter The Lower Bound : ")),int(input("Enter The Upper Bound : ")))
        elif(choice==3):
            print_prime_range(int(input("Enter The Number of Prime Nos. : ")))
        else:
            print("Invalid Choice.\nTry a again.\n")
            continue
        break
    except:
        print("Give a Proper input.")
        continue

