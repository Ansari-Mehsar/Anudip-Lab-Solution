#1.Compute the median of the flattened NumPy array 

#   Input: x_odd = np.array([1, 2, 3, 4, 5, 6, 7])

import numpy as np

# Input array
x_odd = np.array([1, 2, 3, 4, 5, 6, 7])

# Compute the median
median_value = np.median(x_odd)  #np.median() function, which directly calculates the median of an array.

# printing the reuslt
print(f"median: {median_value}")

#output
"""
median: 4.0

"""
