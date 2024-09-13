"""
2. Write a Python program to Return a set of elements present in Set A or B, but not both.

   Input: set1 = {10, 20, 30, 40, 50} set2 = {30, 40, 50, 60, 70} 

   Output: {20, 70, 10, 60}

"""

def symmetric_difference(set1, set2):
    """
    Returns the elements present in either set1 or set2 but not in both.

    Parameters:
    set1 (set): First set of items
    set2 (set): Second set of items

    Returns:
    set: Symmetric difference of set1 and set2
    """
    return set1 ^ set2  # The '^' operator is used to get the symmetric difference.

# Example input
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Output the result
result = symmetric_difference(set1, set2)

# printing the result
print(result)

#output
"""
{20, 70, 10, 60}

"""
