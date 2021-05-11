import pygame
import utility as util

# for displaying health we need text
pygame.font.init()

# width, height = 900, 500
WINDOW = pygame.display.set_mode((util.width, util.height))
pygame.display.set_caption("Spaceship War Game")

# Creating user event so that we can came to know if the bullet collides, diff number indicates diff events
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2


def drawWindow(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health,
               YELLOW_SPACESHIP, RED_SPACESHIP, SPACE, BORDER):
    """
    This functions gives displays the graphics of the Game which includes
    both the spaceship, background space image, bullets, and health of players
    with 60 Frames per second.
    :param red: Bounding rectangle of Red Spaceship
    :param yellow: Bounding rectangle of Yellow Spaceship
    :param red_bullets: Bullets fired by red spaceship
    :param yellow_bullets: Bullets fired by Yellow spaceship
    :param red_health: Health of Red Player
    :param yellow_health: Health of Yellow Player
    :param YELLOW_SPACESHIP: Red Spaceship Image
    :param RED_SPACESHIP: Yellow Spaceship Image
    :param SPACE: Space Background Image
    :param BORDER: Center border
    """
    # ORDER IN WHICH DRAW THINGS MATTER REMEMBER
    WINDOW.blit(SPACE, (0, 0))

    # Adding border created above
    pygame.draw.rect(WINDOW, (255, 255, 255), BORDER)

    # to indicate health
    HEALTH_FONT = pygame.font.SysFont('comicsans', 40)

    # Displaying Health by font
    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), True, (255, 255, 255))
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), True, (255, 255, 255))
    WINDOW.blit(red_health_text, (util.width - red_health_text.get_width() - 10, 10))
    WINDOW.blit(yellow_health_text, (10, 10))

    # to load surfaces we use blit
    WINDOW.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))

    WINDOW.blit(RED_SPACESHIP, (red.x, red.y))

    # Drawing bullets
    for bullet in red_bullets:
        pygame.draw.rect(WINDOW, (255, 0, 0), bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WINDOW, (255, 255, 0), bullet)

    pygame.display.update()


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    """
    This function moves the bullet forward with a specific Bullet velocity
    and at a time only 3 bullets can be fired by the user.
    It also checks weather the bullet has hit the spaceship by using collidirect
    function, so that we can decrease the health of that player.
    :param yellow_bullets: Bullets fired by red spaceship
    :param red_bullets: Bullets fired by red spaceship
    :param yellow: Bounding rectangle of Yellow Spaceship
    :param red: Bounding rectangle of Red Spaceship
    """
    # Bullet velocity
    BULLET_VEL = 7

    # To check weather the bullet hit red or yellow spaceship or they fly through the skin
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL

        # colliddirect only works if both are rectangle
        if red.colliderect(bullet):
            # Now we are going to post a event then check in the main function for the event
            # it will indicate us that the bullet hit the spaceship
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > util.width:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL

        # colliddirect only works if both are rectangle
        if yellow.colliderect(bullet):
            # Now we are going to post a event then check in the main function for the event
            # it will indicate us that the bullet hit the spaceship
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def main():
    """
    Main logic of the game, This function makes everything work together.
    1. Load the assets
    2. Reads input from the keyboard
    3. Making bullets fire
    4. Handling bullet movements
    5. Displaying everything together on the screen.
    6. Showing the winner
    7. Again restarting the game after 5 sec.
    """
    # Loading Assets
    YELLOW_SPACESHIP, RED_SPACESHIP, SPACE, BORDER = util.load_assests()

    # Making two rectangles so that we can control where our spaceship are moving
    SPACESHIP_WIDTH, SPACESHIP_HEIGHT = (50, 40)
    red = pygame.Rect(700, 250, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 250, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    # To making our game refresh at a constant interval
    clock = pygame.time.Clock()

    # To storing our bullet location in pixels so that we can move it
    yellow_bullets = []
    red_bullets = []

    # Healths of our spaceships
    red_health = 10
    yellow_health = 10

    run = True

    while run:
        # Capped frame rate so it remains consistent on diff computers
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            # checking if key pressed for firing bullet
            if event.type == pygame.KEYDOWN:

                # maximum amount of bullets a spaceship can shoot at a time
                MAX_BULLETS = 3
                # CHECKING if we press LCTRL and we have 3 bullets at a time on a screen
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    # 10, 5 width, height of bullet and others are location
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2 - 2, 10, 5)
                    yellow_bullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 10, 5)
                    red_bullets.append(bullet)

            # If bullets hit red spaceship then decrease health
            if event.type == RED_HIT:
                red_health -= 1
            # If bullets hit yellow spaceship then decrease health
            if event.type == YELLOW_HIT:
                yellow_health -= 1

        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins!!"
        if yellow_health <= 0:
            winner_text = "Red Wins!!"
        if winner_text != "":
            util.winner(winner_text, WINDOW)
            break

        # Checking which keys are pressed while the game is running it also checks if the
        # keys are pressed and remain down
        keys_pressed = pygame.key.get_pressed()
        # Spaceship velocity
        VELOCITY = 5
        # Function that handle key movements of yellow and red spaceship and bullets
        util.yellow_handle_movement(keys_pressed, yellow, VELOCITY, BORDER)
        util.red_handle_movement(keys_pressed, red, VELOCITY, BORDER)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        # Displaying everything on the screen.
        drawWindow(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health,
                   YELLOW_SPACESHIP, RED_SPACESHIP, SPACE, BORDER)

    main()


if __name__ == "__main__":
    main()
