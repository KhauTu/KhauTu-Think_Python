# Tuple được giới hạn bởi cặp ngoặc tròn ()
# các phần tử tuple được phân cách bởi dấu phảy ,
# Tuple có khả năng chứa mọi giá trị
# Tốc độ truy xuất tuple nhanh hơn list
# dung lượng chiếm trong bộ nhớ nhỏ hơn list
# bảo vệ dữ liệu không bị thay đổi
# có thể dùng làm key của dictionary

tup = (i for i in range(10) if i % 2 ==0)

# generator expession
a = tuple(tup)

tup = (1,5,9,4)

a = tup.count(1)

# index() lấy ra vị trí xuất hiện đầu tiên
print(tup)
print(a)