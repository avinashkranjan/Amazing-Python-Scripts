from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update()

   # to update the points of the players
    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("courier", 60, "normal"))
