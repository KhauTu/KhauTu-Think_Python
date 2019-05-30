import turtle
import math

bob = turtle.Turtle()

r1 = 0.1
r2 = 0.1

def quarter(t,r):
    length = 2 * math.pi * r
    angle = 120
    n = int(length / 2) + 1
    step_length = length / n
    step_angle = float(angle) / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

for i in range(100):
    r3 = r1 + r2
    r1 = r2
    r2 = r3
    quarter(bob,r3)

turtle.mainloop()