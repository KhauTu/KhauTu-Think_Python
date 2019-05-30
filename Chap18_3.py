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
# tess.left(60)

angles = [0, 120, 240]
colors = ["red", "blue", "magenta"]

def tri_ang(t, size):
    """
        Make turtle t draw a Triangle with "size" each side.
    """
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

def Sier_ang(t, order, size, colorChangeDepth=-1):
    """
        Make turtle t draw a Sierpinski triangle of ’order’ and ’size’.
        Leave the turtle facing the same direction.
    """
    if order == 0: # draw an equilateral triangle at order 0
        tri_ang(t, size)

    else: # otherwise, test if colorChangeDepth == 0 and when it does change the color
        if colorChangeDepth == 0:
            # get index of angles
            for (ind, angle) in enumerate(angles):
                t.color(colors[ind])
                Sier_ang(t, order-1, size/2, colorChangeDepth - 1)
                shift_turtle(t, size/2, angle)
        else: # if colorChangeDepth does not == 0 yet
            for angle in angles:
                Sier_ang(t, order-1, size/2, colorChangeDepth - 1)
                shift_turtle(t, size/2, angle)

Sier_ang(tess, 5, 200, 0)

'''
for i in range(4):
    Sier_ang(tess, i, 100)
    tess.penup()
    tess.right(60)
    tess.forward(110)
    tess.left(60)
    tess.pendown()
'''
turtle.mainloop()