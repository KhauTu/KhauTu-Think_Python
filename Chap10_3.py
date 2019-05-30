import turtle # Tess becomes a traffic light.

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
yellow = turtle.Turtle()
red = turtle.Turtle()

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

draw_housing()

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)

yellow.penup()
yellow.forward(40)
yellow.left(90)
yellow.forward(120)

red.penup()
red.forward(40)
red.left(90)
red.forward(190)

# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

yellow.shape("circle")
yellow.shapesize(3)
yellow.fillcolor("yellow")
yellow.hideturtle()

red.shape("circle")
red.shapesize(3)
red.fillcolor("red")
red.hideturtle()

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess’ position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0

def advance_state_machine():
    global state_num
    if state_num == 0: # Transition from state 0 to state 1
        tess.fillcolor("darkgrey")
        yellow.showturtle()
        yellow.fillcolor("yellow")
        wn.ontimer(advance_state_machine, 1000)
        # tess.forward(70)
        # tess.fillcolor("yellow")
        state_num = 1
    elif state_num == 1: # Transition from state 1 to state 2
        yellow.fillcolor("darkgrey")
        red.showturtle()
        red.fillcolor("red")
        wn.ontimer(advance_state_machine, 2000)
        # tess.forward(70)
        # tess.fillcolor("red")
        state_num = 2
    elif state_num == 2: # Transition from state 2 to state 3
        red.fillcolor("darkgrey")
        tess.fillcolor("green")
        # tess.back(140)
        # tess.fillcolor("green")
        wn.ontimer(advance_state_machine, 3000)
        state_num = 3
    else: # Transition from state 3 to state 0
        yellow.fillcolor("yellow")
        wn.ontimer(advance_state_machine, 1000)
        state_num = 0

# Bind the event handler to the space key.
wn.onkey(advance_state_machine, "space")

wn.listen()

wn.mainloop()