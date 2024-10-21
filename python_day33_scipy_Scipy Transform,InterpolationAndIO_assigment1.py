# Lab1: Write a python program using pandas Interpolation to fill in missing values in the data frame.

import pandas as pd

# Creating the DataFrame
df = pd.DataFrame({
    "Math": [12, 4, 7, None, 2],
    "English": [4, 3, 57, 3, None],
    "Hindi": [20, 16, None, 3, 8],
    "Science": [14, 3, None, None, 6]
})

# Interpolating missing values
df_interpolated = df.interpolate()

# Printing the DataFrame after interpolation
print("DataFrame after interpolation:\n", df_interpolated)

#Output
"""
DataFrame after interpolation:
    Math  English  Hindi  Science
0  12.0      4.0   20.0     14.0
1   4.0      3.0   16.0      3.0
2   7.0     57.0    9.5      4.0
3   4.5      3.0    3.0      5.0
4   2.0      3.0    8.0      6.0

"""
