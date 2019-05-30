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

def hypotenuse(a,b):
    while a > 0 and b > 0:
        try:
            return math.sqrt(a**2 + b**2)
        except TypeError:
            # print("Oops! Wrong arguments!")
            return None

def test_suite():
    test(hypotenuse(-3, 4) == None)
    test(hypotenuse(12, 5) == 13.0)
    test(hypotenuse(24, 7) == 25.0)
    test(hypotenuse(9, 12) == 15.0)

test_suite()