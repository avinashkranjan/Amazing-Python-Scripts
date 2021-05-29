import turtle as t

tim = t.Turtle()
for i in range(20):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
scr = t.Screen()
scr.exitonclick()
