# list: giới hạn bởi cặp ngoặc vuông []
# các phần tử của list được ngăn cách bởi dấu phảy ,
# List có khả năng chứa mọi giá trị đối tượng của Python và bao gồm chính nó

a = [1,2,5,'Kteam',[[1,2,3],[4,5,6],['Free','education']]]

# list rỗng a = []

# list comprehension
a = [i for i in range(0,10,2)]

a = [[n,n*1,n*2] for n in range(1,4)]

# list constructor: a = list(iterable)
a = list('Kteam')

a = [1,2,'a','b','c',[3,4]]
# toán tử in trả ra True hoặc False
b = 3 in a
a[1] = 'Kteam'
b = a[1]
# print(b)
# print(a)

# ma trận
a = [[1,2,3],[4,5,6],[7,8,9]]

# không được gán list này qua list kia nếu không có chủ đích

a = [[1,2,3],[4,5,6]]
# list constructor có tác dụng copy
b = list(a)
print(b)
print(a)
b[0][0] = 'Kteam'
print(b)
print(a)