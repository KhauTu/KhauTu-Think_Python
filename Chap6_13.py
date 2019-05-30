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

def slope(x1, y1, x2, y2):
    while True:
        try:
            if x1 != x2:
                slope = (y1 - y2) / (x1 - x2)
            else:
                slope = "infinity"
            return slope
        except TypeError:
            # print("Oops! Wrong arguments!")
            return None

def intercept(x1, y1, x2, y2):
    while True:
        try:
            return y1 - slope(x1, y1, x2, y2) * x1
        except TypeError:
            # print("Oops! Wrong arguments!")
            return None

def test_suite():
    test(slope('a', 3, 4, 2) == None)
    # test(slope(5, 3, 4, 2) == 1.0
    test(slope(1, 2, 3, 2) == 0.0)
    test(slope(1, 2, 3, 3) == 0.5)
    test(slope(2, 4, 1, 2) == 2.0)
    test(intercept(1, 6, 3, 12) == 3.0)
    test(intercept(6, 1, 6, 6) == None)
    # test(intercept(6, 1, 1, 6) == 7.0)
    test(intercept(4, 6, 12, 8) == 5.0)


test_suite()