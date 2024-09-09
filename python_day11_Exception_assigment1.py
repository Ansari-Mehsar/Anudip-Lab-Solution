# 1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

# define function 
def devide_number():
    while True:    
        try:
            first_input=float(input("Enter the dividend: "))
            second_input=float(input("Enter the divisor: "))
            result=first_input/second_input
            print(f"The result of {first_input} divided by {second_input} is {result}")
            break
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")

# test function
devide_number()

# output
"""
Enter the dividend: 12
Enter the divisor: 0
Error: Cannot divide by zero!
Enter the dividend: 14
Enter the divisor: 7
The result of 14.0 divided by 7.0 is 2.0

"""
