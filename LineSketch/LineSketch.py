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


scr.listen()
scr.onkey(key="f", fun=move_forward)
scr.onkey(key="d", fun=move_backward)
scr.onkeypress(key="c", fun=clockwise)
scr.onkeypress(key="a", fun=anticlockwise)
scr.onkey(key="x", fun=clear)
scr.exitonclick()
