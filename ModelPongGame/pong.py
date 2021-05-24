import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

scr = t.Screen()
GameOn = True
# Setting up the screen of the game
scr.setup(height=600, width=800)
scr.bgcolor("Black")
scr.tracer(0)  # To turn off the animation

# Positioning the left and the right paddles
LeftSide = Paddle(-300, 0)
RightSide = Paddle(300, 0)

ball = Ball()
scoreboard = Scoreboard()

# Adding Event Listeners
scr.listen()
scr.onkeypress(key="Up", fun=RightSide.GoUp)
scr.onkeypress(key="Down", fun=RightSide.GoDown)
scr.onkeypress(key="w", fun=LeftSide.GoUp)
scr.onkeypress(key="s", fun=LeftSide.GoDown)

# Setting up the game
while GameOn:
    time.sleep(0.05)  # to visualise the running movement of the ball
    scr.update()  # to update the screen animation while the game is running
    ball.move()  # to move the ball in the x and the y directions

    # to make the ball bounce from the ceiling and the floor
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # to make the ball bounce from the paddle
    if ball.xcor() > 270 and ball.distance(RightSide) < 50 or ball.xcor() < -270 and ball.distance(LeftSide) < 50:
        ball.bounce_paddle()

    # to update the scores everytime the ball hits the screen
    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.bounce_paddle()
        scoreboard.left_score += 1
        scoreboard.update()

    if ball.xcor() < -380:
        ball.goto(0, 0)
        ball.bounce_paddle()
        scoreboard.right_score += 1
        scoreboard.update()

scr.exitonclick()
