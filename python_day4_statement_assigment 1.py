#1. Write a Python program that takes a number as input and prints
#   "Even" if the number is even and "Odd" if it's odd

# Program to check if a number is even or odd

# Input: Number
number = int(input("Enter a number: "))

# Check if the number is even or odd by using if else statement
# The % operator gives the remainder when num is divided by 2.
# If the remainder is 0, then num is divisible by 2, meaning it is an even number.
# If the remainder is not 0, then num is not divisible by 2, meaning it is an odd number.

if number % 2 == 0:
    print(f"{number} is Even number")
else:
    print(f"{number} is Odd number")
    
#Output:
"""
Enter a number: 13
13 is Odd number

"""
    
