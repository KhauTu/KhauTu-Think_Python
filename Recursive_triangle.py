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

angles = [0, 120, 240]
colors = ["red", "blue", "magenta"]

def draw_equi_triang(t, size):
    for i in range(3):
        t.forward(size)
        t.left(120)

def shift_turtle(t, size, angle):

    # moves turtle to correct location to begin next triangle

    t.left(angle)
    t.penup()
    t.forward(size)
    t.pendown()
    t.right(angle)

def sierpinski(t, order, size, colorChangeDepth = -1):

    # draw an equilateral triangle at order 0

    if order == 0:
        draw_equi_triang(t, size)

    # otherwise, test if colorChangeDepth == 0 and when it does change the color

    else:
        if colorChangeDepth == 0:
            # get index of angles
            for (ind, angle) in enumerate (angles):
                t.color(colors[ind])
                sierpinski(t, order-1, size/2, colorChangeDepth-1)
                shift_turtle(t, size/2, angle)
        # if colorChangeDepth does not == 0 yet
        else:
            for angle in angles:
                sierpinski(t, order-1, size/2, colorChangeDepth-1)
                shift_turtle(t, size/2, angle)

sierpinski(tess, 5, 200, 1)

turtle.mainloop()