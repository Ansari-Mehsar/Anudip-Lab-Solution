# 1: Write a Pandas program to create a dataframe from a dictionary and display it.Sample data:

# importing pandas
import pandas as pd

# Sample dictionary data

score={
    'Math':[78,85,96,80,86],
    'English':[84,94,89,83,86],
    'Hindi':[86,97,96,72,83]
}
# Creating DataFrame
df=pd.DataFrame(score, index=(range(1,6)))

# printig the Data Frame
print(df)

#output
"""

    Math  English  Hindi
1    78       84     86
2    85       94     97
3    96       89     96
4    80       83     72
5    86       86     83
"""

