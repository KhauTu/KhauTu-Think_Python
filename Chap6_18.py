import sys

def test(did_pass):
    """Print the result of the test."""
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def f2c(t):
    while type(t) is int or float:
        try:
            return round((t-32) * 5 / 9)
        except TypeError:
            # print("Oops! Wrong arguments!")
            return None

def c2f(t):
    while type(t) is int or float:
        try:
            return round(t * 9 / 5 + 32)
        except TypeError:
            # print("Oops! Wrong arguments!")
            return None

def test_suite():
    test(f2c(212) == 100) # Boiling point of water
    test(f2c(32) == 0) # Freezing point of water
    test(f2c(-40) == -40) # Wow, what an interesting case!
    test(f2c(36) == 2)
    test(f2c(37) == 3)
    test(f2c(38) == 3)
    test(f2c(39) == 4)
    print('*' * 20)
    test(c2f(0) == 32)
    test(c2f(100) == 212)
    test(c2f(-40) == -40)
    test(c2f(12) == 54)
    test(c2f(18) == 64)
    test(c2f(-48) == -54)

test_suite()
