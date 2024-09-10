#  2. Write a Python program to get the largest and smallest number from a list without builtin functions

def find_largest_and_smallest(numbers):
    """
    Returns the largest and smallest numbers from a list without using built-in functions.

    :param numbers: A list of numbers
    :return: A tuple with the largest and smallest numbers
    """
    if not numbers:
        raise ValueError("The list is empty.")
    
    # We set both largest and smallest to the first element of the list (numbers[0])
    # so that we have a starting point to compare other elements.

    largest = numbers[0]
    smallest = numbers[0]

    for number in numbers:
        if number > largest: # This checks if the current number in the list (number) is greater than the current value of largest.
            largest = number
        if number < smallest: # This checks if the current number in the list (number) is smaller than the current value of smallest.

            smallest = number

    return largest, smallest

# Example usage
my_list = [15, 42, 3, 99, 4, 18]
largest, smallest = find_largest_and_smallest(my_list)
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")

#output
"""
Largest number: 99
Smallest number: 3

"""
