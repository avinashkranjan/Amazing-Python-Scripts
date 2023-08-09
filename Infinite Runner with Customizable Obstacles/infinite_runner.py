import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Infinite Runner with Customizable Obstacles")

# Load sound effects and background music
pygame.mixer.music.load("background_music.mp3")
jump_sound = pygame.mixer.Sound("jump_sound.wav")
collision_sound = pygame.mixer.Sound("collision_sound.wav")

# Scoring
score = 0
font = pygame.font.Font(None, 36)

# Player attributes
player_width = 50
player_height = 50
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - player_height - 20
player_speed = 5

# Obstacle attributes
obstacle_width = 100
obstacle_height = 20
obstacle_speed = 5
obstacles = []

# Game loop
running = True
clock = pygame.time.Clock()
pygame.mixer.music.play(-1)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Input handling - left and right arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += player_speed

    # Jumping with Spacebar
    if keys[pygame.K_SPACE] and player_y == SCREEN_HEIGHT - player_height - 20:
        player_y -= 10
        jump_sound.play()

    # Apply gravity
    if player_y < SCREEN_HEIGHT - player_height - 20:
        player_y += 5

    # Add a new obstacle randomly
    if random.randint(0, 100) < 2:
        obstacle_type = random.choice(["rect", "tri", "circle"])
        obstacle_x = random.randint(0, SCREEN_WIDTH - obstacle_width)

        if obstacle_type == "circle":
            obstacle_x = random.randint(0, SCREEN_WIDTH - obstacle_width - 50)

        obstacles.append((obstacle_x, -obstacle_height, obstacle_type))

    # Update obstacle positions
    for i, (obstacle_x, obstacle_y, obstacle_type) in enumerate(obstacles):
        if obstacle_type == "rect":
            # Rectangular obstacle: move straight down
            obstacles[i] = (obstacle_x, obstacle_y + obstacle_speed)
        elif obstacle_type == "tri":
            # Triangular obstacle: move diagonally
            obstacles[i] = (obstacle_x + obstacle_speed,
                            obstacle_y + obstacle_speed)
        elif obstacle_type == "circle":
            # Rotating circular obstacle: update the angle
            angle = 0.1  # Adjust the rotation speed
            rotated_obstacle_x = obstacle_x + (obstacle_width // 2)
            rotated_obstacle_y = obstacle_y + (obstacle_height // 2)
            obstacles[i] = (rotated_obstacle_x - obstacle_width // 2 * math.cos(angle),
                            rotated_obstacle_y -
                            obstacle_height // 2 * math.sin(angle),
                            "circle")

        # Remove obstacles that are off the screen
        if obstacle_y > SCREEN_HEIGHT:
            del obstacles[i]

        # Check for collision with obstacles
        if obstacle_y + obstacle_height > player_y and obstacle_y < player_y + player_height:
            if obstacle_x + obstacle_width > player_x and obstacle_x < player_x + player_width:
                # Game over
                collision_sound.play()
                running = False

                # Save high score to a file (you can choose a different file path)
                with open("high_score.txt", "w") as file:
                    file.write(str(score))

    # Increase the score
    score += 1

    # Clear the screen
    screen.fill(WHITE)

    # Draw the player
    pygame.draw.rect(screen, (0, 0, 255), (player_x,
                     player_y, player_width, player_height))

    # Draw the obstacles
    for obstacle_x, obstacle_y, obstacle_type in obstacles:
        if obstacle_type == "rect":
            pygame.draw.rect(screen, (255, 0, 0), (obstacle_x,
                             obstacle_y, obstacle_width, obstacle_height))
        elif obstacle_type == "tri":
            pygame.draw.polygon(screen, (0, 255, 0), [(obstacle_x, obstacle_y), (obstacle_x + obstacle_width, obstacle_y),
                                                      (obstacle_x + obstacle_width // 2, obstacle_y + obstacle_height)])
        elif obstacle_type == "circle":
            pygame.draw.circle(screen, (0, 0, 255), (int(obstacle_x + obstacle_width // 2),
                                                     int(obstacle_y + obstacle_height // 2)), obstacle_width // 2)

    # Draw the score
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update the screen
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
