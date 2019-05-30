import sys
import time
import draw_queens
import random
from Chap14_RemoveDup import *

def test(did_pass):
    """Print the result of the test."""
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0) # Calc the absolute y distance
    dx = abs(x1 - x0) # CXalc the absolute x distance
    return dx == dy # They clash if dx == dy

def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
        with any queen to its left.
    """
    for i in range(c): # Look at all columns to the left of c
        if share_diagonal(i, bs[i], c, bs[c]):
            return True
    return False # No clashes - col c has a safe placement.

def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We’re assuming here that the_board is a permutation of column
        numbers, so we’re not explicitly checking row or column clashes.
    """
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False

def main(m):
    # m: num_found
    import random
    rng = random.Random() # Instantiate a generator
    n = 8
    bd = list(range(n)) # Generate the initial permutation
    num_found = 0
    tries = 0
    sol_lst = []
    while num_found < m:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            # print("Found solution {0} in {1} tries.".format(bd, tries))
            sol_lst += bd
            tries = 0
            num_found += 1        
    # print(len(sol_lst))
    sol_lst = [sol_lst[i:i+8] for i in range(0, len(sol_lst), 8)]
    sol_lst.sort()
    sol_lst = remove_adjacent_dups(sol_lst)
    return sol_lst

t0 = time.process_time()
# main()
t1 = time.process_time()
# print("total time is {0}".format(t1-t0))

# lst0 = []
# lst1 = [1, 2, 3, [4, 5, 6], 7, 8, 9]
# lst2 = [4, 5, 6]
# print(lst2 in lst1)
# lst0.append(lst1)
# lst0.append(lst2)

# print(lst0)

def mirror_X(lst):
    mirror = []
    for v in lst:
        v = 7 - v
        mirror.append(v)
    return mirror

def mirror_Y(lst):
    lst.reverse()
    return lst

def anti_90(lst):
    result = []
    for [i, v] in enumerate(lst):
        [i, v] = [v, 7 - i]
        result.append([i, v])
        result.sort()
    lst = []
    for [i, v] in result:
        lst.append(v)
    return lst

def anti_180(lst):
    return anti_90(anti_90(lst))

def anti_270(lst):
    return anti_180(anti_90(lst))

def sym_family(lst):
    fl = [mirror_X, mirror_Y, anti_90, anti_180, anti_270]
    family = []
    for f in fl:
        family += lst
        lst = f(lst)
        for f in fl:
            family += lst
            lst = f(lst)
            for f in fl:
                family += lst
                # lst = f(lst)
                # for f in fl:
                #     family += lst

    family = [family[i:i+8] for i in range(0, len(family), 8)]
    family.sort()
    family = remove_adjacent_dups(family)
    return family

lst = [0,4,7,5,2,6,1,3]
# print(sym_family(lst))
sol_lst = main(92)
all_sym = []
for l in sol_lst:
    all_sym.append(sym_family(l))
all_sym.sort()
all_sym = remove_adjacent_dups(all_sym)


for i in range(len(all_sym)):
    print(all_sym[i][0])
    draw_queens.draw_board(all_sym[i][0])
print(len(all_sym))   
'''
def same_sym(first, second):
    return (first in sym_family(second))
lt = []
for i in range(len(sol_lst)):
    for j in range(len(sol_lst)):
        if j > i:
            if same_sym(sol_lst[i], sol_lst[j]):
                lt.append(i)
for k in lt:
    print(sol_lst[k])
'''
'''
def sym_family(lst):
    X = mirror_X(lst)
    Y = mirror_Y(lst)
    XY = mirror_X(mirror_Y(lst))
    
    X_90 = mirror_X(anti_90(lst))
    X_90_flip = anti_90(mirror_X(lst))

    Y_90 = mirror_Y(anti_90(lst))
    Y_90_flip = anti_90(mirror_Y(lst))

    XY_90 = mirror_X(mirror_Y(anti_90(lst)))
    XY_90_flip = anti_90(mirror_X(mirror_Y(lst)))

    X_180 = mirror_X(anti_180(lst))
    X_180_flip = anti_180(mirror_X(lst))

    Y_180 = mirror_Y(anti_180(lst))
    Y_180_flip = anti_180(mirror_Y(lst))

    XY_180 = mirror_X(mirror_Y(anti_180(lst)))
    XY_180_flip = anti_180(mirror_X(mirror_Y(lst)))

    X_270 = mirror_X(anti_270(lst))
    X_270_flip = anti_180(mirror_X(lst))

    Y_270 = mirror_Y(anti_270(lst))
    Y_270_flip = anti_270(mirror_Y(lst))

    XY_270 = mirror_X(mirror_Y(anti_270(lst)))
    XY_270_flip = anti_180(mirror_X(mirror_Y(lst)))

    family = [lst, X, Y, XY, X_90, X_90_flip, Y_90, Y_90_flip, XY_90, XY_90_flip, X_180, X_180_flip, Y_180, Y_180_flip, XY_180, XY_180_flip, X_270, X_270_flip, Y_270, Y_270_flip, XY_270, XY_270_flip]
    family.sort()
    family = remove_adjacent_dups(family)
    for v in family:
        print(v, end="\n")
'''
# sym_family([0,4,7,5,2,6,1,3])
# sym_family(mirror_X([0,4,7,5,2,6,1,3]))
# print(remove_adjacent_dups(sym_family([0,4,7,5,2,6,1,3])))

'''
print(not has_clashes([0, 4, 7, 5, 2, 6, 1, 3]))
print(mirror_Y([0, 4, 7, 5, 2, 6, 1, 3]))
print(not has_clashes(mirror_Y([0, 4, 7, 5, 2, 6, 1, 3])))

print(not has_clashes([6,4,2,0,5,7,1,3]))
print(anti_90([6,4,2,0,5,7,1,3]))
print(not has_clashes(anti_90([6,4,2,0,5,7,1,3])))

print(not has_clashes([6,4,2,0,5,7,1,3]))
print(anti_180([6,4,2,0,5,7,1,3]))
print(not has_clashes(anti_180([6,4,2,0,5,7,1,3])))

print(not has_clashes([6,4,2,0,5,7,1,3]))
print(anti_270([6,4,2,0,5,7,1,3]))
print(not has_clashes(anti_270([6,4,2,0,5,7,1,3])))
'''

def main():

    bd = list(range(8)) # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < 10:
        random.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            print('Found solution {0} in {1} tries.'.format(bd, tries))
            draw_queens.draw_board(bd)
            tries = 0
            num_found += 1

# main()

def test_suite():
    test(not share_diagonal(5,2,2,0))
    test(share_diagonal(5,2,3,0))
    test(share_diagonal(5,2,4,3))
    test(share_diagonal(5,2,4,1))
    # Solutions cases that should not have any clashes
    test(not col_clashes([6,4,2,0,5], 4))
    test(not col_clashes([6,4,2,0,5,7,1,3], 7))
    # More test cases that should mostly clash
    test(col_clashes([0,1], 1))
    test(col_clashes([5,6], 1))
    test(col_clashes([6,5], 1))
    test(col_clashes([0,6,4,3], 3))
    test(col_clashes([5,0,7], 2))
    test(not col_clashes([2,0,1,3], 1))
    test(col_clashes([2,0,1,3], 2))

    test(not has_clashes([6,4,2,0,5,7,1,3])) # Solution from above
    test(has_clashes([4,6,2,0,5,7,1,3])) # Swap rows of first two
    test(has_clashes([0,1,2,3])) # Try small 4x4 board
    test(not has_clashes([2,0,3,1])) # Solution to 4x4 case

# test_suite()
