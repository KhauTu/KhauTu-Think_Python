import sys

def test(did_pass):
    """Print the result of the test."""
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def turn_clockwise(par):
    lst = ['N','E','S','W']
    for i in range(len(lst)):
        if par == lst[i]:        
            return lst[i+1] if i < len(lst)-1 else lst[0]
        else: continue
    return None

def test_suite():
    test(turn_clockwise('N') == 'E')
    test(turn_clockwise('W') == 'N')
    test(turn_clockwise(42) == None)
    test(turn_clockwise('rubbish') == None)

test_suite()