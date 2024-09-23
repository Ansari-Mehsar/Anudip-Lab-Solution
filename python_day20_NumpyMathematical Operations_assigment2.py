# 2. Calculate the profit made by a company

import numpy as np

# Input arrays for revenue and expenses
revenue = np.array([10000, 12000, 11000, 10500])
expenses = np.array([4000, 5000, 4500, 4800])

# Calculate profit
profit = revenue - expenses  # Subtract the expenses from the revenue to calculate the profit.

# printing the result
print("Profit:", profit)

#output
"""
Profit: [6000 7000 6500 5700]

"""
