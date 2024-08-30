# 2. Python program to check if a given number is an Armstrong number

def know_armstrong(number):
    # Convert the number to a string to easily get the digits
    num_str = str(number)
    # Get the number of digits (power)
    num_digits = len(num_str)
    
    # Initialize the sum of powers
    sum_of_powers = 0
    
    # Loop through each digit in the number
    for digit in num_str:
        # Convert the digit back to an integer and raise it to the power of the number of digits
        sum_of_powers += int(digit) ** num_digits
    
    # Check if the sum of the powers is equal to the original number
    return sum_of_powers == number

# Input number
input_number = int(input("Enter a number: "))

# Check if the number is an Armstrong number
if know_armstrong(input_number):
    print(f"{input_number} is an Armstrong number.")
else:
    print(f"{input_number} is not an Armstrong number.")

#Output
"""
Enter a number: 153
153 is an Armstrong number.

 ===============
Enter a number: 145
145 is not an Armstrong number

"""
