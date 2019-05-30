import turtle

# k = int(input('What number?'))

def week_day(k):
    weekday = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    for i in range (len(weekday)):
        if k % 7 == i:
            wd = weekday[i]
            return wd
        else:
            pass

# day_number = int(input('Day number?'))
# starting_day= int(input('Starting day?'))
# k = day_number + starting_day

# print('You will return on ' + str(week_day(k)))

# mark = float(input('Mark?'))

def grade(mark):
    if mark > 100 or mark < 0:
        result = 'mark out of range'
    else:
        if mark >= 75:
            result = 'First'
        elif mark >= 70 and mark < 75:
            result = 'Upper Second'
        elif mark >= 60 and mark < 70:
            result = 'Second'
        elif mark >= 50 and mark < 60:
            result = 'Third'
        elif mark >= 45 and mark < 50:
            result = 'F1 Supp'
        elif mark >= 40 and mark < 45:
            result = 'F2'
        else:
            result = 'F3'
    return result
# xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

# for i in range(len(xs)):
#     # print(str(grade(xs[i])))
#     print('Mark ' + str(xs[i]) + ' Grade: ' + str(grade(xs[i])))

xs = [-48,117,-200,240,160,260,220]

def draw_bar(t, height):
    t.begin_fill()
    t.left(90)
    t.fd(height)

    t.penup()
    if height < 0:
        t.fd(-15)
    t.write(' ' + str(height))
    if height < 0:
        t.fd(15)
    t.pendown()

    t.right(90)
    t.fd(40)
    t.right(90)
    t.fd(height)
    t.left(90)
    t.end_fill()
    t.penup()
    t.fd(10)
    t.pendown()

# tess = turtle.Turtle()
# tess.pensize(3)

# for v in xs:
#     if v >= 200:
#         tess.color('blue','red')
#         draw_bar(tess, v)
#     elif v >= 100 and v < 200:
#         tess.color('blue','yellow')
#         draw_bar(tess, v)
#     else:
#         tess.color('blue','green')
#         draw_bar(tess, v)

def find_hypot(a,b):
    c = (a ** 2 + b ** 2) ** 0.5
    return c

# print(find_hypot(4,3))

def is_rightangled(a, b, c):
    return (a**2 + b**2) == c**2 or (a**2 + c**2) == b**2 or (b**2 + c**2) == a**2

import math
a = math.sqrt(2.0)
print(a, a*a)
print(a*a == 2.0)
# print(is_rightangled(5,3,4))

# turtle.mainloop()