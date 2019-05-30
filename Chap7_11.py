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

drunk = [(160, 200), (-43, 100), (270, 80), (-43, 120)]
for (angle, step) in drunk:
    tess.left(angle)
    tess.fd(step)

turtle.mainloop()