# 3. Write a Python program to reverse words in a string 

# Given string
string = "Deeptech Python Training"

# Split the string into a list of words
words = string.split()

# Reverse the list of words
reversed_words = words[::-1]


# Join the reversed list back into a string
reversed_string = ' '.join(reversed_words)

# printing the result
print(f"Original string: {string}")
print(f"reversed string: {reversed_string}")

# output
"""
Original string: Deeptech Python Training
reversed string: Training Python Deeptech

"""
