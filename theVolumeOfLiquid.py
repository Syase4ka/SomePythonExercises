
""" Calculates the volume of liquid held in a disposable cup
"""

import math

def cone_volume (bottom_radius, top_radius, height):

    """ Calculates the volume of liquid held in a disposable cup

    Arguments:
    bottom_radius - bottom radius of a truncated cone (float)
    top_radius - top radius of a truncated cone (float)
    height - height of a truncated cone (float)

    Returns:
    Volume of a truncated cone (float)

    Doctest is accurate to 2 decimal places
    
    >>> round (cone_volume(2,3,10),2)
    198.97
    >>> round (cone_volume(3,4,15),2)
    581.19
    >>> round (cone_volume(5,5,20),2)
    1570.8

    """

    volume = math.pi/3*height*(bottom_radius**2+bottom_radius*top_radius+top_radius**2)
    return volume


