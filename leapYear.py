def leap_year (year):

    """ Determines if a given year is a leap year

    Arguments:
    year - a posotive integer number representing a year

    Returns:
    True - if the number is a leap year
    False - otherwise

    >>> leap_year(2004)
    True
    >>> leap_year(2100)
    False
    >>> leap_year(2000)
    True
    >>> leap_year(2001)
    False

    """

    if year % 400 ==0:
        return True
    elif year % 100 ==0:
        return False
    elif year % 4==0:
        return True
    else:
        return False
