# 1. Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions.
# Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day). 

import numpy as np

# Input data
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2,-4,-12])

# Days (assuming day 1 corresponds to temperatures[0])
days = np.arange(1, len(temperatures) + 1)

# Identifying hot and cold days
hot_days = days[temperatures > 35]
cold_days = days[temperatures < 5]

hot_temps = temperatures[temperatures > 35]
cold_temps = temperatures[temperatures < 5]

# Displaying output as required
print("Hot Days:")
print("Day\tTemperature (°C)")
for day, temp in zip(hot_days, hot_temps):
    print(f"{day}\t{temp:.1f}")

print("\nCold Days:")
print("Day\tTemperature (°C)")
for day, temp in zip(cold_days, cold_temps):
    print(f"{day}\t{temp:.1f}")

#output
"""
Hot Days:
Day	Temperature (°C)
3	36.8
6	38.7
10	37.2

Cold Days:
Day	Temperature (°C)
11	-4.0
12	-12.0

"""

