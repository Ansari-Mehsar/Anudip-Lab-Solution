#Task : 2.Write a Pandas program to split the following dataframe by school code and get mean, min, and max value of age for each school.
#Also generate a horizontal bar chart based on the result and explain the conclusion.

# Importing the pandas library for handling tabular data
import pandas as pd

# Importing matplotlib for creating visualizations like bar charts
import matplotlib.pyplot as plt  

# Input data: Creating a DataFrame with student information
student_data = pd.DataFrame({
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],  
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],  
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'age': [12, 12, 13, 13, 14, 12],  
    'height': [173, 192, 186, 167, 151, 159],  
    'weight': [35, 32, 33, 30, 31, 32],  
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']  
})

# Grouping data by 'school_code' and calculating the mean, minimum, and maximum of 'age'
age_stats = student_data.groupby('school_code')['age'].agg(['mean', 'min', 'max'])
# Explanation:
# - We group the data by 'school_code', meaning we will get separate statistics for each school.
# - The 'agg()' function allows us to calculate multiple statistics: 
#   - 'mean': the average age of students in each school
#   - 'min': the minimum age of students in each school
#   - 'max': the maximum age of students in each school

# Create a horizontal bar chart to display the statistics
age_stats.plot(kind='barh', figsize=(10, 6))  
plt.title('Age Statistics by School Code')  
plt.xlabel('Value')  
plt.ylabel('School Code')  
plt.grid(axis="x", linestyle="--", alpha=0.7)  
print(age_stats)
# Display the horizontal bar chart
plt.show()  

"""
OUTPUT  :
             mean  min  max
school_code                
s001         12.5   12   13
s002         13.0   12   14
s003         13.0   13   13
s004         12.0   12   12
"""
