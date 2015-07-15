def unique_list (list):

    """ Returns unique values in a list

    Arguments:
    list - a list of strings

    Returns:
    A list which contains unique strings

    >>> unique_list (['cat', 'dog', 'cat', 'bug', 'ant', 'dog', 'bug'])
    ['cat', 'dog', 'bug', 'ant']

    >>> unique_list (['Welcome', 'to', 'COMPSCI101', 'To'])
    ['Welcome', 'to', 'COMPSCI101', 'To']

    """

    new_list = []
    for element in list:
        if element not in new_list:
            new_list.append(element)
    print (new_list)

