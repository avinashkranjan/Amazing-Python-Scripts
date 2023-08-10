import pygame
import sys

# Define the game window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define tile size and number of tiles
TILE_SIZE = 20
NUM_TILES_X = WINDOW_WIDTH // TILE_SIZE
NUM_TILES_Y = WINDOW_HEIGHT // TILE_SIZE

# Define directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class TronGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("AI-driven AI Tron")
        self.clock = pygame.time.Clock()
        self.running = True
        self.board = [[BLACK for _ in range(NUM_TILES_X)]
                      for _ in range(NUM_TILES_Y)]
        self.player1_pos = (NUM_TILES_X // 4, NUM_TILES_Y // 2)
        self.player2_pos = (NUM_TILES_X * 3 // 4, NUM_TILES_Y // 2)
        self.player1_direction = RIGHT
        self.player2_direction = LEFT

    def draw_board(self):
        for y in range(NUM_TILES_Y):
            for x in range(NUM_TILES_X):
                pygame.draw.rect(
                    self.screen, self.board[y][x], (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    def move_player(self, player_pos, player_direction, player_color):
        x, y = player_pos
        dx, dy = player_direction
        new_x, new_y = x + dx, y + dy

        if not (0 <= new_x < NUM_TILES_X) or not (0 <= new_y < NUM_TILES_Y):
            return False

        if self.board[new_y][new_x] == BLACK:
            self.board[new_y][new_x] = player_color
            return (new_x, new_y)
        return False

    def update(self):
        new_player1_pos = self.move_player(
            self.player1_pos, self.player1_direction, BLUE)
        new_player2_pos = self.move_player(
            self.player2_pos, self.player2_direction, RED)

        if not new_player1_pos or not new_player2_pos:
            self.running = False
            return

        self.player1_pos = new_player1_pos
        self.player2_pos = new_player2_pos

    def ai_move(self, player_pos, player_direction, opponent_pos):
        def is_valid_move(new_pos):
            x, y = new_pos
            return (0 <= x < NUM_TILES_X) and (0 <= y < NUM_TILES_Y) and self.board[y][x] == BLACK

        def simulate_move(pos, direction):
            x, y = pos
            dx, dy = direction
            return (x + dx, y + dy)

        def alpha_beta_search(pos, direction, opponent_pos, depth, alpha, beta, max_player):
            if depth == 0:
                return self.heuristic_evaluation(pos, opponent_pos)

            if max_player:
                value = -float('inf')
                for d in [UP, DOWN, LEFT, RIGHT]:
                    new_pos = simulate_move(pos, d)
                    if is_valid_move(new_pos):
                        value = max(value, alpha_beta_search(
                            new_pos, d, opponent_pos, depth - 1, alpha, beta, False))
                        alpha = max(alpha, value)
                        if beta <= alpha:
                            break
                return value
            else:
                value = float('inf')
                for d in [UP, DOWN, LEFT, RIGHT]:
                    new_pos = simulate_move(opponent_pos, d)
                    if is_valid_move(new_pos):
                        value = min(value, alpha_beta_search(
                            pos, direction, new_pos, depth - 1, alpha, beta, True))
                        beta = min(beta, value)
                        if beta <= alpha:
                            break
                return value

        best_score = -float('inf')
        best_move = None
        for d in [UP, DOWN, LEFT, RIGHT]:
            new_pos = simulate_move(player_pos, d)
            if is_valid_move(new_pos):
                score = alpha_beta_search(
                    new_pos, d, opponent_pos, depth=3, alpha=-float('inf'), beta=float('inf'), max_player=False)
                if score > best_score:
                    best_score = score
                    best_move = d
        return best_move

    def heuristic_evaluation(self, player_pos, opponent_pos):
        # The heuristic evaluation function calculates the manhattan distance between the player's position and the opponent's position
        return -(abs(player_pos[0] - opponent_pos[0]) + abs(player_pos[1] - opponent_pos[1]))

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w and self.player1_direction != DOWN:
                        self.player1_direction = UP
                    elif event.key == pygame.K_s and self.player1_direction != UP:
                        self.player1_direction = DOWN
                    elif event.key == pygame.K_a and self.player1_direction != RIGHT:
                        self.player1_direction = LEFT
                    elif event.key == pygame.K_d and self.player1_direction != LEFT:
                        self.player1_direction = RIGHT

            self.screen.fill(WHITE)
            self.update()
            self.draw_board()
            pygame.display.flip()
            self.clock.tick(10)

        pygame.quit()


if __name__ == "__main__":
    game = TronGame()
    game.run()
