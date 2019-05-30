import sys

def test(did_pass):
    """Print the result of the test."""
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def count(target, nxs):
    """
    returns the number of occurrences of target in a nested list.
    """
    n = 0
    for e in nxs:
        if type(e) == type([]):
            n += count(target, e)
        else:
            if target == e:
                n += 1
    return n

def flatten(nxs):
    """
    returns a simple list containing all the values in a nested list.
    """
    lst = []
    for e in nxs:
        if type(e) == type([]) or type(e) == type(()): # Check type of e is list or tuple
            for e2 in flatten(e):
                lst.append(e2)
        else:
            lst.append(e)
    return lst

def test_suite():
    test(count(2, []) == 0)
    test(count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]) == 4)
    test(count(7, [[9, [7, 1, 13, 2], 8], [7, 6]]) == 2)
    test(count(15, [[9, [7, 1, 13, 2], 8], [2, 6]]) == 0)
    test(count(5, [[5, [5, [1, 5], 5], 5], [5, 6]]) == 6)
    test(count("a", [["this",["a",["thing","a"],"a"],"is"], ["a","easy"]]) == 4)
    test(flatten([2,9,[2,1,13,2],8,[2,6]]) == [2,9,2,1,13,2,8,2,6])
    test(flatten([[9,[7,1,13,2],8],[7,6]]) == [9,7,1,13,2,8,7,6])
    test(flatten([[9,(7,1,13,2),8],[2,6]]) == [9,7,1,13,2,8,2,6])
    test(flatten([["this",["a",["thing"],"a"],"is"],["a","easy"]]) == ["this","a","thing","a","is","a","easy"])
    test(flatten([]) == [])

test_suite()