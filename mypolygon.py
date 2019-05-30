import turtle
import math
bob = turtle.Turtle()

def square(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
    print(t)

# square(bob,200)

def polyline(t, n, length, angle):
    """Draws n line segments with the given length
    and angle (in degrees) between them. t is turtle.
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)
    print(t)

def polygon(t,n,length):
    angle = 360.0 / n
    polyline(t,n,length,angle)

    
# polygon(bob, n=10, length=100)

# def circle(t,r): # r is radius (ban kinh)
#     circum = 2 * math.pi * r
#     n = int(circum / 3) + 1
#     length = circum / n # length approximately equals to 3, small enough
#     polygon(t,n,length)

# circle(bob,100)

def arc(t,r,angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t,n,step_length,step_angle)
    # t.rt(step_angle / 2)

def circle(t,r):
    arc(t,r,360)

circle(bob,50)

'''if __name__ == '__main__':
    bob = turtle.Turtle()

    # draw a circle centered on the origin
    radius = 100
    bob.pu() # pen up
    bob.fd(radius)
    bob.lt(90)
    bob.pd() # pen down
    circle(bob, radius)

    # wait for the user to close the window
    turtle.mainloop()'''

turtle.mainloop()