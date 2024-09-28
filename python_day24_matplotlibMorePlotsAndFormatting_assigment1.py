#1. Create a pie chart to visualize the distribution of your monthly income by source.
#   You have collected data on the various sources of your income, such as salary, freelance
#   work, investments, and rental income. Share your conclusion/analysis.

import matplotlib.pyplot as plt

# market share data
income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
monthly_income = [5000, 1500, 1000, 600, 400]

# colours each slice
colors=['lightblue', 'lightcoral', 'lightgreen', 'lightpink', 'lightgrey']

# create a pie chart
plt.pie(monthly_income, labels=income_sources, autopct='%1.1f%%',startangle=140,  colors=plt.cm.Paired.colors)

# title
plt.title('Monthly Income Distribution by Source')

# show the pie chart
plt.show()

#conclusion and analysis
"""
Salary (58.8%):
The largest portion of the income comes from the Salary source, contributing 58.8% of the total monthly income.
This indicates a strong reliance on a stable salary income compared to other sources.

Freelance (17.6%):
Freelance work contributes 17.6% to the monthly income.
While significantly less than Salary, it still represents a substantial secondary income stream, suggesting an active engagement in freelance opportunities.

Investments (11.8%):
Investments contribute 11.8% to the overall income.
This portion shows that there is some passive income being generated, likely from stocks, bonds, or other investment vehicles, but it's still smaller compared to the primary income sources.

Rental (7.1%):
Rental income accounts for 7.1% of the total income.
This indicates a source of passive income, likely from property rentals, contributing a modest portion of the total income.

Other (4.7%):
The smallest portion of the income comes from the 'Other' category, contributing 4.7%.
This category may include miscellaneous income sources like part-time work, gifts, or small business profits.
"""
