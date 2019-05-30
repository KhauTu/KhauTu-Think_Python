# toán tử and tương đương &
# ưu tiên toán tử ngoặc tròn trước, rồi đến +,-,x,/ rồi đến toán tử logic sau cùng
print(5*0 != 0)

# Python so sánh các kí tự với nhau bằng cách đưa chúng về dưới dạng số bằng hàm ord.
# Bạn có thể tham khảo giá trị của nó trong ASCII Table.

print(ord('A'))

# Khi bạn so sánh bằng các toán tử ==, >=, <= thì Python sẽ so sánh hết các phần tử.
# Còn nếu bạn dùng các toán tử như >, <, != thì nhiều lúc Python sẽ không cần phải đi hết các giá trị iterable.

print('a'>'ABC')

# toán tử is
lst = [1, 2, 3]
lst_ = lst

print(lst == lst_)
print(lst is lst_)

# Khi so sánh hai giá trị (đối tượng) bằng toán tử == thì Python sẽ so sánh bằng giá trị của chúng.
# Còn nếu so sánh bằng toán tử is thì Python sẽ lấy giá trị của hàm id để so sánh.

# Các số từ -5 đến 256 hoặc là một số chuỗi có số kí tự dưới 20 thì các biến có cùng một giá trị sẽ có cùng một giá trị trả về từ hàm id.
a = -5
b = -5
print(id(a))
print(id(b))
print(a is b)

# NOT, AND và OR
'''
>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> False and False
False
'''
'''
>>> True or True
True
>>> True or False
True
>>> False or True
True
>>> False or False
False
'''
# giá trị là 0, None, rỗng sẽ trả về False
'''
>>> bool(0)
False
>>> bool(None)
False
>>> bool('')
False
>>> bool([])
False
>>> bool(())
False
>>> bool(set())
False
>>> bool({})
False
'''
'''
>>> bool(1)
True
>>> bool('abc')
True
>>> bool([1, 2, 3])
True
'''
# Syntaxnic sugar:
# >>> k in (3, 4, 5) # nên dùng () hơn là [] hoặc thứ gì khác
# True