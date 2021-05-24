import time
from turtle import Screen
from player import Player
from car import Car
from scoreboard import Scoreboard

# Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
# Removing animations
screen.tracer(0)

player = Player()
car = Car()
scoreboard = Scoreboard()

# Declaring event listeners
screen.listen()
screen.onkeypress(player.go_up, "Up")

# Playing the game
game_running = True
while game_running:
    time.sleep(0.1)
    screen.update()

    car.generate()
    car.move()

    # Detecting collision with car
    for car in car.car_list:
        if car.distance(player) < 20:
            game_running = False
            scoreboard.game_over()

    # Detecting successful crossing to the other end
    if player.ycor() > 280:
        player.goto(0, -250)
        car.start += 10
        scoreboard.level += 1
        scoreboard.update()

screen.exitonclick()
