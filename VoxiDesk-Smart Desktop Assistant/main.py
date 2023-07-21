import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import geocoder
import pyautogui

import turtle
import random

import pygame
import pygame.camera

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


talk('Hello buddy , What can i help you')


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'nova' in command:
                command = command.replace('nova', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)

    # play song on youtube
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    # Current time
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('Current time is ' + time)

    # wikipedia answer
    elif 'what is' in command:
        person = command.replace('See', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'tell me' in command:
        person = command.replace('See', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'who is' in command:
        person = command.replace('See', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)

    # fun with nova
    elif 'i love you' in command:
        talk('i love you too')
    elif 'what are you doing' in command:
        talk('I am talking to you')
    elif 'are you single' in command:
        talk('I am relationship with wifi')

    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())

    # current location
    elif 'location' in command:
        g = geocoder.ip('me')
        print(g.city)
        talk('your current location is' + g.city)

    # take a screen shot
    elif 'screenshot' in command:
        im = pyautogui.screenshot()
        im.save("SS1.jpg")

    # Take some photo
    elif 'take a photo' in command:
        pygame.camera.init()
        camlist = pygame.camera.list_cameras()
        if camlist:
            cam = pygame.camera.Camera(camlist[0], (640, 480))
            cam.start()
            image = cam.get_image()
            pygame.image.save(image, "filename.jpg")
        else:
            print("No camera on current device")

    # play snake game
    elif 'snake game' in command:
        w = 500
        h = 500
        food_size = 10
        delay = 100

        offsets = {
            "up": (0, 20),
            "down": (0, -20),
            "left": (-20, 0),
            "right": (20, 0)
        }

        def reset():
            global snake, snake_dir, food_position, pen
            snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
            snake_dir = "up"
            food_position = get_random_food_position()
            food.goto(food_position)
            move_snake()

        def move_snake():
            global snake_dir

            new_head = snake[-1].copy()
            new_head[0] = snake[-1][0] + offsets[snake_dir][0]
            new_head[1] = snake[-1][1] + offsets[snake_dir][1]

            if new_head in snake[:-1]:
                reset()
            else:
                snake.append(new_head)

                if not food_collision():
                    snake.pop(0)

                if snake[-1][0] > w / 2:
                    snake[-1][0] -= w
                elif snake[-1][0] < - w / 2:
                    snake[-1][0] += w
                elif snake[-1][1] > h / 2:
                    snake[-1][1] -= h
                elif snake[-1][1] < -h / 2:
                    snake[-1][1] += h

                pen.clearstamps()

                for segment in snake:
                    pen.goto(segment[0], segment[1])
                    pen.stamp()

                screen.update()

                turtle.ontimer(move_snake, delay)

        def food_collision():
            global food_position
            if get_distance(snake[-1], food_position) < 20:
                food_position = get_random_food_position()
                food.goto(food_position)
                return True
            return False

        def get_random_food_position():
            x = random.randint(- w / 2 + food_size, w / 2 - food_size)
            y = random.randint(- h / 2 + food_size, h / 2 - food_size)
            return (x, y)

        def get_distance(pos1, pos2):
            x1, y1 = pos1
            x2, y2 = pos2
            distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
            return distance

        def go_up():
            global snake_dir
            if snake_dir != "down":
                snake_dir = "up"

        def go_right():
            global snake_dir
            if snake_dir != "left":
                snake_dir = "right"

        def go_down():
            global snake_dir
            if snake_dir != "up":
                snake_dir = "down"

        def go_left():
            global snake_dir
            if snake_dir != "right":
                snake_dir = "left"

        screen = turtle.Screen()
        screen.setup(w, h)
        screen.title("Snake")
        screen.bgcolor("blue")
        screen.setup(500, 500)
        screen.tracer(0)

        pen = turtle.Turtle("square")
        pen.penup()

        food = turtle.Turtle()
        food.shape("square")
        food.color("yellow")
        food.shapesize(food_size / 20)
        food.penup()

        screen.listen()
        screen.onkey(go_up, "Up")
        screen.onkey(go_right, "Right")
        screen.onkey(go_down, "Down")
        screen.onkey(go_left, "Left")

        reset()
        turtle.done()

    # any command doesn't match nova talk this line
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
