import sys

def test(did_pass):
    """Print the result of the test."""
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def myreplace(old, new, s):
    """ Replace all occurrences of old with new in s. """
    return new.join(s.split(old))

def test_suite():
    test(myreplace(",", ";", "this, that, and some other thing") == 
    "this; that; and some other thing")
    test(myreplace(" ", "**","Words will now be separated by stars.") ==
    "Words**will**now**be**separated**by**stars.")

test_suite()