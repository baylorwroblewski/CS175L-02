#Baylor Wroblewski
#CS 175L
#Turtle Stop Sign

import math
import turtle

# Named constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10

s = LENGTH
x = s/math.sqrt(2)
diameter = s + (2 * x)

#sign outer red
turtle.begin_fill()
turtle.color("red")
turtle.penup()
turtle.goto(-50, 125)
turtle.pendown()

for x in range(NUM_SIDES):
    turtle.forward(100)
    turtle.right(ANGLE)
turtle.end_fill()

#sign inner white
turtle.begin_fill()
turtle.color("white")
turtle.penup()
turtle.goto(-47, 117)
turtle.pendown()

for x in range(NUM_SIDES):
    turtle.forward(93)
    turtle.right(ANGLE)
turtle.end_fill()

#sign inner red
turtle.begin_fill()
turtle.color("red")
turtle.penup()
turtle.goto(-43, 105)
turtle.pendown()

for x in range(NUM_SIDES):
    turtle.forward(85)
    turtle.right(ANGLE)

#words
turtle.end_fill()
turtle.penup()
turtle.pendown()
turtle.goto(0,-25)
turtle.color("white")
turtle.write("STOP", align = "center", font=("Calabri", 35, "bold"))

