# import urllib.request

'''
url = "http://www.ict.ru.ac.za/Resources/ThinkSharply/ThinkSharply/_downloads/alice_in_wonderland.txt"
alice_in_wonderland = "alice_in_wonderland.txt"

urllib.request.urlretrieve(url, alice_in_wonderland)
'''

# url = "http://www.ict.ru.ac.za/Resources/ThinkSharply/ThinkSharply/_downloads/vocab.txt"
# vocab = "vocab.txt"

# urllib.request.urlretrieve(url, vocab)

import sys
import time

from Chap14_BinarySearch import *

def test(did_pass):
    """Print the result of the test."""
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def search_linear(xs, target):
    """ Find and return the index of target in sequence xs """
    for (i, v) in enumerate(xs):
        if v == target:
            return i
    return -1

def find_unknown_words(vocab, wds):
    """ Return a list of words in wds that do not occur in vocab """
    result = []
    for w in wds:
        if (search_binary(vocab, w) < 0):
        # if (search_linear(vocab, w) < 0):
            result.append(w)
    return result

def load_words_from_file(filename):
    """ Read words from filename, return list of words. """
    f = open(filename, "r")
    file_content = f.read()
    f.close()
    wds = file_content.split()
    return wds

bigger_vocab = load_words_from_file("vocab.txt")

# print("There are {0} words in the vocab, starting with\n {1} ".format(len(bigger_vocab), bigger_vocab[:6]))

def text_to_words(the_text):
    """ return a list of words with all punctuation removed,
    and all in lowercase.
    """
    my_substitutions = the_text.maketrans(
        # If you find any of these
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_'‘{|}~’\\;\r\n",
        # Replace them by these
        "abcdefghijklmnopqrstuvwxyz                                              ")

        # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds

def get_words_in_book(filename):
    """ Read a book from filename, and return a list of its words. """
    f = open(filename, "r")
    content = f.read()
    f.close()
    wds = text_to_words(content)
    return wds

book_words = get_words_in_book("alice_in_wonderland.txt")
# print("There are {0} words in the book, the first 100 are\n{1}".format(len(book_words), book_words[:100]))

t0 = time.perf_counter()
missing_words = find_unknown_words(bigger_vocab, book_words)
t1 = time.perf_counter()

# print("There are {0} unknown words.".format(len(missing_words)))
# print("That took {0:.4f} seconds.".format(t1-t0))

vocab = ["apple", "boy", "dog", "down", "fell", "girl", "grass", "the", "tree"]
book_words = "the apple fell from the tree to the grass".split()

def test_suite():
    test(find_unknown_words(vocab, book_words) == ["from", "to"])
    test(find_unknown_words([], book_words) == book_words)
    test(find_unknown_words(vocab, ["the", "boy", "fell"]) == [])

# test_suite()