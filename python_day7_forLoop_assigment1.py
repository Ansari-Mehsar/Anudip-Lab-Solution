# 1.Python program to check if the given string is a palindrome 

def is_palindrome(string):
    # Convert the string to lowercase to ignore case
    string = string.lower()
    
    # Remove spaces and non-alphanumeric characters from the string (optional)
    string = ''.join(char for char in string if char.isalnum())
    
    # Initialize flag as True
    is_palindrome = True
    
    # Loop through half of the string
    for i in range(len(string) // 2):
        # Compare characters from the start and the end
        if string[i] != string[-(i + 1)]:
            is_palindrome = False
            break
    
    return is_palindrome

# Input string
input_string = input("Enter a string: ")

# Check if the string is a palindrome
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")
    
#output
    
"""
Enter a string: mehsarashem
'mehsarashem' is a palindrome.

"""
