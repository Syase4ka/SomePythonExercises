def replace_text (filename, old_string, new_string):


    """ Replaces all occurences of old strings in a file with the new strings

    Arguments:
    filename - an input filename
    old_string
    new_string

    Returns:
    The list where all old strings replaces by the new strings

    >>> replace_text ('words.txt', 'go', 'think')
    The woods are lovely dark and deep
    But I have promises to keep
    And miles to think before I sleep
    And miles to think before I sleep
    

    """

    input_file = open(filename, 'r')
    contents = input_file.read()
    input_file.close()
    new_contents = contents.replace(old_string, new_string)

    print (new_contents)
