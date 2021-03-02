"""
    Simple Interest Calculator

    This Program calculates the Simple Interest
    Author:
    Date:
"""


principle = float(input('Enter the principle: '))
rate_of_interest = float(input('Enter the Rate of Interest: '))
time = float(input('Enter the time: '))


# Calculating the Simple interest using the 
# parameters passed
simple_interest = principle * rate_of_interest / 100 * time

amount = principle + simple_interest

print(f"Simple Interest is {simple_interest}")
print(f"Ammount is {amount}")


