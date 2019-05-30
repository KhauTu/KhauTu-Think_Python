from Chap14_LinearSearch import *
from Chap14_BinarySearch import *
from Chap14_RemoveDup import *

alice = get_words_in_book("alice_in_wonderland.txt")
alice.sort()
alice_clean = remove_adjacent_dups(alice)

vocab = get_words_in_book("vocab.txt")
vocab.sort()
vocab_clean = remove_adjacent_dups(vocab)

def both_list(first, second):
    '''Return only those items that are present in both lists.'''
    
    # find words only in second, not in first:
    only_second = find_unknown_words(first, second)
    for wd in only_second:
        second.remove(wd)
    only_first = find_unknown_words(second, first)
    for wd in only_first:
        first.remove(wd)    
    return first

def either_list(first, second):
    '''Return items that are present in either the first or the second list.'''
    only_second = find_unknown_words(first, second)
    only_first = find_unknown_words(second, first)
    result = both_list(first, second) + only_first + only_second
    result.sort()
    return result
lst1 = list(range(11))
lst2 = list(range(0,18))

# print(either_list(lst1,lst2))
# print(both_list(vocab_clean, alice_clean))

def bagdiff(first, second):
    ''' Return items from the first list that are not eliminated by a matching element in the second list.
    In this case, an item in the second list “knocks out” just one matching item in the first list.
    This operation is sometimes called bagdiff. '''
    for v in second:
        if v in first:
            ind = first.index(v)
            first.remove(first[ind])
    return first

# print(bagdiff([5,7,11,11,11,12,13], [7,8,11]))



