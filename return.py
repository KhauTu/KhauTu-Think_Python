def cal_rec_per(width, height):
    per = (width + height) * 2
    return per
'''
rec_1_width = 5
rec_1_height = 3

# khởi tạo một biến để hứng kết quả
rec_1_per = cal_rec_per(rec_1_width, rec_1_height)

print(rec_1_per)

# trường hợp này là khi bạn không cần tái sử dụng nó ở lần sau
print(cal_rec_per(7, 4))
'''
def _return_ter_func():
    print('chúng ta sử dụng return để ngắt hàm')
    # dòng dưới đây tương tự như bạn viết return None
    return
    print('Hàm print này dĩ nhiên không được gọi')
'''
none = _return_ter_func()
print(type(none))
'''
# return ra nhiều giá trị cùng lúc
def cal_rec_area_per(width, height):
    perimeter = (width + height) * 2
    area = width * height
    return perimeter, area

rec_width = 3
rec_height = 9
rec_per, rec_area = cal_rec_area_per(rec_width, rec_height)

print(rec_per, rec_area)
