# letter_counts = {}
# for letter in "Mississippi":
#     letter_counts[letter] = letter_counts.get(letter, 0) + 1

# letter_items = list(letter_counts.items())
# letter_items.sort()
# print(letter_items)

letter_counts = {}
string = "ThiS is String with Upper and lower case Letters"
string = "".join(string.lower().split(" "))
print(string)
for letter in string:
    letter_counts[letter] = letter_counts.get(letter, 0) + 1

letter_items = list(letter_counts.items())
letter_items.sort()
for (l,c) in letter_items:
    print(l, c, sep = '\t')

