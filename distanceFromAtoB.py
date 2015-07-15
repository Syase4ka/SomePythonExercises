""" Calculates the distance from my home to the Clock Tower of
The University of Auckland.

"""

import math

earth_radius = 6371

# My home located at latitude -36.910513, longitude 174.752775
lat1 = math.radians(-36.910513)
long1 = math.radians(174.752775)

#The Clock Tower of The University of Auckland is located at latitude -36.849980, longitude 174.769498
lat2 = math.radians(-36.849980)
long2 = math.radians(174.769498)

distance = 2*earth_radius*math.asin(math.sqrt(
    math.sin((lat2-lat1)/2)**2+
    math.cos(lat1)*math.cos(lat2)*
    math.sin((long2-long1)/2)**2))

print (distance)


