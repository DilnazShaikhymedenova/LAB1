import math #imports the math function and constant pi

def volumeOfSphere(radius):
    return (4/3) * math.pi * pow(radius, 3) 

radius = int(input()) #enter the radius of the sphere
Volume = volumeOfSphere(radius)
print(Volume)

#math.pi - from math function, constant number