import turtle
import math

bob = turtle.Turtle()

# leaf = 7
# length = 200

def side(t,step_length,step_angle,n,angle):
    for i in range(2):
        for i in range(n):
            t.fd(step_length)
            t.lt(step_angle)
        t.lt(180 - angle)

def one_leaf(t,length, angle):
    n = int(length / 2) + 1
    step_length = length / n
    step_angle = float(angle) / n
    side(t,step_length,step_angle,n,angle)
    

# one_leaf(200, 360 / 7)
def flower(t,length, leaf):
    angle = 360 / leaf
    for i in range(leaf):
        one_leaf(t,length, angle)
        bob.lt(angle)

flower(bob,200,20)

turtle.mainloop()