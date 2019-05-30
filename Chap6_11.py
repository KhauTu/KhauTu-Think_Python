import sys

def test(did_pass):
    """Print the result of the test."""
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def compare(a,b):
    while True:
        try:
            if a > b:
                return 1
            elif a == b:
                return 0
            else:
                return -1
        except TypeError:
            # print("Oops! Wrong arguments!")
            return None

def test_suite():
    test(compare(1, 'aA') == None)
    test(compare(7, 7) == 0)
    test(compare(2, 3) == -1)
    test(compare(42, 1) == 1)

test_suite()
