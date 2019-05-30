import turtle

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
# tess = make_turtle("hotpink", 2)

xs = [48,117,200,240,160,260,220]

def draw_bar(t, height):
    t.begin_fill()
    t.left(90)
    t.fd(height)
    t.write(' ' + str(height))
    t.right(90)
    t.fd(40)
    t.right(90)
    t.fd(height)
    t.left(90)
    t.end_fill()
    t.penup()
    t.fd(10)
    t.pendown()

tess = turtle.Turtle()
tess.color('blue','red')
tess.pensize(3)

for v in xs:
    draw_bar(tess, v)

turtle.mainloop()