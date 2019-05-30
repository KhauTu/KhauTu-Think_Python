a = 'how kteam free education'

# split(sep, maxsplit) trả về một list được cắt ra bằng 1 ký tự; maxsplit là số lần cắt tối đa
# rsplit() cắt từ phải qua
# partition() trả về tuple lần lượt là 3 phần tử
# rpartition()
# count(sub, start, end) đếm 1 tập con trong số ký tự từ vị trí start đến end
# startswith() trả về True hoặc False nếu chuỗi bắt đầu bằng ký tự trong ngoặc
# endswith()
# find() trả về số nguyên là vị trí đầu tiên tìm thấy chuỗi
# rfind() tìm từ phải qua
# islower() có phải chuỗi viết thường
# isupper()
# isdigit() kiểm tra có phải số hay không
# isspace() kiểm tra tất cả ký tự có phải khoảng trắng
b = a.isspace()

s = 'aaaAAaaaooaaneu mot Ngay naO Doaaaaaaa'

s = s.strip('aAo')
s = s.title()
s = s + "o"
# 'Neu Mot Ngay Nao Do
print(s)
# print(a)
# print(b)