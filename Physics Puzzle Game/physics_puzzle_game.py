import pygame
import pymunk
import sys

# Define screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Physics Puzzle Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Physics space setup
space = pymunk.Space()
space.gravity = 0, 1000  # Set the gravity

# Main game loop
clock = pygame.time.Clock()


def create_physics_object(x, y, vertices):
    body = pymunk.Body(1, 100)
    body.position = x, y
    shape = pymunk.Poly(body, vertices)
    shape.elasticity = 0.5
    space.add(body, shape)
    return body


# Create interactive objects
object_vertices = [(-30, -30), (30, -30), (30, 30), (-30, 30)]
interactive_object = create_physics_object(200, 500, object_vertices)

# Create goal object
goal_vertices = [(-20, -20), (20, -20), (20, 20), (-20, 20)]
goal_object = create_physics_object(600, 100, goal_vertices)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Check if the mouse button is pressed
    if pygame.mouse.get_pressed()[0]:  # Left mouse button pressed
        # Check if the mouse is over the interactive object
        if interactive_object.shapes[0].point_query(interactive_object.position).distance < 30:
            interactive_object.position = mouse_x, SCREEN_HEIGHT - mouse_y

    # Clear the screen
    screen.fill(WHITE)

    # Update physics simulation
    dt = 1.0 / 60.0
    space.step(dt)

    # Draw physics objects on the screen
    for body in space.bodies:
        for shape in body.shapes:
            # Convert physics coordinates to screen coordinates
            vertices = [(body.position + v.rotated(body.angle))
                        for v in shape.get_vertices()]
            vertices = [(v.x, SCREEN_HEIGHT - v.y) for v in vertices]
            pygame.draw.polygon(screen, BLACK, vertices)

    # Check if the goal object is reached
    if goal_object.shapes[0].point_query(goal_object.position).distance < 20:
        print("Level Completed!")

    # Update the display
    pygame.display.flip()
    clock.tick(60)
