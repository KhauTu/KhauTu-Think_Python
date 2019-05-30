import sys

def test(did_pass):
    """Print the result of the test."""
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def days_in_month(month):
    month28 = ['February']
    month30 = ['April', 'June','September','November']
    month31 = ['January', 'March', 'May', 'July', 'August', 'October', 'December']
    if month in month28:
        return 28
    elif month in month30:
        return 30
    elif month in month31:
        return 31
    else:
        return None

def test_suite():
    test(days_in_month("February") == 28)
    test(days_in_month("December") == 31)
    test(days_in_month("year") == None)

test_suite()
