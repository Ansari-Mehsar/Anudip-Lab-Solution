"""
1. Write a Python program and calculate the mean of the below dictionary.

 test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4} 

Output: 6.2

"""


def calculate_mean(dictionary):
  """Calculates the mean of values in a dictionary.

  Args:
    dictionary: The dictionary containing key-value pairs.

  Returns:
    The mean of the values in the dictionary.
  """

  values = list(dictionary.values())
  total = sum(values)
  mean = total / len(values)
  return mean

# Example usage
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}
mean_value = calculate_mean(test_dict)

# priting the result

print("Mean:", mean_value)

#output
"""
Mean: 6.2

"""
