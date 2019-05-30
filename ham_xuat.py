# hàm print()
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

print('Kteam',69,sep = '/')

'''Khi truyền giá trị vào cho parameter theo cách keyword argument thì sẽ không bị packing.
Nghĩa là sẽ không bị gói vào trong giá trị của parameter object.
'''

# parameter end= có giá trị mặc định là newline \n

# print('a line without newline', end = '|||')

'''
from time import sleep
print('start...',end='') # chương trình chưa gặp newline sẽ chưa in ra
sleep(3) # dừng chương trình 3s
print('end...')

print('line1', 'lin\ne2',end = '') # gặp newline, print sẽ xuất hết trong bộ nhớ đệm
sleep(3)
print('end...')
'''

# ta cũng có thể sử dụng hàm print như là phương thức write trong việc ghi file.
with open('printtext.txt','w') as f:
    print('printed by print function',file = f)
with open('printtext.txt') as f:
    data = f.read()
# print(data)

'''
from time import sleep
print('start...',end='', flush=True) # flush = True sẽ yêu cầu xuất hết trong bộ đệm ra
sleep(3)
print('end...')
'''
# print 3x là 1 hàm
# print 2x là một câu lệnh

from time import sleep
your_name = 'Henry'
your_great = 'Hello! My name is '
for c in your_great + your_name:
    print(c, end = '', flush = True)
    sleep(0.1)
print()