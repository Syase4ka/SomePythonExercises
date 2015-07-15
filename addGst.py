def add_gst (list_of_prices):

    """ Calculates a new list of prices including GST

    Arguments:
    list_of_prices - list of prices excluding GST (float)

    Returns:
    A new list where each element of the original list has GST added (float)
    GST - 15%

    >>> add_gst([])
    []
    >>> add_gst([100])
    [115.0]
    >>> add_gst([100,200,350,712.23])
    [115.0, 230.0, 402.5, 819.06]

    """

    add_gst=[]
    for item in list_of_prices:
        list_with_gst = round(item*1.15,2)
        add_gst+=[list_with_gst]
    return add_gst
