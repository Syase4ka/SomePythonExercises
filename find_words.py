def find_words(character,filename):

    """ Prints all words in the file which contain the specified character

    Arguments:
    character - string
    filename - input filename

    Returns:
    prints all words in the file which contain the specified character

    >>> find_words("n", "names.txt")
    andrew
    ann
    angela
    >>> find_words("e", "names.txt")
    andrew
    peter
    angela

    """

    input_file = open('names.txt','r')
    contents = input_file.read()
    input_file.close()
    word_list = contents.split(',')
    for word in word_list:
        if character in word:
            print (word)
