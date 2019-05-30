
# letter_counts = {}
string = "ThiS is String with Upper and lower case Letters"
# string = "".join(string.lower().split(" "))
# print(string)
# for letter in string:
#     letter_counts[letter] = letter_counts.get(letter, 0) + 1

# letter_items = list(letter_counts.items())
# letter_items.sort()
# for (l,c) in letter_items:
#     print(l, c, sep = '\t')

def dict_str(string):
    letter_counts = {}
    string = "".join(string.lower().split(" "))
    for letter in string:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    letter_items = list(letter_counts.items())
    letter_items.sort()
    return letter_items

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

def dict_lst(lst):
    letter_counts = {}
    for letter in lst:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    letter_items = list(letter_counts.items())
    letter_items.sort()
    return letter_items

book_words = get_words_in_book("alice_in_wonderland.txt")

'''
print("{0:<10}\t{1:<5}".format("Word","Count"))
print("="*21)

for i, (l,c) in enumerate(dict_lst(book_words)):
    if i < 10:
        print("{0:<10}\t{1:<5}".format(l,c))
'''
leng_wds = {}
leng_lst = []
for (l,c) in dict_lst(book_words):
    leng_wds[l] = len(l)
    if len(l) not in leng_lst:
        leng_lst.append(len(l))

for wd,leng in leng_wds.items():
    if leng == max(leng_lst):
        print(wd)

print(max(leng_lst))


