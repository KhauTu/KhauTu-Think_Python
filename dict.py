# Các phần tử của Dict là một cặp key: value
# các key phải là một hash object

dic = {'name': 'Kteam', 'member': 69}

# comprehension
dic = {key: value for key, value in [('name','Kteam'),('member',69)]}

# khởi tạo dict rỗng
dic = dict()

# khởi tạo dict từ một mapping object

# khởi tạo dict bằng iterable
iter = [('name','Kteam'),('member',69)]
dic = dict(iter)

# khởi tạo bằng keyword argument
dic = dict(name='Kteam',FE='Free education')

# Phương thức dict.fromkeys(iterable, value)
iter = ('name','number')
dic_none = dict.fromkeys(iter)
# print(dic_none)
dic = dict.fromkeys(iter,'None none value')
dic['name'] = 'HowKteam'
# print(dic['name'])

dic = dict(K = 'Kteam', HK = 'HowKteam', FE = 'Free education')
print(dic)

dic['K'] = dic['K'] + ' - Share to be better'
print(dic)
