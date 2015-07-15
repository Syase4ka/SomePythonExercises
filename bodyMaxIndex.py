""" Calculates the Body Mass Index based on the height and weight of a person.

"""



# weight_in_kilograms = 44.5
weight_in_kilograms = 84

height_in_metres = 1.82
# height_in_metres = 1.58



body_mass_index = weight_in_kilograms/height_in_metres**2





print ("My weight is: " + str(weight_in_kilograms) + " kg") # str() - built-in python function, which transform float to string format. It allows you to concatenate both values

print ("My height is: " + str(height_in_metres) + " m")

print ("My Body Mass Index is: " + str(body_mass_index))





"""

If you don't want to use the str() function you can use multiple prints instead:

print ("My weight is: ")

print (weight_in_kilograms)

print ("My height is: ")

print (height_in_metres)

...

etc.

"""

