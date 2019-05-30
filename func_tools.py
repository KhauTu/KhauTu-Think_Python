# hàm map: map(func, iterable)
# Hàm map này sẽ trả về một map object (một dạng generator).
'''hàm map lấy từng  phần  tử của iterable sau đó dùng gọi hàm func với argument là giá trị mới lấy ra từ iterable,
kết quả trả về của hàm func sẽ được yield.
'''
def mymap(func, iterable):
    for x in iterable:
        yield func(x)

# def inc(x): return x + 1
kteam = [1, 2, 3, 4]
inc = lambda x: x + 1
print([inc(x) for x in kteam])

'''
Ở list comprehension trên, nếu bạn thay ngoặc vuông ( [ ) bằng ngoặc tròn ( (  ) thì thời gian của ngoặc tròn có thể tương đương với hàm map và tiết kiệm dữ liệu hơn list comprehension vì nó cũng tạo ra một generator expression.
'''

# map(func, *iterable)
'''
khi bạn pass vào nhiều container để biến hàm map gọm lại bằng cách packing argument thì các container phải cùng số lượng giá trị 
(cùng giá trị hàm len). Vì khi có nhiều container pass vào, thì hàm map sẽ cùng một lúc lấy lượt các giá trị của các container.
'''

func = lambda x, y: x + y
kteam_1 = [1, 2, 3, 4]
kteam_2 = [5, 6, 7, 8]
kteam = map(func, kteam_1, kteam_2)

print(list(kteam))

# hàm filter: filter(function or None, iterable)
# không như hàm map, iterable ở đây chỉ là 1 container, không hề có packing argument.
'''
Hàm filter lấy từng giá trị trong iterable, sau đó gửi vào hàm, nếu như giá trị hàm trả ra là một giá trị mà khi chuyển sang kiểu dữ liệu boolean là True thì sẽ yield giá trị đó, nếu không thì bỏ qua.
Trường hợp bạn không gửi hàm vào mà  là None, hàm filter lấy từng giá trị trong iterable, nếu giá trị đó chuyển sang giá trị boolean là True thì yield, nếu không thì bỏ qua.
'''
func = lambda x: x > 0
kteam = [1, -3, 5, 0, 2, 6, -4, -9]

print(list(filter(func, kteam)))
print([x for x in kteam if x > 0])

# hàm reduce: Bất cứ giá trị nào khi chuyển qua giá trị boolean mà False thì sẽ không được yield.
# from functools import reduce
# reduce(function, sequence[, initial])
# Hàm reduce không giống như hai hàm trước là trả về một generator expression mà là một giá trị.

from functools import reduce
kteam_add = lambda x, y: x + y
kteam_multi = lambda x, y: x * y
kteam = [1, 2, 3, 4, 5]
print(reduce(kteam_add, kteam)) # ((((1+2)+3)+4)+5)
print(reduce(kteam_add, kteam, 10))
print(reduce(kteam_multi, kteam, 10))
'''
khi chưa có initial, hàm reduce lấy hai giá trị để quăng vào function đầu tiên.
Nhưng khi bạn đưa argument vào cho parameter initial thì hàm reduce sẽ lấy giá trị initial và giá trị đầu tiên của sequence (index 0) đưa vào function và tiếp tục trả ra một giá trị,
rồi giá trị đó lại tiếp tục với giá trị thứ hai của sequence (index 1).
'''

