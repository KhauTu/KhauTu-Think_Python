# while expression:
     # while-block
'''
k = 5
while k > 0:
    print('k = ', k)
    k -= 1
'''
'''
s = 'How Kteam'
idx = 0
length = len(s)

while idx < length:
    print(idx, 'stands for', s[idx])
    idx += 1
'''
'''
five_even_numbers = []
k_number = 1

while True: # vòng lặp vô hạn vì giá trị này là hằng nên ta không thể tác động được
    if k_number % 2 == 0: # nếu k_number là một số chẵn
        five_even_numbers.append(k_number) # thêm giá trị của k_number vào list
        if len(five_even_numbers) == 5: # nếu list này đủ 5 phần tử
            break # thì kết thúc vòng lặp
    k_number += 1
print(five_even_numbers)
print(k_number)
'''
'''
k_number = 0
while k_number < 10:
    k_number += 1
    if k_number % 2 == 0: # nếu k_number là số chẵn
        continue
    print(k_number, 'is odd number')
print(k_number)
'''
'''
while expression:
    # while-block

else:
    # else-block
'''
'''
k = 0
while k < 3:
    print('value of k is', k)
    k += 1
else:
    print('k is not less than 3 anymore')
'''
# Trong trường hợp trong while-block chạy câu lệnh break thì vòng lặp while sẽ kết thúc và phần else-block cũng sẽ không được thực hiện.

draft = '''an so dfn Kteam odsa in fasfna Kteam mlfjier
as dfasod nf ofn asdfer fsan dfoans ldnfad Kteam asdfna
asdofn sdf pzcvqp Kteam dfaojf kteam dfna Kteam dfaodf
afdna Kteam adfoasdf ncxvo aern Kteam dfad'''
kteam = []

# Khởi tạo file draft.txt
with open('draft.txt','w') as d:
    print(draft, file = d)

# đọc từng dòng trong draft.txt
with open('draft.txt') as d:
    line = d.readlines()
    # print(len(line))

    for i in range(len(line)):
        print(line[i])
        # đưa từng line về dạng list, ngăn cách bằng space ' '
        line_list = line[i].split(sep = ' ')
        print(line_list)
        k = 0
        while k < len(line_list):
            # thay thế 'Kteam' bằng 'How Kteam' nếu từ đầu tiên của list là 'Kteam'            
            if line_list[k] == "Kteam":
                # print(line_list[k-1])
                if k-1 < 0:
                    line_list[k] = "How Kteam"
                # thay thế từ đứng trước 'Kteam' bằng 'How' nếu 'Kteam' không đứng đầu list
                else:
                    line_list[k-1] = "How"
                k += 1
            else: k += 1
        # nối các từ trong list thành line mới
        new_line = ' '.join(line_list)
        print(new_line)
        # cho new line vào trong list kteam
        kteam.append(new_line)
# Nối các line trong list kteam thành đoạn văn bản
# print(''.join(kteam))
with open('kteam.txt','w') as f:
    print(''.join(kteam), file = f)



# thay thế xuống dòng \n bằng dấu cách space
# draft = draft.replace('\n',' ')

# đưa về dạng list
# draft_list = draft.split(sep = ' ')


# print(draft_list)
# print(data)
# print(kteam)