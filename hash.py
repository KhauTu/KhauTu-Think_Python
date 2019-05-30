# hashable vs unhashable
b = 'Kteam'
a = id(b)
c = id((1,2,3))
# print(a)
# print(id('Kteam'))
# print(c)

n = 69
# print(n)
# print(n.__add__(1))
# print(n.__sub__(1))
# print(n.__mul__(2))
# print(n.__neg__())

s_1 = [1,2]

print(id(s_1))

# +=
s_1 = s_1.__add__([3,4])

print(s_1)