def distribution (filename, valid_grades):

    """ Prints a table of the distribution of grades

    Arguments:
    filename - an input filename
    valid_grades - a list of valid grades

    Returns:
    a table of the distribution of grades

    >>> distribution ('grades.txt', ['A', 'B', 'C', 'D', 'E', 'F'])
    3 students got A
    3 students got B
    2 students got C
    1 student got D
    2 students got F

    """

    input_file = open(filename, 'r')
    contents = input_file.read()
    input_file.close()
    grades = contents.split()
 
    count=[]
    for element in valid_grades:
        if element in grades:
            if grades.count(element)==1:
                print ("1 student got " + element)
            else:
                print (str(grades.count(element))+ " students got " + element)
            

