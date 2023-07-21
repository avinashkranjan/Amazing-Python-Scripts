import pygame
# Initialize pygame

pygame.init()  # Initialize pygame

# Set the window size
screen = pygame.display.set_mode((600, 400))  # Set the window size

# Set the title of the window
pygame.display.set_caption("Pong")  # Set the title of the window

# Set up the game clock
clock = pygame.time.Clock()  # Set up the game clock

# Load the images for the ball and paddles
ball_image = pygame.image.load("Assets/ball.png")
paddle_image = pygame.image.load("Assets/paddle.png")

# Create the ball sprite
ball = pygame.sprite.Sprite()  # Create the ball sprite
ball.image = ball_image  # Load the ball image
ball.rect = ball.image.get_rect()  # Get the ball's rects

# Create the paddles
left_paddle = pygame.sprite.Sprite()  # Create the left paddle
left_paddle.image = paddle_image  # Load the left paddle image
left_paddle.rect = left_paddle.image.get_rect()  # Get the left paddle's rect

right_paddle = pygame.sprite.Sprite()  # Create the right paddle
right_paddle.image = paddle_image  # Load the right paddle image
right_paddle.rect = right_paddle.image.get_rect()  # Get the right paddle's rect

# Set the initial positions of the ball and paddles
ball.rect.center = (300, 200)  # Set the ball's initial position
left_paddle.rect.left = 20  # Set the left paddle's initial position
left_paddle.rect.centery = 200  # Set the left paddle's initial position
right_paddle.rect.right = 580  # Set the right paddle's initial position
right_paddle.rect.centery = 200  # Set the right paddle's initial position

# Set the ball's initial velocity
ball_vx = 5
ball_vy = 5

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():  # Handle events
        if event.type == pygame.QUIT:  # Handle the QUIT event
            pygame.quit()  # Quit pygame
            exit()  # Exit the program

    # Update game state
    ball.rect.x += ball_vx  # Update the ball's x position
    ball.rect.y += ball_vy  # Update the ball's y position

    # Update game state
    keys = pygame.key.get_pressed()  # Get the keys that are pressed
    if keys[pygame.K_UP]:  # Check if the up key is pressed
        right_paddle.rect.y -= 5  # Update the right paddle's y position
    if keys[pygame.K_DOWN]:  # Check if the down key is pressed
        right_paddle.rect.y += 5  # Update the right paddle's y position
    if keys[pygame.K_w]:    # Check if the w key is pressed
        left_paddle.rect.y -= 5  # Update the left paddle's y position
    if keys[pygame.K_s]:    # Check if the s key is pressed
        left_paddle.rect.y += 5  # Update the left paddle's y position

    # Check for ball collision with paddles
    # Check for ball collision with paddles
    if ball.rect.colliderect(left_paddle.rect) or ball.rect.colliderect(right_paddle.rect):
        ball_vx = -ball_vx  # Reverse the ball's x velocity

    # Check for ball collision with walls
    if ball.rect.top < 0 or ball.rect.bottom > 400:  # Check for ball collision with walls
        ball_vy = -ball_vy  # Reverse the ball's y velocity

    # Draw the screen
    screen.fill((0, 0, 0))  # Fill the screen with black
    screen.blit(ball.image, ball.rect)  # Draw the ball
    screen.blit(left_paddle.image, left_paddle.rect)  # Draw the left paddle
    screen.blit(right_paddle.image, right_paddle.rect)  # Draw the right paddle
    pygame.display.flip()  # Update the display

    # Limit the frame rate
    clock.tick(60)
