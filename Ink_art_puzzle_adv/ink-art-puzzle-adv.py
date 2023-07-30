import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ink Art Puzzle Adventure")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player properties
player_x, player_y = WIDTH // 2, HEIGHT // 2
player_speed = 5

# Main game loop


def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_UP]:
            player_y -= player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed

        # Draw the player and background
        screen.fill(WHITE)
        # Player rectangle
        pygame.draw.rect(screen, BLACK, (player_x, player_y, 50, 50))

        # Draw ink art illustrations (replace this with your own images)
        # Example: ink_art_image = pygame.image.load("ink_art_image.png")
        # screen.blit(ink_art_image, (x, y))

        pygame.display.update()


# Start the game loop
game_loop()

# Quit Pygame
pygame.quit()
sys.exit()
