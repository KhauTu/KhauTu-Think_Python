import sys

def test(did_pass):
    """Print the result of the test."""
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def find(strng, ch, start=0, end=None):
    ix = start
    if end is None:
        end = len(strng)
    while ix < end:
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1

def count_letter2(strng, ch):
    count = 0
    i = 0
    while find(strng, ch, start = i) != - 1:
        i = find(strng, ch, start = i) + 1
        count += 1
    return count

def remove_letter(ch, strng):
    i = 0
    while find(strng, ch, start = i) != - 1:
        i = find(strng, ch, start = i)
        strng = strng[:i] + strng[i+1:]
        i += 1
    return strng

def reverse(strng):
    reverse = ""
    for i in range(len(strng)):
       reverse += strng[len(strng) - 1 - i]
    return reverse

def is_palindrome(strng):
    return strng == reverse(strng)

def test_suite():
    test(remove_letter("a", "apple") == "pple")
    test(remove_letter("a", "banana") == "bnn")
    test(remove_letter("z", "banana") == "banana")
    test(remove_letter("i", "Mississippi") == "Msssspp")
    test(remove_letter("b", "") == "")
    test(remove_letter("b", "c") == "c")
    test(is_palindrome("abba"))
    test(not is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(not is_palindrome("banana"))
    test(is_palindrome("straw warts"))
    test(is_palindrome("a"))
    test(is_palindrome(""))

test_suite()
# strng = "banana"
# print(strng[:1] + strng[2:])

        