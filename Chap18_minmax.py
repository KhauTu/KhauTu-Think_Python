import sys

def test(did_pass):
    """Print the result of the test."""
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def r_max(nxs):
    """
    Find the maximum in a recursive structure of lists
    within other lists.
    Precondition: No lists or sublists are empty.
    """
    largest = None
    first_time = True
    for e in nxs:
        if type(e) == type([]):
            val = r_max(e)
        else:
            val = e

        if first_time or val > largest:
            largest = val
            first_time = False
    return largest

def recursive_min(nxs):
    """
    Find the minimum in a recursive structure of lists
    within other lists.
    Precondition: No lists or sublists are empty.
    """
    smallest = None
    first_time = True
    for e in nxs:
        if type(e) == type([]):
            val = recursive_min(e)
        else:
            val = e

        if first_time or val < smallest:
            smallest = val
            first_time = False
    return smallest

def test_suite():
    test(r_max([2, 9, [1, 13], 8, 6]) == 13)
    test(r_max([2, [[100, 7], 90], [1, 13], 8, 6]) == 100)
    test(r_max([[[13, 7], 90], 2, [1, 100], 8, 6]) == 100)
    test(r_max(["joe", ["sam", "ben"]]) == "sam")
    test(recursive_min([2, 9, [1, 13], 8, 6]) == 1)
    test(recursive_min([2, [[100, 1], 90], [10, 13], 8, 6]) == 1)
    test(recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]) == -7)
    test(recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6]) == -13)

test_suite()