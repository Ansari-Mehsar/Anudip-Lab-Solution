# 1. Using input() function take one number from the user and using
# ternary operators check whether the number is even or odd

# Taking input from the user
num = int(input("Enter a number: "))

# Using a ternary operator to check if the number is even or odd 
result = "Even" if num % 2 == 0 else "Odd"

#( % operator gives the remainder when num is divided by 2.If the remainder is 0, then num is divisible by 2, meaning it is an even number.)
#(If the remainder is not 0, then the num is not divisible by 2, meaning it is an odd number)

# Printing the result
print(f"The number {num} is {result}.")

#Output
"""
Enter a number: 12
The number 12 is Even.
"""
