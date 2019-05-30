# set là một container, nhưng không được dùng nhiều như list hay tuple
# set không chứa phần tử trùng lặp
# set chỉ chứa hashable object, nhưng set không phải hashable object
# Không thể tạo một empty set
# Set không quan tâm vị trí các phần tử
# set và list là unhashable object

set_1 = {69, 96}

set_2 = {value for value in range(3)}

# constructor có thể tạo ra empty set
set_2 = set([1,1,2,3,3,4,4,5,6])
set_2 = set()
# print(set_2)
# print(type(set_2))

# <set 1> - <set 2> Kết quả trả về là một Set gồm các phần tử chỉ tồn tại trong Set1 mà không tồn tại trong Set2
# print({2,3} - {2,3,4})

# <set 1> & <set 2> Kết quả trả về là một Set chứa các phần tử vừa tồn tại trong Set1 vừa tồn tại trong Set2
# print({2,3} & {2,3,4}) # phép giao

# <set 1> | <set 2> Kết quả trả về là một Set chứa tất cả các phần tử tồn tại trong hai Set
# print({2,3} | {2,3,4}) # phép hợp

# <set 1> ^ <set 2> Kết quả trả về là một Set chứa tất cả các phần tử chỉ tồn tại ở một trong hai Set
# print({2,3} ^ {2,3,4})

set1 = {1,2,3}
set2 = {3,4}

set3 = set1 & set2
set4 = set1 | set2
set5 = set4 - set3

print(set3)
print(set4)
print(set5)

# set5.clear() trả về set rỗng
# set5.pop() lấy ra 1 phần tử và xoá phần tử đó trong set ban đầu
# set5.remove(2) lấy ra phần tử chỉ định trong set
# set5.discard(5) giống remove, nhưng không báo lỗi nếu phần tử khai báo không có trong set
# set5.copy()
# set5.add(5) thêm 1 phần tử vào set

print(id(set5))
set5.add(5)
print(id(set5))
