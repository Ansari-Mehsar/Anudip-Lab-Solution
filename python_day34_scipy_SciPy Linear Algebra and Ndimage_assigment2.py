# Lab2: Using SciPy Linear Algebra please solve the below problem. Input: 7x + 2y = 8 4x + 5y = 10

import numpy as np
from scipy.linalg import solve

# Define the coefficient matrix A and the constant matrix B
A = np.array([[7, 2], [4, 5]])  # Coefficients of x and y
B = np.array([8, 10])           # Constants on the right-hand side

# Use scipy.linalg.solve to solve for x and y
solution = solve(A, B)

# Display the solution
x, y = solution
print(f"Solution: x = {x}, y = {y}")

#Output
"""
Solution: x = 0.7407407407407407, y = 1.4074074074074074

"""
