# 1. Write a Python program to find the number of times 4 appears in the tuple. 

#  Input: tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7 ) Output: 3 

def count_occurrences(tuple, element):
  """Counts the number of occurrences of an element in a tuple.

  Args:
    tuple: The input tuple.
    element: The element to count.

  Returns:
    The number of occurrences of the element in the tuple.
  """

  count = 0
  for item in tuple:
    if item == element:
      count += 1
  return count

# Example usage:
tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7)
element = 4
occurrences = count_occurrences(tuplex, element)
# printing the result
print("Number of occurrences of", element, ":", occurrences)

#output
"""
Number of occurrences of 4 : 3

"""
