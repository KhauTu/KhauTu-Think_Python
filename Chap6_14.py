import sys
import math

def test(did_pass):
    """Print the result of the test."""
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def is_even(n):
    while type(n) is int:
        try:
            return not bool(n % 2)
        except TypeError:
            # print("Oops! Wrong arguments!")
            return None

def is_odd(n):
    while type(n) is int:
        try:
            return bool(n % 2)
        except TypeError:
            # print("Oops! Wrong arguments!")
            return None

def test_suite():
    test(is_even(11) == False)
    test(is_even(0) == True)
    test(is_even(-1) == False)
    test(is_even('a') == None)
    test(is_odd(11) == (not False))
    test(is_odd(0) == (not True))
    test(is_odd(-1) == (not False))
    test(is_odd('a') == None)

test_suite()