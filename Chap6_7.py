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

def to_secs(h, m, s): # arguments: hours, minutes, seconds
    while True:
        try:
            return math.floor(60 * (m + h * 60) + s)
        except TypeError:
            # print("Oops! Wrong arguments!")
            return None

def hours_in(s): # arguments: seconds
    while True:
        try:
            return math.floor((s / 60) / 60)
        except TypeError:
            # print("Oops! Wrong arguments!")
            return None

def minutes_in(s): # arguments: seconds
    while True:
        try:
            return math.floor(s / 60 - hours_in(s) * 60)
        except TypeError:
            # print("Oops! Wrong arguments!")
            return None

def seconds_in(s): # arguments: seconds
    while True:
        try:
            return s - minutes_in(s) * 60 - hours_in(s) * 3600
        except TypeError:
            # print("Oops! Wrong arguments!")
            return None

def test_suite():
    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)
    test(to_secs(0, -10, 'a') == None)
    test(to_secs(2.5, 0, 10.71) == 9010)
    test(to_secs(2.433,0,0) == 8758)
    test(hours_in(9010) == 2)
    test(minutes_in(9010) == 30)
    test(seconds_in(9010) == 10)
    test(3 % 4 == 0)
    test(3 % 4 == 3)
    test(3 / 4 == 0)
    test(3 // 4 == 0)
    test(3+4 * 2 == 14)
    test(4-2+2 == 0)
    test(len("hello, world!") == 13)

test_suite()
