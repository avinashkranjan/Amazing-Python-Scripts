import turtle as t
import random
import time

scr = t.Screen()
scr.setup(width=500, height=500)
UserInput = scr.textinput(title="Play luck",
                          prompt="Who would win in your opinion??Enter your lucky color from rainbow")
# declaring a list of colors
ColorList = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
RaceRunning = False
Runners = []
pos = -100
# for each and every turtle
for i in range(0, 7):
    NewTurtle = t.Turtle()
    NewTurtle.shape("turtle")
    NewTurtle.penup()
    NewTurtle.color(ColorList[i])
    NewTurtle.goto(x=-250, y=pos)
    pos += 50
    Runners.append(NewTurtle)
if UserInput:
    RaceRunning = True
    # till the game is running
while RaceRunning:
    for runner in Runners:
        if runner.xcor() > 230:
            winner = runner.pencolor()
            RaceRunning = False
            show = t.Turtle()
            show.hideturtle()
            show.penup()
            show.goto(-200, -150)
            show.color("red")
            if winner.lower() == UserInput.lower():
                print("Your turtle won!")
                show.write("Your turtle won!")
            else:
                print(f"Your turtle lost, the winner is {winner} turtle!")
                show.write(f"Your turtle lost, the winner is {winner} turtle!")
        runner.forward(random.randint(0, 10))
scr.exitonclick()
