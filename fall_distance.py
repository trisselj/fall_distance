# Author: Jake Trissel
# Github Username: trisselj
# Date: 07/17/2024
# Description: Describes the distance an object falls toward Earth when given time

#Defining the function that we will use
def fall_distance(t):
    g = 9.8 #Acceleration due to gravity
    d = 0.5 * g * t**2 #Formula for calculating distance
    return d

#Initial input statement for time (Assuming people wont input error producing words)
t = int(input("Please enter the time that the object is falling for in seconds"))

#Final print statement telling them their fall distance
print(f"The distance fallen in {t} seconds is: {fall_distance(t)} meters")