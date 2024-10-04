# 2: Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels. 
#    Sample Python dictionary data and list labels: 

# importing pandas and numpy 
import pandas as pd
import numpy as np

# Sample dictionary data

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],

 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19], 

'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 

'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

# Creating DataFrame

df=pd.DataFrame(exam_data,index=(range(1,11)))

# printing the DataFrame
print(df)

#output
"""
         name  score  attempts qualify
1   Anastasia   12.5         1     yes
2        Dima    9.0         3      no
3   Katherine   16.5         2     yes
4       James    NaN         3      no
5       Emily    9.0         2      no
6     Michael   20.0         3     yes
7     Matthew   14.5         1     yes
8       Laura    NaN         1      no
9       Kevin    8.0         2      no
10      Jonas   19.0         1     yes
"""
