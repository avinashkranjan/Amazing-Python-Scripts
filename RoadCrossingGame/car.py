from turtle import Turtle
import random


class Car(Turtle):
    car_list = []
    start = 5

    def __init__(self):
        super().__init__()
        # Creating a car
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(-350, random.randint(-220, 250))
        self.speed(self.start)

    # Generating a train of cars
    def generate(self):
        rand_chance = random.randint(1, 6)
        if rand_chance == 1:
            car = Car()
            self.car_list.append(car)

    # Moving all the generated cars
    def move(self):
        for car in self.car_list:
            car.forward(10)
