import sys
# sys.setrecursionlimit(60200)
def recursion_depth(number):
    '''
    print("{0}, ".format(number), end="")
    recursion_depth(number + 1)
    '''
    print("Recursion depth number", number)
    try:
        recursion_depth(number + 1)
    except:
        print("I cannot go any deeper into this wormhole.")
recursion_depth(0)


# print(sys.getrecursionlimit())