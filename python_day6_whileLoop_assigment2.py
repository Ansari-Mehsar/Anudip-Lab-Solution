# 2. Write a python program finding the factorial of a given number using a while loop

def factorial(number):
    # Initialize result to 1 (factorial of 0 is 1)
    result = 1
    
    # Multiply result by each number from 1 to the given number
    while number > 0:
        result *= number
        number -= 1
    
    return result

# Input from the user
number = int(input("Enter a number: "))

# Ensure the input is a non-negative integer
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Calculate and print the factorial
    print(f"The factorial of {number} is {factorial(number)}.")

#output
"""
Enter a number: 4
The factorial of 4 is 24.

"""
