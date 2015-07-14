def compound_interest (principal, interest_rate, term):

    """ Calculates the compound interest on an investment

    Arguments:
    principal - the initial amount (int or float)
    interst_rate - the interest rate (float)
    term - the number of years of the investment (float)

    Returns:
    The final value of that investment rounded to the nearest dollar value

    >>> compound_interest (100,3,20)
    181
    >>> compound_interest (200,5,15)
    416
    >>> compound_interest (300,6,30)
    1723

    """

    compound_interest = principal*(1+interest_rate/100)**term
    return round (compound_interest)

import doctest
doctest.testmod()

