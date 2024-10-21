# Lab2: Write a python program using Interpolation to fill in missing values in the data frame.
#       After that store the data frame into a MATLAB file using SciPy IO.Then display the contents from the MATLAB file. 

import pandas as pd
from scipy.io import savemat, loadmat

# Step 1: Create the DataFrame
df = pd.DataFrame({
    "Math": [12, 4, 7, None, 2],
    "English": [4, 3, 57, 3, None],
    "Hindi": [20, 16, None, 3, 8],
    "Science": [14, 3, None, None, 6]
})

# Step 2: Interpolating missing values
df_interpolated = df.interpolate()

# Step 3: Convert the DataFrame to a dictionary to store as a MATLAB file
data_dict = {col: df_interpolated[col].values for col in df_interpolated.columns}

# Save the DataFrame into a MATLAB (.mat) file
savemat('interpolated_data.mat', data_dict)

print("Data has been saved to 'interpolated_data.mat'")

# Step 4: Load the .mat file and display its contents
mat_contents = loadmat('interpolated_data.mat')

# Display the content of the MATLAB file
print("\nContent from the MATLAB file:")
for key, value in mat_contents.items():
    if not key.startswith("__"):  # Skip meta data
        print(f"{key}: {value}")

#Output
"""
Content from the MATLAB file:
Math: [[12.   4.   7.   4.5  2. ]]
English: [[ 4.  3. 57.  3.  3.]]
Hindi: [[20.  16.   9.5  3.   8. ]]
Science: [[14.  3.  4.  5.  6.]]

"""
