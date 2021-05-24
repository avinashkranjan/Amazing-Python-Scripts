from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, a, b):
        super().__init__()
        self.color("White")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=a, y=b)

    # to function the upward movement
    def GoUp(self):
        self.goto(self.xcor(), self.ycor() + 20)

    # to function the downward movement
    def GoDown(self):
        self.goto(self.xcor(), self.ycor() - 20)
