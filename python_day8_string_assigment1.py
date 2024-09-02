#1. Write a Python program to count the occurrences of each word in a given sentence 


# Given string
string = "To change the overall look of your document. To change the look available in the gallery"

# Convert the string to lowercase and split it into words
words = string.lower().split()

# Create an empty dictionary to store word counts
word_count = {}

# Iterate through each word in the list
for word in words:
    # Remove any punctuation from the word (like periods, commas, etc.)
    word = word.strip(".!?,")
    
    # If the word is already in the dictionary, increment its count
    if word in word_count:
        word_count[word] += 1
    else:
        # If the word is not in the dictionary, add it with a count of 1
        word_count[word] = 1

# Print the word count dictionary
print(word_count)

#output
"""
{'to': 2, 'change': 2, 'the': 3, 'overall': 1, 'look': 2, 'of': 1, 'your': 1,
'document': 1, 'available': 1, 'in': 1, 'gallery': 1}

"""
