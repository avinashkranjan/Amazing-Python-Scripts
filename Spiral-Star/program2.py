from turtle import *
import random

speed(speed='fastest')


def draw(n, x, angle):
    # loop for number of stars
    for i in range(n):

        colormode(255)

        # choosing random integers
        # between 0 and 255
        # to generate random rgb values
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)

        # setting the outline
        # and fill colour
        pencolor(a, b, c)
        fillcolor(a, b, c)

        # begins filling the star
        begin_fill()

        # loop for drawing each star
        for j in range(5):

            forward(5 * n - 5 * i)
            right(x)
            forward(5 * n - 5 * i)
            right(72 - x)

        # colour filling complete
        end_fill()

        # rotating for
        # the next star
        rt(angle)


# setting the parameters
n = 30  # number of stars
x = 144  # exterior angle of each star
angle = 18  # angle of rotation for the spiral

draw(n, x, angle)
