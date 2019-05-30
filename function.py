# default argument phải nằm ở vị trí cuối cùng của khai báo parameter
def kteam(age, text = 'Kter'):
    print(text)
    print(age)

def f(kteam = []):
    kteam.append('F')
    print(kteam)

# positional truyền parameter theo đúng thứ tự
# keyword argument cần khai báo theo keyword
# khai báo positional trước, keyword sau
def Teo(a, b=2, c=3, d=4):
    f = (a+d) * (b+c)
    print(f)

# * parameter ám chỉ từ đó về sau là keyword argument, có thể thay bằng *identifier
def kteam(pos_or_key_arg, *, key_arg1=1, key_arg2=2):
    print(pos_or_key_arg)
    print(key_arg1)
    print(key_arg2)

# sorted([1,2,3], key = None)

# dấu / ám chỉ các argument trước đó là positional-only argument

# unpacking các list, tuple, set, dict key, truyền vào dưới dạng positional argument
def kteam(k, t, e, r):
    print(k)
    print(t, e)
    print('end', r)
lst = ['123','Kteam',69.96, 'Henry']

# kteam(lst[0],lst[1],lst[2],lst[3])
# kteam(*lst)

# packing arguments
# không được cho 2 parameter làm nhiệm vụ packing cho 1 hàm
# sau 1 packing arguments, thì chỉ được dùng keywork arguments
def k(*args, kter):
    print(args)
    print(kter)

# k(*(x for x in range(7)),kter = 'ahihi') # unpack sau đó là pack

# hàm khai báo trước, biến khai báo sau
def kteam(name, member):
    print('name =>', name)
    print('member =>', member)

dict = {'name': 'Kteam', 'member': 69}

# unpacking value trong dict
kteam(**dict)

def kt(**kwargs):
    # print(kwargs)
    # print(type(kwargs))
    for key, value in kwargs.items(): # phương thức items của kiểu dữ liệu dict
        print(key, '=>', value)
kt(name='Kteam', member=69)

'''
def best_function_ever(*args, **kwargs): # packing và unpacking arguments
'''

'''
sorted(iterable, /, *, key=None, reverse=False):
key: đặc điểm của iterable cần sắp xếp, ví dụ như len() - độ dài
'''