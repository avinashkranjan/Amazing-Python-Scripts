from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 270)
        self.update()

    # Showing the level number
    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", font=("", 10, ""))

    # Showing the "GAME OVER"
    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER", align="center", font=("", 20, ""))
