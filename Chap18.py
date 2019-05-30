import turtle
import sys

def test(did_pass):
    """Print the result of the test."""
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def make_window(colr, ttle):
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w

def make_turtle(colr, sz):
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t


wn = make_window("lightgreen", "Tess and Alex dancing")
tess = make_turtle("hotpink", 2)


def koch(t, order, size):
    """
        Make turtle t draw a Koch fractal of ’order’ and ’size’.
        Leave the turtle facing the same direction.
    """

    if order == 0: # The base case is just a straight line
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order-1, size/3)
            t.left(angle)
        '''
        koch(t, order-1, size/3) # Go 1/3 of the way
        t.left(60)
        koch(t, order-1, size/3)
        t.right(120)
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)
        '''

def koch_10(t, order, size):
    """
        Make turtle t draw a Koch fractal of ’order’ and ’size’.
        Leave the turtle facing the same direction.
    """

    if order == 0: # The base case is just a straight line
        t.forward(size)
    else:
        for angle in [-85, 170, -85, 0]:
            koch_10(t, order-1, size/3)
            t.left(angle)

# koch_10(tess, 3, 500)

def flake(t, order, size):
    for i in range(3):
        koch(t, order, size)
        t.left(-120)

# flake(tess, 3, 100)

def flake_10(t, order, size):
    for i in range(4):
        koch_10(t, order, size)
        t.left(-90)

flake_10(tess, 4, 300)

def r_sum(nested_num_list):
    tot = 0
    for element in nested_num_list:
        if type(element) == type([]):
            tot += r_sum(element)
        else:
            tot += element
    return tot

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

def test_suite():
    test(r_max([2, 9, [1, 13], 8, 6]) == 13)
    test(r_max([2, [[100, 7], 90], [1, 13], 8, 6]) == 100)
    test(r_max([[[13, 7], 90], 2, [1, 100], 8, 6]) == 100)
    test(r_max(["joe", ["sam", "ben"]]) == "sam")

# test_suite()

turtle.mainloop()