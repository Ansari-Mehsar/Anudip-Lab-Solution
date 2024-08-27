# 4.Create a Python program that checks if a user-given number is positive, negative, or zero.

# Program to check if a number is positive, negative, or zero

# Input: Number
number = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#Output:
"""
Enter a number: -15
The number is negative.

"""
