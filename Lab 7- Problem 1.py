#Name- Alexander Koschnitzki
#Date- 11-11-21

#Problem 1

#In this problem, it is able to use a function to be able to
#find the area of any circle. You can input any number and it can
#be able to find it.


import math

def areaOfCircle(r):

    area_of_circle = math.pi * r * r
    return area_of_circle

radius = 5
print("Area", areaOfCircle(radius))