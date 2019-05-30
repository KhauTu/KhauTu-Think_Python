'''
def fib(n):
    # if n <= 1:
    #     return n
    # t = fib(n-1) + fib(n-2)
    # return t
    n0 = 0
    n1 = 1
    i = 1
    if n <= 1:
        return n
    while i < n:
        n2 = n0 + n1
        n0 = n1
        n1 = n2
        i += 1
    return n2
'''

alreadyknown = {0: 0, 1: 1}

def fib(n):
    if n not in alreadyknown:
        new_value = fib(n-1) + fib(n-2)
        alreadyknown[n] = new_value
    return alreadyknown[n]
print(fib(40))
