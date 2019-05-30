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
    '''
    Hàm này dùng để tìm ký tự ch trong một string
    kết quả trả ra vị trí của ký tự đó trong chuỗi
    nếu không, trả về -1
    start: là vị trí bắt đầu tìm kiếm trong chuỗi
    end: là vị trí kết thúc tìm kiếm
    '''
    ix = start
    if end is None:
        end = len(strng)
    while ix < end:
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1

def count_letter2(strng, ch):
    '''
    Hàm này dùng để đếm số ký tự ch trong một string
    kết quả trả ra số lần xuất hiện của ký tự
    nếu không, trả về 0
    '''
    count = 0
    i = 0
    while find(strng, ch, start = i) != - 1:
        i = find(strng, ch, start = i) + 1
        count += 1
    return count

def count(sub, strng):
    '''
    Hàm này dùng để đếm số lần xuất hiện của chuỗi này trong chuỗi khác
    kết quả trả ra số lần xuất hiện của chuỗi
    nếu không, trả về 0
    '''
    count = 0
    i = 0
    # 1: Tìm xem ký tự đầu tiên trong sub có xuất hiện trong strng
    while find(strng, ch=sub[0], start = i) != - 1:
        # 2: Gán i cho vị trí tìm thấy sub[0] + 1 và tìm tiếp
        i = find(strng, ch=sub[0], start = i) + 1
        # 3: Gán check bằng sub[0] + các ký tự tiếp theo trong strng
        check = sub[0] + strng[i:(i-1+len(sub))]
        if check == sub:
            count +=1
    return count

def find_sub(strng, sub, start=0, end=None):
    i = start
    if end is None:
        end = len(strng)
    while find(strng, ch=sub[0], start = i) != - 1:
        i = find(strng, ch=sub[0], start = i) + 1
        check = sub[0] + strng[i:(i-1+len(sub))]
        if check == sub:
            return i - 1
    return - 1

def remove_sub(sub, strng):
    i = 0
    while find_sub(strng, sub, start = i) != - 1:
        i = find_sub(strng, sub, start = i)
        strng = strng[:i] + strng[(i+len(sub)):]
        i += 1
    return strng

def remove_all(sub, strng):
    while find_sub(strng, sub) != -1:
        strng = remove_sub(sub,strng)
    return strng

def test_suite():
    # test count(sub, strng)
    test(count("is", "Mississippi") == 2)
    test(count("an", "banana") == 2)
    test(count("ana", "banana") == 2)
    test(count("nana", "banana") == 1)
    test(count("nanan", "banana") == 0)
    test(count("aaa", "aaaaaa") == 4)
    # test find_sub(strng, sub, start=0, end=None)
    test(find_sub("banana", "an") == 1)
    test(find_sub("bicycle", "cyc") == 2)
    test(find_sub("Mississippi", "iss") == 1)
    test(find_sub("bicycle", "eggs") == -1)
    # test remove_sub(sub, strng)
    test(remove_sub("an", "banana") == "bana")
    test(remove_sub("cyc", "bicycle") == "bile")
    test(remove_sub("iss", "Mississippi") == "Missippi")
    test(remove_sub("eggs", "bicycle") == "bicycle")
    # test remove_all(sub, strng)
    test(remove_all("an", "banana") == "ba")
    test(remove_all("cyc", "bicycle") == "bile")
    test(remove_all("iss", "Mississippi") == "Mippi")
    test(remove_all("eggs", "bicycle") == "bicycle")

test_suite()

# print(find_sub("banana", "an"))

# strng[(i+len(sub)):]
# strng = "bicycle"
# print(find_sub("bicycle", "eggs"))