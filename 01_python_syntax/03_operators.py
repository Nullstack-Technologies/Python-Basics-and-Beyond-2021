"""
    OPERATORS

    Operators are used to perform operations on variables and values.

    1) ARITHMETIC OPERATORS

    +	Addition	x + y	
    -	Subtraction	x - y	
    *	Multiplication	x * y	
    /	Division	x / y	
    %	Modulus	x % y	
    **	Exponentiation	x ** y	
    //	Floor division	x // y


    2) Logical Operators

    ==	Equal	x == y	
    !=	Not equal	x != y	
    >	Greater than	x > y	
    <	Less than	x < y	
    >=	Greater than or equal to	x >= y	
    <=	Less than or equal to	x <= y

    3) Identity Operators

    is 	Returns True if both variables are the same object	x is y	
    is not	Returns True if both variables are not the same object	x is not y

    4) Membership Operators

    in 	Returns True if a sequence with the specified value is present in the object	x in y	
    not in	Returns True if a sequence with the specified value is not present in the object	x not in y

    5) Bitwise Operators

    & 	AND	Sets each bit to 1 if both bits are 1
    |	OR	Sets each bit to 1 if one of two bits is 1
    ^	XOR	Sets each bit to 1 if only one of two bits is 1
    ~ 	NOT	Inverts all the bits
    <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
    >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off


"""

x = 1
y = 2

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)


print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)


print(x is y)
print(x is not y)

