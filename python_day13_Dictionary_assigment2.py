"""
2.Write a Python script to concatenate the following dictionaries to create a new one. 

Sample Dictionary : dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60} 

Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""

# Define the sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Create an empty dictionary to store the result
new_dict = {}

# Loop through each dictionary and update the new_dict
for d in (dic1, dic2, dic3):
    new_dict.update(d)

# printing the new dictionary
print(f"Expected Result : {new_dict}")

#output
"""
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

"""
