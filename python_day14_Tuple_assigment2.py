# 2.Write a Python program to convert a list to a tuple.

# Input: listx = [5, 10, 7, 4, 15, 3] Output: (5, 10, 7, 4, 15, 3)

def list_to_tuple(listx):
  """Converts a list to a tuple.

  Args:
    listx: The input list.

  Returns:
    The converted tuple.
  """

  tuplex = tuple(listx)
  return tuplex

# Example usage:
listx = [5, 10, 7, 4, 15, 3]
tuplex = list_to_tuple(listx)

# printing the result

print(f"Output: {tuplex}")

#output
"""
Output: (5, 10, 7, 4, 15, 3)

"""
