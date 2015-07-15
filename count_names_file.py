def count_names_in_file(filename):

    """ Returns the number of names in a text file

    Arguments:
    an input filename

    Returns:
    the number of the names

    >>> count_names_in_file("names.txt")
    6
    
    """

    input_file = open('names.txt','r')
    contents = input_file.read()
    input_file.close()
    word_list = contents.split(',')
    return len(word_list)
