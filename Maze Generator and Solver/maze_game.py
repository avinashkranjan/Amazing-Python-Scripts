import pygame
import random
import time

MAZE_WIDTH, MAZE_HEIGHT = 20, 20
CELL_SIZE = 30
WINDOW_WIDTH, WINDOW_HEIGHT = MAZE_WIDTH * CELL_SIZE, MAZE_HEIGHT * CELL_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


class Cell:
    WALL = 0
    PATH = 1
    VISITED = 2


maze = [[Cell.WALL for _ in range(MAZE_WIDTH)] for _ in range(MAZE_HEIGHT)]


def generate_maze(x, y):
    maze[y][x] = Cell.VISITED
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    random.shuffle(directions)

    for dx, dy in directions:
        nx, ny = x + 2 * dx, y + 2 * dy
        if 0 <= nx < MAZE_WIDTH and 0 <= ny < MAZE_HEIGHT and maze[ny][nx] == Cell.WALL:
            maze[y + dy][x + dx] = Cell.PATH
            generate_maze(nx, ny)


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        new_x, new_y = self.x + dx, self.y + dy
        if 0 <= new_x < MAZE_WIDTH and 0 <= new_y < MAZE_HEIGHT and maze[new_y][new_x] != Cell.WALL:
            self.x = new_x
            self.y = new_y


player = Player(1, 1)

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Maze Generator and Solver")

generate_maze(0, 0)
start_point = (1, 1)
end_point = (MAZE_WIDTH - 2, MAZE_HEIGHT - 2)
path = []

running = True
start_time = time.time()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                maze = [[Cell.WALL for _ in range(
                    MAZE_WIDTH)] for _ in range(MAZE_HEIGHT)]
                generate_maze(0, 0)
                start_point = (1, 1)
                end_point = (MAZE_WIDTH - 2, MAZE_HEIGHT - 2)
                path = []
                player.x, player.y = start_point[0], start_point[1]
            elif event.key in (pygame.K_UP, pygame.K_w):
                player.move(0, -1)
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                player.move(0, 1)
            elif event.key in (pygame.K_LEFT, pygame.K_a):
                player.move(-1, 0)
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                player.move(1, 0)

    window.fill(WHITE)

    for y in range(MAZE_HEIGHT):
        for x in range(MAZE_WIDTH):
            if maze[y][x] == Cell.WALL:
                pygame.draw.rect(window, BLACK, (x * CELL_SIZE,
                                 y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif maze[y][x] == Cell.PATH:
                pygame.draw.rect(window, WHITE, (x * CELL_SIZE,
                                 y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif maze[y][x] == Cell.VISITED:
                pygame.draw.rect(window, GREEN, (x * CELL_SIZE,
                                 y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    for x, y in path:
        pygame.draw.rect(window, RED, (x * CELL_SIZE, y *
                         CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.draw.rect(
        window, GREEN, (end_point[0] * CELL_SIZE, end_point[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    if (player.x, player.y) == end_point:
        elapsed_time = time.time() - start_time
        pygame.draw.rect(
            window, GREEN, (end_point[0] * CELL_SIZE, end_point[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        font = pygame.font.SysFont(None, 40)
        text = font.render(
            f"Congratulations! Time: {elapsed_time:.2f} seconds", True, BLACK)
        window.blit(text, (10, WINDOW_HEIGHT - 40))
    else:
        path = []
        visited = set()
        queue = [(start_point, [])]

        while queue:
            (x, y), current_path = queue.pop(0)

            if (x, y) == end_point:
                path = current_path
                break

            visited.add((x, y))

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < MAZE_WIDTH and 0 <= ny < MAZE_HEIGHT and maze[ny][nx] in (Cell.PATH, Cell.VISITED) and (nx, ny) not in visited:
                    queue.append(((nx, ny), current_path + [(x, y)]))
                    visited.add((nx, ny))

    pygame.display.update()

pygame.quit()
