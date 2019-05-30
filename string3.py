a = "My team is %s %s years old" %('1','2')
# print(a)

s = '%s %s'
result = s %('1','2')
print(result)

# %s: giá trị phương thức __str__ của đối tượng
# %r: giá trị phương thức __repr__ của đối tượng
# %d: giá trị của một số - lấy phần nguyên
# %f: giá trị của 1 số thực
# %.2f: lấy 2 số ở phần thập phân
# có thể sử dụng %s hoặc %r với mọi đối tượng trong python

# f = '%.3f' %(3.49999)
# print(f)

# định dạng bằng chuỗi f-string
name = "Kteam"
address = "Da Lat"
phone = "0123456789"

result = f'Student: {{name}}\nAddress: {{address}}\nPhone: {{phone}}'
print(result)

# định dạng bằng phương thức format
r = 'a:{}, b:{}, c:{}'.format('one','two','three')
print(r)
print('a:{1}, b:{2}, c:{0}'.format('one','two','three'))

print('1:{one}, 2:{two}'.format(one = 111, two = 222))

# 3 cách căn lề cơ bản của phương thức format
# căn lề trái {:(c)<n}
# căn lề phải {:(c)>n}
# căn giữa {:(c)^n}

t = '{:*^10}'.format('Kteam')
print(t)

# phần định dạng
row_1 = '+{:-<6}+{:-^15}+{:->10}+'.format('','','')
row_2 = '|{:<6}|{:^15}|{:>10}|'.format('ID','Ho va ten','Noi sinh')
row_3 = '|{:<6}|{:^15}|{:>10}|'.format('123','Yui Hatano','Japanese')
row_4 = '|{:<6}|{:^15}|{:>10}|'.format('6969','Sunny Leone','Canada')
row_5 = '+{:-<6}+{:-^15}+{:->10}+'.format('','','')

print(row_1)
print(row_2)
print(row_3)
print(row_4)
print(row_5)