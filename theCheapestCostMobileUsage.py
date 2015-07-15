
""" Calculates the cheapest cost for mobile usage

"""

def plan_a (calls, txts, data):

    """ Calculates the cost of the plan A

    Arguments:
    calls - number of calls (int)
    texts - number of texts (int)
    data - number of MB of data used (float)

    >>> plan_a(100, 90, 120)
    104.0
    >>> plan_a(55, 101, 45)
    46.79
    >>> plan_a(200, 145, 1233)
    708.55
    
    Returns:
    Cost in dollars for the given usage on the Plan A (float)

    """
    
    calls_cost = calls*0.44 
    data_cost = data*0.5

    if txts <= 100:
        txts_cost = 0
    else:
        txts_cost= (txts-100)*0.09
    
    plan_a = calls_cost+txts_cost+data_cost
     
    
    return plan_a


def plan_b (calls, txts, data):

    """ Calculates the cost of the plan B

    Arguments:
    calls - number of calls (int)
    texts - number of texts (int)
    data - number of MB of data used (float)

    >>> plan_b(100,100,100)
    99.0
    >>> plan_b(50,150,1000)
    354.5
    >>> plan_b(34,156,678)
    251.26
    
    
    Returns:
    Cost in dollars for the given usage on the Plan B (float)

    """
    
    calls_cost = calls*0.49
    txts_cost = txts*0.2
    data_cost = data*0.3

    
    plan_b = calls_cost+txts_cost+data_cost

    
    return plan_b

def plan_c (calls, txts, data):

    """ Calculates the cost of the plan C

    Arguments:
    calls - number of calls (int)
    texts - number of texts (int)
    data - number of MB of data used (float)

    >>> plan_c(100,100,100)
    86.0
    >>> plan_c(100, 100, 5)
    41.0
    >>> plan_c(100,100,0)
    40.0
    
    Returns:
    Cost in dollars for the given usage on the Plan C (float)

    """
    
    calls_cost = calls*0.2
    txts_cost = txts*0.2

    if data <= 10:
        if data == 0:
            data_cost = 0
        else:
            data_cost = 1.0
    else:
        data_cost=(data-10)*0.5+1.0
    
    plan_c = calls_cost+txts_cost+data_cost
     
    
    return plan_c

def the_cheapest (calls, txts, data):

    """ Calculates the cheapest cost for mobile usage

    Arguments:
    calls - number of calls (int)
    texts - number of texts (int)
    data - number of MB of data used (float)


    >>> the_cheapest(100,100,100)
    86.0
    >>> the_cheapest(50, 90, 100)
    72.0
    >>> the_cheapest(100, 0, 5)
    21.0
    
    Returns:
    cost in dollars for the given usage on the cheapest plan (float)

    """

    a = plan_a(calls, txts, data)
    b = plan_b(calls, txts, data)
    c = plan_c(calls, txts, data)
    
    if a<b:
        if a<c:
            return a
        else:
            return c
    else:
        if b<c:
            return b
        else:
            return c

import doctest
doctest.testmod()
