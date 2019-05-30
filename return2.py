# y = f(x) = x**3 + 2*x**2 - 4*x + 1
# list (x0, y0)
# Nếu (x0, y0) thoả mãn y0 = f(x0) thì đưa vào list A, không thì đưa vào list B

def f(*args):
    listA = []
    listB = []
    for x, y in args:
        if y == x**3 + 2*x**2 - 4*x + 1:
            listA.append((x,y))
        else:
            listB.append((x,y))  
    return listA, listB
lst = [(-5,-20),(-4,-15),(-3,4),(-2,9),(-1,7),(0,1),(1,-7),(2,-9),(4,81),(5,130)]

listA, listB = f(*lst)
print("Tập hợp các điểm thuộc đồ thị hàm số: ", listA, "\n", "Tập hợp các điểm không thuộc đồ thị hàm số: ", listB)

def sum_y(*args):
    s_y = 0
    for x, y in args:
        s_y += y
    return s_y

# print(sum_y(*listA))
# print(sum_y(*listB))
s_y_dif = sum_y(*listA) - sum_y(*listB)
print("Trị tuyệt đối của hiệu tổng tung độ hai list trên: ", s_y_dif if s_y_dif > 0 else -s_y_dif)

def max2_1(args):
    for i in range(len(args)):
        sum = 0
        for i in range(len(args)):
            sum += args[i]
        ave = float(sum)/len(args)
        if args[i] < ave and len(args) > 1:
            args.pop(i)
        else:
            return 2*args[i]-1
lst = [32,59,8,24,15,100]
print(max2_1(lst))

# Đáp án:
'''
def f_x(x):
    return x**3 + 2 * x**2 - 4 * x + 1

def check_point(x, y):
    if y == f_x(x):
        return True
    return False

def fil_point(lst_point):
    lst_A, lst_B = [], []
    for l in lst:
        if check_point(*l):
            lst_A.append(l)
            continue
        lst_B.append(l)
    return lst_A, lst_B

def cal_sum(lst):
    s = 0
    for value in lst:
        s += value[1]
    return s

lst = [(-5, -20), (-4, -15), (-3, 4), (-2, 9), (-1, 7), (0, 1)
, (1, -7), (2, -9), (4, 81), (5, 130)]

lst_A_after, lst_B_after = fil_point(lst)
print(abs(cal_sum(lst_A_after) - cal_sum(lst_B_after)))
'''

'''
def find_max(x, y):
    return int((x + y + abs(x - y))/2)

a = 32
b = 59
c = 8
d = 24
e = 15

_max = find_max(find_max(find_max(find_max(a, b), c), d), e)
print(2 * _max - 1)
'''

