# 1. Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.

#creating function by using def

def div(a, b):
    # Check if the denominator is not zero to avoid division by zero error
    if b != 0:
        return f"Division is {a / b}"
    else:
        return "Division by zero is not allowed."

# Calling the function

result=div(81,9)
print(result)

#Output
"""
Division is 9.0

"""

