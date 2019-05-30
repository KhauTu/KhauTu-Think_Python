# chuỗi trần: bỏ qua các escape sequence trong chuỗi
# print(r'Haizz, \neu mot ngay nao do')

# toán tử in: nhận 1 trong 2 giá trị True hoặc False
# in: kiểm tra 1 chuỗi có nằm trong chuỗi khác không
strA = "HowKteam.com"
strB = strA[:5:-1]
strC = strB in strA

# cắt chuỗi bằng indexing
# strB = strA[None:None]
# strB = strA[:5:-1]
print(strB)

# ép kiểu dữ liệu
A = int("69") + 5
B = str(69) + "5"
print(A)
print(B)

# hashable object
print(hash(strA))



