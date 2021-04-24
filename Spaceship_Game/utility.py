import pygame
import os

width, height = 900, 500


def load_assests():
    """
    Loading the spaceship images and manipulating them.
    and creating a centre border.
    :return: YELLOW_SPACESHIP, RED_SPACESHIP, SPACE, BORDER
    """
    # Loading spaceship images into our file known as surfaces as we use this above background
    spaceshipImageYellow = pygame.image.load(os.path.join("Assets", "Yellow_Spaceship.png"))
    spaceshipImageRed = pygame.image.load(os.path.join("Assets", "Red_Spaceship.png"))
    SPACE = pygame.image.load(os.path.join("Assets", "space.jpg"))

    # SCALING down the images
    SPACESHIP_WIDTH, SPACESHIP_HEIGHT = (50, 40)
    YELLOW_SPACESHIP = pygame.transform.scale(spaceshipImageYellow, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
    RED_SPACESHIP = pygame.transform.scale(spaceshipImageRed, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
    SPACE = pygame.transform.scale(SPACE, (900, 500))

    # ROTATING the images
    YELLOW_SPACESHIP = pygame.transform.rotate(YELLOW_SPACESHIP, 90)
    RED_SPACESHIP = pygame.transform.rotate(RED_SPACESHIP, -90)

    # BORDER in the middle of the window
    # starting coordinates then width and height of the border
    BORDER = pygame.Rect(width / 2 - 5, 0, 10, height)

    return YELLOW_SPACESHIP, RED_SPACESHIP, SPACE, BORDER


def yellow_handle_movement(keys_pressed, yellow, VELOCITY, BORDER):
    """
    This function takes the Bounding box of spaceship and with the keys pressed down on
    keyboard it moves the spaceship with a velocity. And by keeping in mind that it should not
    cross the border and should not go out of the frame.
    +------------------------------+
    |      KEYS      |    ACTION   |
    +----------------+-------------+
    |       A        |     LEFT    |
    |       D        |     RIGHT   |
    |       W        |     UP      |
    |       S        |     DOWN    |
    |   Left CTRL    |     FIRE    |   in handle_bullets function
    +----------------+-------------+
    :param keys_pressed: Gives which keys are pressed on keyboard.
    :param yellow: Bounding rectangle of yellow Spaceship.
    :param VELOCITY: Spaceship Velocity.
    :param BORDER: Center Border.
    """
    # and checking that it remains in the screen and dont cross the border
    if keys_pressed[pygame.K_a] and yellow.x - VELOCITY > 0:  # LEFT
        yellow.x -= VELOCITY
    elif keys_pressed[pygame.K_d] and yellow.x + VELOCITY + yellow.width < BORDER.x:  # RIGHT
        yellow.x += VELOCITY
    elif keys_pressed[pygame.K_w] and yellow.y - VELOCITY > 0:  # UP
        yellow.y -= VELOCITY
    elif keys_pressed[pygame.K_s] and yellow.y + VELOCITY + yellow.height < height - 15:  # DOWN
        yellow.y += VELOCITY


def red_handle_movement(keys_pressed, red, VELOCITY, BORDER):
    """
    This function takes the Bounding box of spaceship and with the keys pressed down on
    keyboard it moves the spaceship with a velocity. And by keeping in mind that it should not
    cross the border and should not go out of the frame.
    +------------------------------+
    |      KEYS      |    ACTION   |
    +----------------+-------------+
    |  Left Arrow    |     LEFT    |
    |  Right Arrow   |     RIGHT   |
    |  Up Arrow      |     UP      |
    |  Down Arrow    |     DOWN    |
    |  Right CTRL    |     FIRE    |  in handle_bullets function
    +----------------+-------------+
    :param keys_pressed: Gives which keys are pressed on keyboard.
    :param red: Bounding rectangle of Red Spaceship.
    :param VELOCITY: Spaceship Velocity.
    :param BORDER: Center Border.
    """
    if keys_pressed[pygame.K_LEFT] and red.x - VELOCITY > BORDER.x + BORDER.width + 8:  # LEFT
        red.x -= VELOCITY
    elif keys_pressed[pygame.K_RIGHT] and red.x + VELOCITY + red.width < width:  # RIGHT
        red.x += VELOCITY
    elif keys_pressed[pygame.K_UP] and red.y - VELOCITY > 0:  # UP
        red.y -= VELOCITY
    elif keys_pressed[pygame.K_DOWN] and red.y + VELOCITY + red.height < height - 15:  # DOWN
        red.y += VELOCITY


def winner(text, WIN):
    """
    # Displaying the winner on screen.
    :param text: Player name
    :param WIN: GUI Window to display text on
    """
    # Font
    FONT = pygame.font.SysFont('comicsans', 100)
    # Displaying the winner font on the screen.
    draw_text = FONT.render(text, 1, (255, 255, 255))
    WIN.blit(draw_text, (width / 2 - draw_text.get_width() / 2, height / 2 - draw_text.get_height() / 2))
    # Updating the display
    pygame.display.update()
    pygame.time.delay(5000)
