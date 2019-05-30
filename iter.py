# cách tạo ra 1 iterator object,
# không thể truy xuất trực tiếp mà chỉ truy xuất được từng phần tử
itera = (x for x in range(3))
print(itera)
# truy xuất từng phần tử:
print(next(itera))
print(next(itera))
print(next(itera))

# File object cũng là một iterator.
# Bạn cũng có thể sử dụng cách này để đọc file.

lst = [6, 3, 7, 'kteam', 3.9, [0, 2, 3]]
iter_list = iter(lst) # iter_list là một iterator tạo từ list

# iterator không hỗ trợ indexing
print(next(iter_list))

# Lưu ý: iterator này cũng dính một vấn đề như List, Dict đó chính là chỉnh một, thay đổi hai.

# Hàm tính tổng – sum
# sum(iterable, start=0)
it = (x for x in range(3))
print(sum(it, 10))

# Hàm tìm giá trị lớn nhất – max
# max(iterable, *[, default=obj, key=func])
it = (x for x in range(3))
print(max([],default='Kteam'))

# Hàm tìm giá trị nhỏ nhất – min
# min(iterable, *[, default=obj, key=func])
# min(arg1, arg2, *args, *[, key=func])

# Hàm sắp xếp – sorted
# sorted(iterable, /, *, key=None, reverse=False)

it = [1,6,7,2]
print(sorted(it,reverse=True))
