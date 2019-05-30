import sys
import string

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

ss = "Python strings have some interesting methods."

def test_suite():
    test(find(ss, "s") == 7)
    test(find(ss, "s", 7) == 7)
    test(find(ss, "s", 8) == 13)
    test(find(ss, "s", 8, 13) == -1)
    test(find(ss, ".") == len(ss)-1)


def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct

my_story = """
2 Pythons are constrictors, which means that they will ’squeeze’ the life
3 out of their prey. They coil themselves around their prey and with
4 each breath the creature takes the snake will squeeze a little tighter
5 until they stop breathing completely. Once the heart stops the prey
6 is swallowed whole. The entire animal is digested in the snake’s
7 stomach except for fur or feathers. What do you think happens to the fur,
8 feathers, beaks, and eggshells? The ’extra stuff’ gets passed out as ---
9 you guessed it --- snake POOP! """

wds = remove_punctuation(my_story).split()
print(wds)