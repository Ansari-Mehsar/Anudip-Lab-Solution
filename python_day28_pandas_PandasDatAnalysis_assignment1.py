#Task : 1Write a Pandas program to split the following data frame into groups based on Class and count the number of students in that particular class.
#Also generate a bar chart based on the result and explain the conclusion.

# Importing the pandas library to handle data in tabular format
import pandas as pd

# Importing matplotlib for creating visualizations like bar charts
import matplotlib.pyplot as plt  

# Input data: Creating a DataFrame with student information
student_data = pd.DataFrame({
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'VI', 'VI', 'VI', 'V', 'VI'],  
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 
    'age': [12, 12, 13, 13, 14, 12],  
    'height': [173, 192, 186, 167, 151, 159], 
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4'] 
})

class_counts = student_data['class'].value_counts()  
# Explanation: 
# 'value_counts()' counts how many times each unique value (class) appears in the 'class' column.
# We are counting the number of students in classes 'V' and 'VI'.

# Printing the number of students in each class
print("Number of students in each class :")
print(class_counts)
# Explanation:
# - This prints the result of the counting, showing how many students are in each class (V and VI).

# Create a bar chart to visualize the number of students in each class
plt.figure(figsize=(8,6))  
class_counts.plot(kind='bar', color='purple')  
plt.title('Number of Students in Each Class')  
plt.xlabel('Class')  
plt.ylabel('Number of Students')  
plt.xticks(rotation=0)  
plt.grid(axis="y", linestyle="--", alpha=0.5)  
plt.show()

"""
OUTPUT :
Number of students in each class :
class
VI    4
V     2
Name: count, dtype: int64
"""
