import turtle

# Create the turtle screen
screen = turtle.Screen()
screen.title("Indian National Flag Animation")
screen.bgcolor("white")

# Set up the turtle object
flag_turtle = turtle.Turtle()
flag_turtle.speed(2)
flag_turtle.penup()

# Draw the orange rectangle (top band)
flag_turtle.goto(-200, 150)
flag_turtle.color("#FF9933")
flag_turtle.begin_fill()
for _ in range(2):
    flag_turtle.forward(400)
    flag_turtle.right(90)
    flag_turtle.forward(50)
    flag_turtle.right(90)
flag_turtle.end_fill()

# Draw the white rectangle (middle band)
flag_turtle.goto(-200, 100)
flag_turtle.color("white")
flag_turtle.begin_fill()
for _ in range(2):
    flag_turtle.forward(400)
    flag_turtle.right(90)
    flag_turtle.forward(50)
    flag_turtle.right(90)
flag_turtle.end_fill()

# Draw the green rectangle (bottom band)
flag_turtle.goto(-200, 50)
flag_turtle.color("#138808")
flag_turtle.begin_fill()
for _ in range(2):
    flag_turtle.forward(400)
    flag_turtle.right(90)
    flag_turtle.forward(50)
    flag_turtle.right(90)
flag_turtle.end_fill()

# Draw the Ashoka Chakra (blue circle)
flag_turtle.goto(0, 75)
flag_turtle.color("navy")
flag_turtle.pendown()
flag_turtle.begin_fill()
flag_turtle.circle(30)
flag_turtle.end_fill()

# Draw the 24 spokes of the Ashoka Chakra (saffron color)
flag_turtle.penup()
flag_turtle.goto(0, 105)
flag_turtle.color("#FF9933")
flag_turtle.pensize(2)
for _ in range(24):
    flag_turtle.pendown()
    flag_turtle.forward(30)
    flag_turtle.backward(30)
    flag_turtle.right(15)

# Hide the turtle cursor
flag_turtle.hideturtle()

# Close the turtle graphics window on click
turtle.exitonclick()
