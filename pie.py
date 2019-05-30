import turtle
import math

bob = turtle.Turtle()


def triangle(t,r,delta):
    angle = float(360) / delta
    s = 2 * r * math.sin(angle * math.pi / 360)
    t.fd(r)
    t.lt(90 + angle / 2)
    t.fd(s)
    t.lt(90 + angle / 2)
    t.fd(r)

def pie(t,r,delta):
    for i in range(delta):
        triangle(t,r,delta) 
        t.lt(180)

pie(bob,100,6)

bob.hideturtle()

turtle.mainloop()

print(bob)