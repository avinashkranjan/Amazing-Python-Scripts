from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove = 10
        self.ymove = 10

    # to move the ball in the x and the y directions
    def move(self):
        self.goto(self.xcor() + self.xmove, self.ycor() + self.ymove)

    # to make the ball bounce from the ceiling and the floor
    def bounce(self):
        self.ymove = -1 * self.ymove

    # to make the ball bounce from the paddle
    def bounce_paddle(self):
        self.xmove = -1 * self.xmove
