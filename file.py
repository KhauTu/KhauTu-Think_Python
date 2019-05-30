'''
mode:
r để đọc
r+ để đọc và ghi
w mở để ghi, trước đó nó sẽ xoá hết nội dung file hiện có
w+ mở để ghi và đọc
a mở để ghi
a+ mở để ghi và đọc
Nếu file không tồn tại sẽ tạo một file mới với tên file chúng ta truyền vào
'''


''' đọc file
<File>.read(size = -1)
Nếu size trống hoặc số âm thì nó sẽ đọc hết nội dung file và đưa con trỏ về cuối file
Nếu không sẽ đọc tới n ký tự tương ứng với size
Đọc xong sẽ trả về một chuỗi
'''
file_object = open('HowKteam.txt')
data = file_object.read(2)
data2 = file_object.read(5)
file_object.close()

'''
readline: đọc một dòng, khi nào gặp newline thì dừng, kết quả trả về 1 chuỗi
thêm size sẽ đọc từng ký tự
'''
file_object = open('HowKteam.txt')
data = file_object.readline()
data2 = file_object.readline()
file_object.close()

'''
readlines: đọc toàn bộ file, cho mỗi dòng vào 1 phần tử của list
'''
file_object = open('HowKteam.txt')
data = file_object.readlines()
data2 = file_object.readlines()
file_object.close()

'''
đọc file bằng constructor list; tuple
'''
'''file_object = open('HowKteam.txt',mode='a+')
# data = list(file_object)
# data = tuple(file_object)
data = file_object.write('\nK9')
file_object.close()'''

'''
Kiểm soát con trỏ
'''
file_object = open('HowKteam.txt',mode='r')
data = file_object.read()
# đưa con trỏ về vị trí đầu file
file_object.seek(10)
data2 = file_object.read()
file_object.close()


'''
Câu lệnh with:
with expression [as variable]
    with-block
tự động đóng file sau khối lệnh with
'''
with open('HowKteam.txt') as file_object:
    data = file_object.read()

print(data)