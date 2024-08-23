#Python program to find the area of a triangle whose sides are given

import math

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return area
a = 3  
b = 5
c = 7
area = triangle_area(a, b, c)
print(f"The area of the triangle with sides {a}, {b}, and {c} is {area:.2f}")


#The area of the triangle with sides 3, 5, and 7 is 6.50

