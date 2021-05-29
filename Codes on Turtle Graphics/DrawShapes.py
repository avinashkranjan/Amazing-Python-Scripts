import turtle as t
import random

tim = t.Turtle()
ColorList = ["pink", "salmon", "pale turquoise", "lime green", "sandy brown"]


def draw_shape(sides):
    for ind in range(sides):
        # Getting the angle of a regular polygon
        angle = 360 / sides
        tim.forward(100)
        tim.right(angle)


for i in range(3, 11):
    tim.color(random.choice(ColorList))
    draw_shape(i)
scr = t.Screen()
scr.exitonclick()
