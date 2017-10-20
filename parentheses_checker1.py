import stack

        #########################################################
        #                                                       #
        # Program to check for balanced parentheses in file     #
        # passed as parameter.                                  #
        #                                                       #
        # __Time complexity: O(n)                               #
        # __Space complexity: O(n/2)                            #
        # __*where n is the length of file(str)                 #
        #                                                       #
        # Time of a python program execution for files used     #
        # as example:                                           #
        #                                                       #
        # stack.py          --- 0.002000093460083008 seconds ---#                    
        # bad_stack1.py     --- 0.0009999275207519531 seconds --#
        # bad_stack2.py     --- 0.021001338958740234 seconds ---#
        # bad_stack3.py     --- 0.021001338958740234 seconds ---#
        # bad_stack4.py     --- 0.0030002593994140625 seconds --#
        #                                                       #                        
        #########################################################

def parentheses_checker1(file):
    """
    Returns the phrase 'Well parenthesed' if each open parenthesis has
    the matching close one.
    In the opposite case, returns the phrase 'Bad parenthesed'.

    :param file: file ( .txt, .py, etc.)
    :return: 'Well parenthesed'/'Bad parenthesed'
    :rtype: str
    :UC: file is an external file
    :example:

    >>> parentheses_checker1('stack.py')
    'Well parenthesed'
    >>> parentheses_checker1('bad_stack1.py')
    'Bad parenthesed'
    >>> parentheses_checker1('bad_stack3.py')
    'Bad parenthesed'
    """
    with open(file) as f:
        strInput = f.read()
        if strInput:
            brackets = [ ('(',')'), ('[',']'), ('{','}')]
            kStart = 0
            kEnd = 1

            stck=stack.create()

            for char in strInput:
                for bracketPair in brackets:
                    if char == bracketPair[kStart]:
                        stck.append(char)
                    elif char == bracketPair[kEnd] and len(stck) > 0 and stck.pop() != bracketPair[kStart]:
                        return 'Bad parenthesed'

            if len(stck) == 0:
                return 'Well parenthesed'

        return 'Bad parenthesed'
