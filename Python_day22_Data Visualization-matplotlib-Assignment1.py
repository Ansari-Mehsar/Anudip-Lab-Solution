"""Install matplotlib  & you can use plt.plot() to create a line plot of given data

x = [0, 5, 9, 10, 15, 20, 25] 

y = [0, 1, 2, 3, 4, 5, 6]"""


import matplotlib.pyplot as plt

# Data for plotting
x = [0, 5, 9, 10, 15, 20, 25]
y = [0, 1, 2, 3, 4, 5, 6]

# Create the plot
plt.plot(x, y, marker='o')

# Adding titles and labels
plt.title("Line Plot of X vs Y")
plt.xlabel("X values")
plt.ylabel("Y values")


# Display the plot
plt.show()
