def binary_to_decimal (binary_list):

    """ Converts a list of binary digits into a decimal number

    Arguments:
    binary_list = list that consists of only 1's and 0's

    Returns:
    a decimal number (int)

    >>> binary_to_decimal([1,0,0,1,1,0])
    38
    >>> binary_to_decimal([1,1,0,0,1])
    25

    """

    sum = 0
    place_value = 1
    for i in reverse_list(binary_list):
        product = i*place_value
        sum+=product
        place_value = place_value*2
    return sum
