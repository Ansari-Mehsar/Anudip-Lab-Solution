# 2: Suppose you want to track and analyze your household expenses for a month.
#    You have recorded the expenses for various categories, such as groceries, utilities,
#    rent, transportation, and entertainment. You can represent this expense data using a Pandas Series. 

import pandas as pd

# Input data
categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']
expenses = [500, 200, 1200, 300, 150]

# Creating a Pandas Series
expenses_series = pd.Series(expenses, index=categories, name="household expenses")

# Display the Series
print(expenses_series)

#output
"""
Groceries          500
Utilities          200
Rent              1200
Transportation     300
Entertainment      150
Name: household expenses, dtype: int64

"""
