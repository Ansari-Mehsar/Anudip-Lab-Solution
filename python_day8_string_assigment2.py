# 2. Write a Python program to remove a newline in Python

# Given string
string = "\nBest \nDeeptech \nPython \nTraining\n"

#str.replace() method to replace newline characters with an empty string
cleaned_string = string.replace("\n", "")

# printing the result
print(cleaned_string)

#output
"""
Best Deeptech Python Training
"""
