# 2 Create a Python program that checks whether a person is
# eligible to vote (18 years or older) based on their age.

# Program to check voting eligibility

# Input: Age of the person
age = int(input("Enter your age: "))

# Check if the person is 18 years or older
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#Output
"""
Enter your age: 23
You are eligible to vote.
"""
