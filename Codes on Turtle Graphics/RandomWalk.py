import turtle
import turtle as t
import random

# Declaring colors
ColorList = ["snow", "salmon", "pale turquoise", "lime green", "sandy brown"]
tim = turtle.Turtle()
tim.pensize(15)
tim.speed("fastest")
for i in range(300):
    tim.forward(30)
    tim.color(random.choice(ColorList))
    tim.setheading(random.choice([0, 90, 180, 270]))
scr = t.Screen()
scr.exitonclick()
