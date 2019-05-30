import turtle
from math import *

def make_window(colr, ttle):
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w

def make_turtle(colr, sz):
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t

wn = make_window("lightgreen", "Tess and Alex dancing")
tess = make_turtle("hotpink", 2)

def koch_ang(t, order, size, ang):
    """
        Make turtle t draw a Koch fractal of ’order’ and ’size’.
        Leave the turtle facing the same direction.
    """
    ang_lst = [ang/2 - 90, 180 -  ang, ang/2 - 90, 0]
    if order == 0: # The base case is just a straight line
        t.forward(size)
    else:
        # size = size *1.5
        for angle in ang_lst:
            ang = ang
            koch_ang(t, order-1, size/3, ang)
            t.left(angle)

# koch_ang(tess, 2, 300)

def flake_angle(t, order, size, ang, n):
    for i in range(n):
        koch_ang(t, order, size, ang)
        t.left(-360/n)

size = 100
ang = 20
# print(1/(2/3 + 2/3 *sin(radians(ang/2))))

for i in range(4):
    flake_angle(tess, i, size, ang, 4)
    size = size * 1/(2/3 + 2/3 *sin(radians(ang/2)))
    print(size)
    tess.penup()
    tess.fd(100*(1.2))
    tess.pendown()

turtle.mainloop()
