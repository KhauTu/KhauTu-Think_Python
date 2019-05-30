import string

txt = '''
Don’t chase people.
Be yourself, do your own thing and work hard.
The right people – 
the ones who really belong in your life – 
will come to you. And stay.
'''

# 1: Remove all punctuation
def remove_punct(s):
    s_no_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_no_punct += letter
    return s_no_punct
# print(remove_punct(txt))

# 2: break string into a list of words
lst = remove_punct(txt).split()
# print(lst)

# 3: counts the number or words that contain "e"
count = 0
for l in lst:
    if "e" in l:
        count += 1
# print(count)
# 4: print: Your text contains 243 words, of which 109 (44.8%) contain an "e".
print('''Your text contains {0} words, of which {1} ({2:.1f}%) contain an "e".'''.format(len(lst)+1, count, count*100 / (len(lst)+1)))

# 5 multiplication table 12x12
layout = "{0:>5}{1:>5}{2:>5}{3:>5}{4:>5}{5:>5}{6:>5}{7:>5}{8:>5}{9:>5}{10:>5}{11:>5}"

print(layout.format("i", "i*2", "i*3", "i*4", "i*5", "i*6", "i*7", "i*8", "i*9", "i*10", "i*11", "i*12"))

for i in range(1, 13):
    print(layout.format(i, i*2, i*3, i*4, i*5, i*6, i*7, i*8, i*9, i*10, i*11, i*12))

layout = "{0:>4}{1:>6}{2:>6}{3:>8}{4:>13}{5:>24}"

print(layout.format("i", "i**2", "i**3", "i**5", "i**10", "i**20"))
for i in range(1, 11):
    print(layout.format(i, i**2, i**3, i**5, i**10, i**20))