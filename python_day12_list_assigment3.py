# 3. Write a Python program to find duplicate values from a list and display those

def find_duplicates(numbers):
    """
    Returns a list of duplicate values from the input list.

    :param numbers: A list of numbers
    :return: A list of duplicate values
    """
    duplicates = [] # A list to store the duplicate numbers found in the list
    seen = set() # A set to track which numbers we've already encountered

    for number in numbers:
        if (number in seen and number not in duplicates):
            duplicates.append(number)
        else:
            seen.add(number)

    return duplicates

# Example usage
my_list = [4, 3, 7, 8, 3, 4, 6, 8, 2]
duplicates = find_duplicates(my_list)

#Printing the result
print(f"Duplicate values: {duplicates}")

#output
"""
Duplicate values: [3, 4, 8]

"""
