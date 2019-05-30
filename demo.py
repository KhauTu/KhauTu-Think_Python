# từ thư viện decimal -> import mọi thứ 
from decimal import *

# lấy tối đa 30 chữ số phần nguyên và phần thập phân decimal
# getcontext().prec = 40

f = 10/3
print(f)
print(type(f))

d = Decimal(10)/(3)
print(d)
print(type(d))