def average_from_file (filename):

    """ Returns the average mark from a file with unspecified number of scores

    Arguments:
    filename - an input filename

    Returns:
    The average score - (float)

    >>> average_from_file ('marks.txt')
    47.5

    """

    input_file = open (filename, 'r')
    contents = input_file.read()
    input_file.close()
    numbers = contents.split()
    sum = 0
    for element in numbers:
        sum+=int(element)
    average = sum/len(numbers)
    return round (average, 1)
