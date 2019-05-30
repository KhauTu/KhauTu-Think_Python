'''
def square(lst):
    for num in lst:
        yield num**2

kteam_ret = square([1,2,3])

for value in kteam_ret:
    print(value)

def gen():
    for value in range(3):
        print('yield', value+1,'times')
        yield value    
for value in gen():
    print(value)
'''
def test():
    yield 'Kteam'
    print('this is the second yield')
    yield 'Free education'
    print('this is the last yield')
    yield 'Long đẹp trai'
    print('Will not return anything')
for value in test():
    print(value)

# phương thức send gửi giá trị vào một generator
# cú pháp: generator.send(value)

'''
def gen():
    for i in range(4):
            x = yield i
            print('value sent from you', x)
'''
def gen():
    while True:
            x = yield # ở đây ta đang yield None, vì ta không cần thiết sinh giá trị gì ở  đây
            yield x ** 2
g = gen()
print(next(g))
print(g.send(2))
print(next(g))
print(g.send(10))

# tham khảo: https://stackoverflow.com/questions/102535/what-can-you-use-python-generator-functions-for
# Bộ nhớ, bạn sẽ phải cân nhắc việc dùng yield khi bạn làm việc với những tập dữ liệu lớn.
# Lúc đó, bạn sẽ phải xem xét lại xem liệu bạn có cần giữ tất cả các giá trị một lúc không hay chỉ cần sinh ra từng giá trị một để tiết kiệm bộ nhớ.