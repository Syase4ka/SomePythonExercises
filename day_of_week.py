def day_of_week (day, month, year):

    """ Returns the name of the day corresponding to a given date

    Arguments:
    day - the day (int)
    week - the week (int)
    year - the year (int)

    Returns:
    The name of the corresponding day (string)
    
    0 - Sunday
    1 - Monday etc

    >>> day_of_week(30,3,2014)
    'Sunday'
    >>> day_of_week(3,3,2014)
    'Monday'
    >>> day_of_week(1,1,2014)
    'Wednesday'

    """

    a = (14-month)//12

    y = year - a

    m = month + 12*a - 2

    d = (day + y + y//4 - y//100 + y//400 + (31*m)//12)%7

    return day_name(d)
