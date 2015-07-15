""" Calculates amount of cups by a given quantity of liquid

"""

def number_of_cups (bottom_radius, top_radius, height, litres_of_liquid):

    """ Calculates a number of cups filled by a given quantity of liquid

    Arguments:
    bottom_radius - bottom radius of a truncated cone (float)
    top_radius - top radius of a truncated cone (float)
    height - height of a truncated cone (float)
    litres_of_liquid - given quantity of liquid in litres (int or float)

    Returns:
    A number of cups filled by a given quantity of liquid
 

    >>> number_of_cups (2,3,10,20)
    100
    >>> number_of_cups (2,3,10,15)
    75
    >>> number_of_cups(2,3,10,30)
    150

    """

    liquid = litres_of_liquid*1000    # Quantity of liquid is given in litres. To convert litres to cubic centimeters litres should bemultiple by 1000.
    number_of_cups = liquid/cone_volume(bottom_radius, top_radius, height)
    return int(number_of_cups)

    
