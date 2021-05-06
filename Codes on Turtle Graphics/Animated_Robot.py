import turtle as t
import time as ti


def rectangle(hor, ver, col):
    t.pendown()    # to create a canvas for drawing
    t.pensize(1)    # size of pen
    t.color(col)
    t.begin_fill()
    for counter in range(1, 3):
        t.forward(hor)
        t.right(90)  # move 90 degree right
        t.forward(ver)
        t.right(90)
    t.end_fill()
    t.penup()


t.penup()
t.speed('slow')
t.bgcolor('Dodger blue')    # give background color

t.goto(-100, -150)       # move the turtle to given coordinates
rectangle(50, 20, 'blue')    # create a rectangle of given size
t.goto(-30, -150)
rectangle(50, 20, 'blue')

t.goto(-25, -50)
rectangle(15, 100, 'grey')
t.goto(-55, -50)
rectangle(-15, 100, 'grey')

t.goto(-90, 100)
rectangle(100, 150, 'skyblue')

t.goto(-150, 70)
rectangle(60, 15, 'grey')
t.goto(-150, 110)
rectangle(15, 40, 'grey')
t.goto(10, 70)
rectangle(60, 15, 'grey')
t.goto(55, 110)
rectangle(15, 40, 'grey')

t.goto(-50, 120)
rectangle(15, 20, 'grey')
t.goto(-85, 170)
rectangle(80, 50, 'red')
t.goto(-60, 160)
rectangle(30, 10, 'white')
t.goto(-55, 155)
rectangle(5, 5, 'black')
t.goto(-40, 155)
rectangle(5, 5, 'black')
t.goto(-65, 138)
rectangle(40, 5, 'black')

ti.sleep(10)

t.hideturtle()
