fruit = "banana"
count = 0
# for char in fruit:
#     if char == "a":
#         count += 1
# print(count)

def count_letters(strng, ch):
    count = 0
    for char in strng:
        if ch == char:
            count += 1
    return count

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

# print(find("banana", "a",2))
print(count_letter2("banana", "n"))