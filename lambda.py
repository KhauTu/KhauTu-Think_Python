# cú pháp: lambda argument_1, argument_2, …, argument_n : expression
def ave(a, b, c):
    return (a + b + c)/3
# print(ave(1, 3, 2))

x_power_a = lambda x, a=2: x ** a
# print(x_power_a(5))

def kteam():
    mem = lambda x: x + ' is a member of Kteam'
    return mem # trả về một hàm nặc danh
call_mem = kteam()
print(call_mem('Long'))

kteam_lst = [lambda x: x**2, lambda x: x**3, lambda x: x**4]
# print(kteam_lst[1](2))
for func in kteam_lst:
    print(func(3))

key = 'Kteam'
print({'Google': lambda: 'Goooooooog',
'YouTube': lambda: 'Youuuuuuuuu',
'Kteam': lambda: 'Free Education'}[key]())

'''
phần argument của lambda ta để trống, điều này hoàn toàn đúng cú pháp vì phần argument là optional (không bắt buộc)
nhưng phần expression bắt buộc phải có một expression.
'''

# Câu điều kiện cho lambda:
# Cách 1: b if a else c
# Cách 2: (a and b) or c

find_greater = lambda x, y: x if x > y else y
# print(find_greater(1,2))

# cd_of_2_3 = lambda x: (1 if x % 3 == 0 else 0) if x % 2 == 0 else 0
cd_of_2_3 = lambda x: (1 if not (x % 3) else 0) if not(x % 2) else 0
# not 0 tương đương True
# print(cd_of_2_3(6))

# lambda trong lambda
def kteam(first_string):
    return lambda second_string: first_string + second_string

slogan = kteam('How Kteam')
print(slogan('Free education'))
