# The Collatz 3n + 1 sequence
# from time import sleep
import math
import sys

def test(did_pass):
    """Print the result of the test."""
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def seq3np1(n):
    """ Print the 3n+1 sequence from n,
        terminating when it reaches 1.
    """
    while n != 1:
        print(n, end=", ")
        if n % 2 == 0: # n is even
            n = n // 2
        else: # n is odd
            n = n * 3 + 1
    print(n, end=".\n")

# seq3np1(670617279)

def count_odd(lst):
    count = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 1:
            count += 1
        else: continue
    return count

def sum_even(lst):
    sum = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            sum = sum + lst[i]
        else: continue
    return sum

def sum_negative(lst):
    sum = 0
    for i in range(len(lst)):
        if lst[i] < 0:
            sum = sum + lst[i]
        else: continue
    return sum

def count_leng5(lst):
    count = 0
    for i in range(len(lst)):
        if len(str(lst[i])) == 5:
            count += 1
        else: continue
    return count

def check_odd(lst): # check xem dãy có toàn số lẻ không
    check = 1
    for k in lst:
        check = check * (k % 2)
    return bool(check)

def sum_ex1even(lst):
    sum = 0
    i = 0   
    if check_odd(lst): # nếu dãy toàn lẻ
        for k in lst:
            sum += k
        return sum
    else: # nếu dãy có ít nhất 1 số chẵn
        while lst[i] % 2 != 0:
            sum += sum + lst[i]
            i += 1
        for k in range(i+1, len(lst)):
            sum = sum + lst[k]
        return sum

def to_sam(lst):
    check = 'sam'
    count = 0
    if check in lst:
        for k in lst:
            if k != check:
                count += 1
            else:
                break
        return count + 1
    else:
        count = len(lst) + 1
        return count

def sqrt(n):
    approx = n/2.0 # Start with some or other guess at the answer
    while True:
        better = (approx + n/approx)/2.0
        if abs(approx - better) < 0.001:
            return better
        approx = better

def print_triangular_numbers(n):
    k = 0
    for i in range(1, n+1):
        k += i
        print(i, "\t", k)

def is_prime(n):
    i = 2
    while i < sqrt(n):
        if n % i == 0:
            return False
            break
        i += 1
    return True

def test_suite():
    test(is_prime(11))
    test(not is_prime(35))
    test(is_prime(19911121))
    test(not is_prime(19920311))
    test(is_prime(101))

# test_suite()

# print_triangular_numbers(5)
# para = '''Composition of list traversal, sam summing, counting, testing conditions and early exit is a rich collection of building blocks that can be combined in powerful ways to create many functions that are all slightly different.'''

# lst = para.split(" ")

# print(count_leng5(lst))
# lst = [1, 2, 5]

# print(count_odd(lst))
# print(sum_even(lst))
# print(sum_negative(lst))
# print(check_odd(lst))
# print(sum_ex1even(lst))
# print(to_sam(lst))
# print(sqrt(25))

