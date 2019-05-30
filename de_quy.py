# đệ quy: chỉ đơn giản là việc chính nó gọi nó.

def cal_sum(lst):
    print(lst)
    if not lst: # tương đương if len(lst) == 0
        return 0
    else:
        return lst[0] + cal_sum(lst[1:])
print(cal_sum([1,2,3,4]))

'''
ta liên tục gọi lại hàm cal_sum với argument là phần còn lại của List tính từ index 1.
Ở mỗi lần gọi hàm, ta để lại giá trị index 0 ở List để khi trong List không còn phần tử nào ta sẽ trả về số 0 để kết thúc đệ quy.
'''

# ternary expression:
# def cal_sum(lst):
#    return 0 if not lst else lst[0] + cal_sum(lst[1:])

# giảm bớt xuống còn n lần return bằng cách:
# def cal_sum(lst):
#    return lst[0] if len(lst) == 1 else lst[0] + cal_sum(lst[1:])
# cách này không sử dụng được trong trường hợp container rỗng

# Hoặc ta có thể sử dụng packing argument:
# def cal_sum(lst):
#    idx0, *r = lst # idx0, r = lst[0], lst[1:]
#    return idx0 if not r else idx0 + cal_sum(r)
# cách này cũng không sử dụng được khi container là rỗng.
# Tuy nhiên điểm lợi của nó cũng như cách vừa nãy là ta có thể cộng không chỉ số mà là chuỗi, hoặc list
# cal_sum(['a', 'b', 'c'])
# cal_sum([[1, 2], [3, 4], [5, 6]])


# Đệ quy cũng có thể chuyển hướng
# Một hàm gọi một hàm khác, sau đó lại gọi lại hàm đã gọi nó.
# def cal_sum(lst):
#    if not lst: return 0
#    return call_cal_sum(lst)
# def call_cal_sum(lst):
#    return lst[0] + cal_sum(lst[1:])

'''đệ quy còn thua vòng lặp ở mặt hiệu quả về bộ nhớ và thời gian thực hiện.
'''

