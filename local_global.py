# kteam = "How Kteam"
def say_slogan():
    kteam = 'How Kteam'
    print('We are', kteam)

# say_slogan()

# Biến khai báo ở hàm cha có thể sử dụng trong hàm con nhưng biến ở hàm con không thể sử dụng ở hàm cha.

# pass by reference: Có nghĩa là bạn đưa bản gốc.
# pass by value: đưa giá trị hoặc là “đưa bản sao”.
num = 69
st = 'How Kteam'
lst = [1, 2, 3]
tup = tuple('Education')

def change(parameter):
    parameter = 'New value' # pass by value
    # parameter[1] = 'New value' # pass by reference
    print('Changed successfully!')
'''
change(num)
change(st)
change(lst)
change(tup)
print('*' * 10)
print('{}\n{}\n{}\n{}\n'.format(num, st, lst, tup))
'''

# lệnh global: biến 1 local thành global
# global <variable>

def make_slogan():
    # khởi tạo với global không có giá trị nhé
    global kteam
    # sau khi khởi tạo xong, ta mới gán giá trị
    kteam = 'How Kteam'
    print(kteam)

# make_slogan()

# print(kteam)

def make_global():
    global x
    x = 1
    print(x)
def local():
    x = 5
    print('x in local', x)

# make_global()
# print(x)
# local()
# print(x)

'''
Hàm locals cho ta biết được những biến local (những biến được khai báo trong hàm) nằm trong chương trình của chúng ta.
Còn globals là hàm giúp chúng ta biết được những  biến global trong chương trình.
Kết quả trả ra của hai hàm này là một Dict. Với key là tên biến và value là giá trị của biến.
'''
globals()
locals()

