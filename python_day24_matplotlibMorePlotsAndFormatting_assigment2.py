import numpy as np
import matplotlib.pyplot as plt

"""
2.Suppose you're a sales manager for an e-commerce company, and you want to create a figure with
subplots to compare the sales performance of different product categories over time. You have sales
data for four product categories: Electronics, Clothing, Home & Garden, and Sports & Outdoors. Share your conclusion/analysis. """

# Data
months = np.arange(1, 13)
electronics_sales = np.array([25000, 28000, 31000, 27000, 30000, 32000, 35000, 36000, 38000, 39000, 41000, 42000])
clothing_sales = np.array([15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000])
home_garden_sales = np.array([18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000])
sports_outdoors_sales = np.array([12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000])

# Create a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Creating bar plots for each category in subplots

# Subplot 1: Electronics Sales
axs[0, 0].plot(months, electronics_sales, marker="o", c='blue',label="Electronics Sales")
axs[0, 0].set_title('Electronics Sales')
axs[0, 0].set_xlabel('Months')
axs[0, 0].set_ylabel('Sales ($)')
axs[0, 0].grid(axis='y')
axs[0, 0].legend()
# Subplot 2: Clothing Sales
axs[0, 1].plot(months, clothing_sales,marker="o", c='green',label="Clothing Sales")
axs[0, 1].set_title('Clothing Sales')
axs[0, 1].set_xlabel('Months')
axs[0, 1].set_ylabel('Sales ($)')
axs[0, 1].grid(axis='y')
axs[0, 1].legend()
# Subplot 3: Home & Garden Sales
axs[1, 0].plot(months, home_garden_sales,marker="o", c='orange',label="Home & Garden Sales")
axs[1, 0].set_title('Home & Garden Sales')
axs[1, 0].set_xlabel('Months')
axs[1, 0].set_ylabel('Sales ($)')
axs[1, 0].grid(axis='y')
axs[1, 0].legend()
# Subplot 4: Sports & Outdoors Sales
axs[1, 1].plot(months, sports_outdoors_sales,marker="o", c='red',label="Sports & Outdoors Sales")
axs[1, 1].set_title('Sports & Outdoors Sales')
axs[1, 1].set_xlabel('Months')
axs[1, 1].set_ylabel('Sales ($)')
axs[1, 1].grid(axis='y')
axs[1, 1].legend()

# Adjust layout to prevent overlap

plt.tight_layout()
plt.show()

#conclusion/Analysis
"""
Electronics Sales:
The sales show a general upward trend over the 12-month period.
There is a noticeable dip around the 4th month, where sales drop from approximately 31,000 to 27,000.
After this dip, sales recover and continue to rise steadily, peaking at around 42,000 in the 12th month.

Clothing Sales:
Clothing sales display a consistent linear growth throughout the year.
Starting from 15,000 in the 1st month, the sales increase steadily each month, reaching 26,000 by the 12th month.
This category shows stable growth without any significant fluctuations.

Home & Garden Sales:
Similar to Clothing Sales, this category also shows a steady upward trend.
Starting at 18,000 in the 1st month, sales increase incrementally to around 29,000 in the 12th month.
This consistent growth suggests a stable market or effective sales strategies.

Sports & Outdoors Sales:
This category has the lowest starting point, beginning at 12,000.
Sales increase linearly throughout the year, reaching 23,000 by the 12th month.
Although the growth is consistent, it remains the lowest among the four categories. """
