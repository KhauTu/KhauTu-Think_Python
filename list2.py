a = [1,2,3,4,5,6,7,8,9]

c = a.count(1)
# index() chỉ ra vị trí phần tử trong list
c = a.index(1)

# copy() trả về một bản sao list tương tự, giống list constructor
c = a.copy()
c[0] = 'Kteam'

# xoá mọi phần tử trong list
c = a.clear() 
# print(c)
# print(a)

a = [9,1,2,3]
print(a)
# a.append([4,5])

# extend() mở rộng thêm từng phần tử vào trong list
# a.extend([4,5,[7,8]])

# insert(x,y) thêm phần tử y vào vị trí x
# nếu x > len(list) thì giống append()
# a.insert(6,9)

# pop(x) lấy ra phần tử thứ x
# c = a.pop(1)
# print(a)

# remove(x) bỏ đi phần tử x đầu tiên; nếu x ko có trong list thì sẽ bị lỗi
# a.remove(1)

# reverse() tạo 1 list thứ tự đảo ngược lại

# sort(key = None, reverse = False) sắp xếp list các phần tử cùng kiểu dữ liệu
a.sort(reverse = True)
print(a)