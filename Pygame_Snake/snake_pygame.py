import pygame
import random

# Initialize pygame
pygame.init()

# Set the screen dimensions
screen_width = 640
screen_height = 480

# Set the colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Set the game clock
clock = pygame.time.Clock()

# Set the snake's initial position and speed
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_speed = 10

# Set the initial food position
food_position = [random.randrange(1, screen_width // 10) * 10,
                 random.randrange(1, screen_height // 10) * 10]
food_spawn = True

# Set the initial game score
score = 0

# Set the game over flag
game_over = False

# Game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Handle snake movement
    keys = pygame.key.get_pressed()
    for key in keys:
        if keys[pygame.K_LEFT]:
            snake_position[0] -= snake_speed
        if keys[pygame.K_RIGHT]:
            snake_position[0] += snake_speed
        if keys[pygame.K_UP]:
            snake_position[1] -= snake_speed
        if keys[pygame.K_DOWN]:
            snake_position[1] += snake_speed

    # Check for collision with the food
    if pygame.Rect(snake_position[0], snake_position[1], 10, 10).colliderect(
            pygame.Rect(food_position[0], food_position[1], 10, 10)):
        score += 1
        food_spawn = False

    # Spawn new food if the previous one was eaten
    if not food_spawn:
        food_position = [random.randrange(1, screen_width // 10) * 10,
                         random.randrange(1, screen_height // 10) * 10]
        food_spawn = True

    # Update the snake's body
    snake_body.insert(0, list(snake_position))
    if len(snake_body) > score + 1:
        snake_body.pop()

    # Check for collision with the snake's own body
    if snake_position in snake_body[1:]:
        game_over = True

    # Check for collision with the screen boundaries
    if snake_position[0] < 0 or snake_position[0] >= screen_width or \
            snake_position[1] < 0 or snake_position[1] >= screen_height:
        game_over = True

    # Set the screen background
    screen.fill(black)

    # Draw the snake
    for pos in snake_body:
        pygame.draw.rect(screen, white, pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw food
    pygame.draw.rect(screen, red, pygame.Rect(
        food_position[0], food_position[1], 10, 10))

    # Update the screen
    pygame.display.flip()

    # Set the game speed
    clock.tick(20)

# Quit the game
pygame.quit()
