# 2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

# define function
def get_integer_from_user():
    while True:
        try:
            user_input = float(input("Please enter an integer: "))
            print(f"You entered: {user_input}")
            break
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")

# Call the function
get_integer_from_user()

#Output

"""
Please enter an integer: xyz
Error: Invalid input. Please enter a valid integer.
Please enter an integer: 13
You entered: 13.0

"""
