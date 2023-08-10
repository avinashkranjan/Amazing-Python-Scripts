import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity Simulation Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Spaceship properties
spaceship_radius = 15
spaceship_pos = [WIDTH // 2, HEIGHT // 2]
spaceship_vel = [0, 0]

# Celestial bodies properties (position, mass)
celestial_bodies = [
    {"pos": [WIDTH // 4, HEIGHT // 4], "mass": 2000},
    {"pos": [WIDTH * 3 // 4, HEIGHT * 3 // 4], "mass": 3000},
]

# Gravity constant
G = 0.1

# Load sound effects
thrust_sound = pygame.mixer.Sound("thrust.wav")
collision_sound = pygame.mixer.Sound("collision.wav")

# Fuel properties
fuel = 100
fuel_consumption_rate = 0.5
fuel_powerup_amount = 50

# Scoring properties
score = 0
level = 1

# Font
font = pygame.font.Font(None, 30)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle spaceship movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        spaceship_vel[0] -= 0.1
        thrust_sound.play()
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        spaceship_vel[0] += 0.1
        thrust_sound.play()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        spaceship_vel[1] -= 0.1
        thrust_sound.play()
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        spaceship_vel[1] += 0.1
        thrust_sound.play()

    # Update spaceship position
    spaceship_pos[0] += spaceship_vel[0]
    spaceship_pos[1] += spaceship_vel[1]

    # Calculate gravity forces on the spaceship
    for body in celestial_bodies:
        dist_x = body["pos"][0] - spaceship_pos[0]
        dist_y = body["pos"][1] - spaceship_pos[1]
        distance = math.sqrt(dist_x**2 + dist_y**2)

        # Apply gravity force to the spaceship's velocity
        spaceship_vel[0] += G * body["mass"] * dist_x / distance**3
        spaceship_vel[1] += G * body["mass"] * dist_y / distance**3

        # Check for collisions with celestial bodies
        if distance < body["mass"] + spaceship_radius:
            collision_sound.play()
            pygame.draw.circle(
                screen, RED, body["pos"], int(body["mass"] / 10))
            pygame.draw.circle(screen, YELLOW, spaceship_pos, spaceship_radius)
            pygame.display.flip()
            pygame.time.delay(2000)
            spaceship_pos = [WIDTH // 2, HEIGHT // 2]
            spaceship_vel = [0, 0]
            fuel = 100

    # Consume fuel while moving
    if keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_RIGHT] or keys[pygame.K_d] or \
            keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_DOWN] or keys[pygame.K_s]:
        fuel -= fuel_consumption_rate

    # Draw celestial bodies
    for body in celestial_bodies:
        pygame.draw.circle(screen, WHITE, body["pos"], int(body["mass"] / 10))

    # Draw the spaceship
    pygame.draw.circle(screen, YELLOW, spaceship_pos, spaceship_radius)

    # Draw fuel indicator and score
    fuel_indicator = pygame.Rect(50, 50, fuel, 10)
    pygame.draw.rect(screen, YELLOW, fuel_indicator)
    score_text = f"Score: {score} - Level: {level}"
    score_surface = font.render(score_text, True, YELLOW)
    screen.blit(score_surface, (50, 80))

    # Check for level completion
    if spaceship_pos[0] > WIDTH or spaceship_pos[0] < 0 or \
            spaceship_pos[1] > HEIGHT or spaceship_pos[1] < 0:
        # Increase score based on remaining fuel and level
        score += fuel + (level * 100)
        level += 1
        fuel = 100
        spaceship_pos = [WIDTH // 2, HEIGHT // 2]
        spaceship_vel = [0, 0]
        celestial_bodies = [{"pos": [random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)],
                             "mass": random.randint(1000, 5000)} for _ in range(level + 1)]

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
