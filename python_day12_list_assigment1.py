# 1. Write a Python program to sum all the items in a list.

def sum_of_list(numbers):
    """
    Returns the sum of all the items in a list.

    :param numbers: A list of numbers
    :return: Sum of the numbers in the list
    """
    total = 0
    for number in numbers:
        total += number
    return total

# Example usage:
my_list = [10, 20, 30, 40]
total = sum_of_list(my_list)

#Printing the result:
print(f"The sum of the list is: {total}")

#output:
"""
The sum of the list is: 100

"""


