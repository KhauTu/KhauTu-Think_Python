import sys

def test(did_pass):
    """Print the result of the test."""
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def add_vectors(u, v):
    ''' Cộng hai vectors '''
    sum_vec = []
    for i in range(len(u)):
        sum = u[i] + v[i]
        sum_vec.append(sum)
    return sum_vec

def scalar_mult(s, v):
    ''' tích vô hướng vectors '''
    mult_vec = []
    for k in v:
        mult = s * k
        mult_vec.append(mult)
    return mult_vec

def dot_product(u, v):
    sum = 0
    for i in range(len(u)):
        sum += u[i] * v[i]
    return sum

def cross_product(u, v):
    cross = [u[1]*v[2] - u[2]*v[1],
             u[2]*v[0] - u[0]*v[2],
             u[0]*v[1] - u[1]*v[0]]
    return cross

'''
def crossProd(a,b):
      dimension = len(a)
      c = []
      for i in range(dimension):
        c.append(0)
        for j in range(dimension):
          if j <> i:
            for k in range(dimension):
              if k <> i:
                if k > j:
                  c[i] += a[j]*b[k]
                elif k < j:
                  c[i] -= a[j]*b[k]
      return c
'''

def test_suite():
    test(add_vectors([1, 1], [1, 1]) == [2, 2])
    test(add_vectors([1, 2], [1, 4]) == [2, 6])
    test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])
    test(scalar_mult(5, [1, 2]) == [5, 10])
    test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
    test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])
    test(dot_product([1, 1], [1, 1]) == 2)
    test(dot_product([1, 2], [1, 4]) == 9)
    test(dot_product([1, 2, 1], [1, 4, 3]) == 12)
    test(cross_product([3,-3,1], [4,9,2]) == [-15,-2,39])
    test(cross_product([3,-3,1], [-12,12,-4]) == [0,0,0])

test_suite()
