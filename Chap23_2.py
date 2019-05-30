
import turtle
'''
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
'''
class TurtleGTX:
    def __init__(self, name = ''):
        from turtle import Turtle
        self.odometer = 0
        self.name = name
        self.turtle = Turtle()
    def forward(self, distance):
        try:
            if self.odometer > 1000:
                raise ValueError("Need to switch for a new tyre")
            if distance > 0:
                self.odometer += distance
                self.turtle.forward(distance)
            if distance < 0:
                self.odometer += distance*(-1)
                self.turtle.backward(distance*(-1))
        except:
      	  	print("Need to switch for a new tyre")

    def change_tyre(self):
      	self.odometer = 0

t = TurtleGTX("tess")
t.forward(10000)

turtle.mainloop()
