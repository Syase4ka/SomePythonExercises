def day_name (number):

    """ Returns the name of the day 

    Arguments:
    number - a number representing the day (int)

    Returns:
    The name of the day (string)

    0 - Sunday
    1 - MOnday etc

    >>> day_name (0)
    'Sunday'
    >>> day_name (4)
    'Thursday'
    >>> day_name(2)
    'Tuesday'
    
    """


    if number==0:
        return ("Sunday")
    elif number==1:
        return ("Monday")
    elif number==2:
        return ("Tuesday")
    elif number==3:
        return ("Wednesday")
    elif number==4:
        return ("Thursday")
    elif number==5:
        return ("Friday")
    elif number==6:
        return ("Saturday")
    else:
        print ("You've entered the wrong number")
                    
