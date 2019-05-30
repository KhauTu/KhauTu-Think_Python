import turtle # Allows us to use turtles
import math

def make_window(colr, ttle):
    w = turtle.Screen() # Creates a playground for turtles
    w.bgcolor(colr)
    w.title(ttle)
    return w

def make_turtle(colr, sz):
    t = turtle.Turtle() # Create a turtle, assign to t
    t.color(colr)
    t.pensize(sz)
    return t

wn = make_window("lightgreen", "Tess and Alex dancing")
tess = make_turtle("hotpink", 2)

def square(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
    print(t)

def next_square(no_of_square,size):
    for i in range(no_of_square):
        square(tess,size)
        tess.penup()
        tess.fd(40)
        tess.pendown()

# next_square(5)

def inner_square(no_of_square,size):
    for i in range(no_of_square):
        square(tess,size * (i+1))
        tess.penup()
        tess.right(90)
        tess.fd(size / 2)
        tess.right(90)
        tess.fd(size / 2)
        tess.right(180)
        tess.pendown()

# inner_square(6,25)

def draw_poly(t,n,sz):
    for i in range(n):
        t.fd(sz)
        t.left(360 / n)

# draw_poly(tess,9,50)

def spiral(angle):
    for i in range(50):
        tess.right(angle)
        i += 1
        tess.fd(i * 5)
        tess.right(angle)
        tess.fd(i * 5)

# spiral(88)
def sum_to(n):
    sum = 0
    for i in range(n + 1):
        sum = sum + i
    return sum

# print(sum_to(10))

def area_of_circle(r):
    area = math.pi * (r) ** 2
    return area

def star():
    for i in range(5):
        tess.fd(100)
        tess.right(360 * 2 / 5)
'''
for i in range(5):
    star()
    tess.penup()
    tess.fd(350)
    tess.right(360 * 2 / 5)
    tess.pendown()
'''
# draw_poly(tess, 12, 30)

''' # Ex 7:
turn = [160, -43, 270, -97, -43, 200, -940, 17, -86]
for i in turn:
        tess.left(i)
        tess.fd(100)
        # print(tess.heading()) # the .heading() method gives us the turtle's current heading in degrees
'''

# draw_poly(tess, 12, 30)
tess.right(90)
for i in range(12):
        tess.penup()
        tess.fd(100)
        tess.pendown()
        tess.fd(20)
        tess.left(180)
        tess.penup()
        tess.fd(120)
        tess.right(180)
        tess.left(360 / 12)

# print_t("We like Python's turtles!", 1000)
turtle.mainloop()