# 1.Write a python program to check whether a number is palindrome or not?

def know_palindrome(number):
    # Convert the number to string to easily compare digits
    num_str = str(number)
    
    # Compare the string with its reverse
    return num_str == num_str[::-1]

# Input from the user
number = int(input("Enter a number: "))

# Check if the number is palindrome
if know_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
    
#Output
"""
Enter a number: 738575837
738575837 is a palindrome.

"""
