# 1.Create a bar chart to represent monthly expenses in different spending categories and give your conclusion. 

import matplotlib.pyplot as plt

# Data
categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
expenses = [1200, 400, 200, 150, 250]


# Create the bar chart
plt.bar(categories, expenses, color='lightblue')

# Add labels and title
plt.xlabel('Spending Categories')
plt.ylabel('Expenses (Dollars)')
plt.title('Monthly Expenses')



# Show the plot
plt.show()
