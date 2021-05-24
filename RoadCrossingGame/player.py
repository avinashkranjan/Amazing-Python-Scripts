from turtle import Turtle
class Player(Turtle):

    def __init__(self):
        # Creating a turtle
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -250)
        self.setheading(90)

    def go_up(self):
        self.forward(10)
