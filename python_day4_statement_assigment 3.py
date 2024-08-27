# 3 Write a Python program that determines if a given year is a leap year or not.

# Program to check if a year is a leap year

# Input: Year
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Explanation:
# If a year is divisible by 4, it is a leap year.
# But if the year is divisible by 100, it is not a leap year, unless it is also divisible by 400.

#Output
"""
Enter a year: 2026
2026 is not a leap year.
"""
