import stack

        #########################################################
        #                                                       #
        # Program to check for balanced parentheses in file     #
        # passed as parameter and return line, col., and        #                          
        # phase containing unbalanced parentheses.              #
        #                                                       #
        # __Time complexity: O(n)                               #
        # __Space complexity: O(n/2)                            #
        # __*where n is the length of file(str)                 #
        #                                                       #
        # Time of a python program execution for files used     #
        # as example:                                           #
        #                                                       #
        # stack.py          --- 0.0009999275207519531 seconds --#                    
        # bad_stack1.py     --- 0.016000986099243164 seconds ---#
        # bad_stack2.py     --- 0.009000539779663086 seconds ---#
        # bad_stack3.py     --- 0.01000070571899414 seconds --- #
        # bad_stack4.py     --- 0.011000394821166992 seconds ---#
        #                                                       #                        
        #########################################################

class ParenthesisError(Exception):
    # there's no need to use this class as exception is this case
    # because there's no racing errors
    # but in case of errors usage all 'print's in this file
    # should be replaced with 'raise'
    def __init__(self, parenthesis, error):
        what_is_wrong = '%s at line %s, char number %s, the problem is >>> %s'
        parenthesis.line = parenthesis.line.replace('\n', '\\n')
        self.what_is_wrong = what_is_wrong % (error ,parenthesis.i_line-1, parenthesis.i_char-1, parenthesis.line)
 
    def __str__(self):
        return self.what_is_wrong
 
 
class Parenthesis:
    def __init__(self, i_line, line, i_char):
        self.i_line = i_line
        self.line = line
        self.i_char = i_char
 
 
def parentheses_checker2(filename):
    """
    Returns the line, char number and phase containing unbalanced
    parentheses is there's parenthesis problem.
    In the opposite case, returns nothing.

    :param file: file ( .txt, .py, etc.)
    :return: None or line, char number and phase
    :rtype: str or None
    :UC: file is an external file
    :example:

    >>> parentheses_checker2('stack.py')
    >>> parentheses_checker2('bad_stack2.py')
    Wrong open parenthesis at line 80, char number 13, the problem is: >>> def is_empty (s:\n
    >>> parentheses_checker2('bad_stack3.py')
    Wrong open parenthesis at line 10, char number 2, the problem is: >>> A [ module for stack data structure.\n
    """
    par_open = {'(':[], '[':[], '{':[]}
    par_close = {')':'(', ']':'[', '}':'{'}
    
    with open(filename) as f:
        for i_line, line in enumerate(f, start=1):
            for i_char, char in enumerate(line, start=1):
                if char in par_open:
                    par_open[char].append(Parenthesis(i_line=i_line, line=line, i_char=i_char))
                elif char in par_close:
                    try:
                        par_open[par_close[char]].pop()
                    except IndexError:
                        print(ParenthesisError(Parenthesis(i_line=i_line, line=line, i_char=i_char), 'Wrong closed parenthesis '))
    
    for _, l in par_open.items():
        for parenthesis in l:
            print(ParenthesisError(parenthesis, 'Wrong open parenthesis'))
