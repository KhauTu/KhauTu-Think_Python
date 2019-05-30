
l = [56, 14, 11, 756, 34, 90, 11, 11, 65, 0, 11, 35]
c = []
print(l)
# Tìm vị trí của 11
for i in range(len(l)):
    if l[i] == 11:
        c.append(i)
    else: continue
# Remove 11 khỏi list
while 11 in l:
    l.remove(11)
# xếp thứ tự list từ bé đến lớn
l.sort()
# chèn 11 vào vị trí cũ
for i in range(len(c)):
    l.insert(c[i],11)

print(c)
print(l)

lst = [56, 14, 11, 756, 34, 90, 11, 11, 65, 0, 11, 35]

idx = 0
max_idx = len(lst) - 1

max_jdx = len(lst)

while idx < max_idx:
    if lst[idx] == 11:
        idx += 1
        continue
    jdx = idx + 1
    while jdx < max_jdx:
        if lst[jdx] == 11:
            jdx += 1
            continue
        if lst[idx] > lst[jdx]:
            lst[idx], lst[jdx] = lst[jdx], lst[idx]
        jdx += 1
    idx += 1

print(lst)

with open('draft.txt') as f:
    # lấy nội dung của file dưới dạng một list
    data = f.readlines()

idx = 0 # mốc bắt đầu
length = len(data) # mốc kết thúc
new_content = '' # nội dung mới sẽ ghi vào file mới

while idx < length:
    # tách một dòng thành một list
    line_list = data[idx].split()
    idx_line = 0
    length_line = len(line_list)
    while idx_line < length_line:
        if line_list[idx_line] == 'Kteam':
            # thay thế chữ trước Kteam là How
            line_list[idx_line - 1] = 'How'
        idx_line += 1
    # nối lại thành một dòng chuỗi
    new_content += ' '.join(line_list) + '\n'
    idx += 1

with open('kteam.txt', 'w') as new_f:
    # ghi nội dung mới vào file kteam.txt
    new_f.write(new_content)

print(new_content)