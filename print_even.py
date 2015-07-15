def print_even(list):

    """ Prints all the even numbers from the list

    Arguments:
    list - a list of numbers (int)

    Returns:
    Even numbers from a list of numbers

    >>> print_even([1,25,36,4,5,96])
    36
    4
    96

    """

    
    for number in list:
        if number%2==0:
            print (number)
