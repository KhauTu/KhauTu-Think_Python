from __future__ import print_function
import math

ratio = math.e
print(math.log10(ratio))

# 3-1
def right_justify(s):
    l = len(s)
    print(' '*(70 - l) + s)

right_justify('monty')

# 3-2
# def do_four(f,s):
#     f(s)
#     f(s)

# def print_twice(s):
#     print(s)
#     print(s)

# do_four(print_twice,'spam')

# 3-3
def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print('+ - - - - ', end='')

def print_post():
    print('|         ', end='')

def print_beams():
    do_twice(print_beam)
    print('+')

def print_posts():
    do_twice(print_post)
    print('|')

def print_row():
    print_beams()
    do_four(print_posts)

def print_grid():
    do_twice(print_row)
    print_beams()

print_grid()

def print_4beam():
    do_four(print_beam)
    print('+')
def print_4post():
    do_four(print_post)
    print('|')

def print_cell():
    print_4beam()
    do_four(print_4post)

def print_4x4():
    do_four(print_cell)
    print_4beam()

print_4x4()
