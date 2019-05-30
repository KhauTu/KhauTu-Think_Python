d = {'Team':'Kteam',(1,2):69}
print(d)

# copy() tạo ra bản sao tại một vùng nhớ mới
d2 = d.copy()
print(d2)

# get(key) ra giá trị value default
value = d.get('Team',(1,2))

# items() trả ra giá trị là 1 tuple gồm key và value
value = d.items()

# keys() lấy ra tuple danh sách keys
value = d.keys()

#values()
value = d.values()

# pop() lấy ra value của key điền vào pop
# value = d.pop('Team')

# popitem()
# value = d.popitem()

# setdefault() thêm 1 cặp key: value
value = d.setdefault('WhatsUpGuys','Hey')

# update()
value = d.update([('a',1),('b',2)])
print(value)
print(d)