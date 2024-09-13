"""
1. Write a Python program to Get Only unique items from two sets. 

   Input: set1 = {10, 20, 30, 40, 50} set2 = {30, 40, 50, 60, 70} 

   Output: {70, 40, 10, 50, 20, 60, 30}
"""


def get_unique_items(set1, set2):
    """
    Returns the unique items from two sets.

    Parameters:
    set1 (set): First set of items
    set2 (set): Second set of items

    Returns:
    set: Unique items from both sets
    """
    return set1 | set2  # The '|' operator is used to get the union of both sets.

# Example input
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Output the result
result = get_unique_items(set1, set2)

# printing the result

print(result)

# output
"""
{70, 40, 10, 50, 20, 60, 30}

"""

