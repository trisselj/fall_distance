# Author: Jake Trissel
# Github Username: trisselj
# Date: 07/17/2024
# Description: Describes the distance an object falls toward Earth when given time

#Defining the function that we will use 
def fall_distance(t):
    g = 9.8 #Acceleration due to gravity
    d = 0.5 * g * t**2 #Formula for calculating distance
    return d