import turtle as t

tim = t.Turtle()
scr = t.Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def clockwise():
    tim.setheading(tim.heading() - 10)


def anticlockwise():
    tim.setheading(tim.heading() + 10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


scr.listen()  # giving instructions for movements
scr.onkey(key="f", fun=move_forward)  # f for forward
scr.onkey(key="d", fun=move_backward)  # d for backward
scr.onkeypress(key="c", fun=clockwise)  # c for clockwise movement
scr.onkeypress(key="a", fun=anticlockwise)  # a for anticlockwise movement
scr.onkey(key="x", fun=clear)
scr.exitonclick()
