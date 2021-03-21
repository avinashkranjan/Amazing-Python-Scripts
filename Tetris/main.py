
import pygame, random, sys


class Color:
    colors = [
        (0, 0, 0),
        (120, 37, 179),
        (100, 179, 179),
        (80, 34, 22),
        (80, 134, 22),
        (180, 34, 22),
        (180, 34, 122),
    ]
    word_color = [
        (0, 0, 0),
        (255, 255, 255),
        (128, 128, 128),
    ]


class Shapes:
    x = 0
    y = 0

    shapes = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.shapes) - 1)
        self.color = random.randint(1, len(Color.colors) - 1)
        self.rotation = 0

    def image(self):
        return self.shapes[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.shapes[self.type])


class Tetris:     
    Stage = 2
    score = 0
    state = "start"
    field = []
    height = 0
    width = 0
    x = 100
    y = 60
    zoom = 20
    Shapes = None

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.field = []
        self.score = 0
        self.state = "start"
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

    def new_Shapes(self):
        self.Shapes = Shapes(3, 0)

    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.Shapes.image():
                    if i + self.Shapes.y > self.height - 1 or \
                            j + self.Shapes.x > self.width - 1 or \
                            j + self.Shapes.x < 0 or \
                            self.field[i + self.Shapes.y][j + self.Shapes.x] > 0:
                        intersection = True
        return intersection

    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i1][j] = self.field[i1 - 1][j]
        self.score += lines ** 2

    def go_space(self):
        while not self.intersects():
            self.Shapes.y += 1
        self.Shapes.y -= 1
        self.freeze()

    def go_down(self):
        self.Shapes.y += 1
        if self.intersects():
            self.Shapes.y -= 1
            self.freeze()

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.Shapes.image():
                    self.field[i + self.Shapes.y][j + self.Shapes.x] = self.Shapes.color
        self.break_lines()
        self.new_Shapes()
        if self.intersects():
            self.state = "gameover"

    def go_side(self, dx):
        old_x = self.Shapes.x
        self.Shapes.x += dx
        if self.intersects():
            self.Shapes.x = old_x

    def rotate(self):
        old_rotation = self.Shapes.rotation
        self.Shapes.rotate()
        if self.intersects():
            self.Shapes.rotation = old_rotation

class Main:

    pygame.init()

    size = (400, 500)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Tetris")

    game_over = False
    clock = pygame.time.Clock()
    fps = 25
    game = Tetris(20, 10)
    counter = 0

    pressing_down = False

    while not game_over:
        if game.Shapes is None:
            game.new_Shapes()
        counter += 1
        if counter > 100000:
            counter = 0

        if counter % (fps // game.Stage // 2) == 0 or pressing_down:
            if game.state == "start":
                game.go_down()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.rotate()
                if event.key == pygame.K_DOWN:
                    pressing_down = True
                if event.key == pygame.K_LEFT:
                    game.go_side(-1)
                if event.key == pygame.K_RIGHT:
                    game.go_side(1)
                if event.key == pygame.K_SPACE:
                    game.go_space()
                if event.key == pygame.K_r:
                    game.__init__(20, 10)
                if event.key == pygame.K_q:
                    game_over = True

        if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    pressing_down = False

        screen.fill(Color.word_color[1])

        for i in range(game.height):
            for j in range(game.width):
                pygame.draw.rect(screen, Color.word_color[2], [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
                if game.field[i][j] > 0:
                    pygame.draw.rect(screen, Color.colors[game.field[i][j]],
                                    [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

        if game.Shapes is not None:
            for i in range(4):
                for j in range(4):
                    p = i * 4 + j
                    if p in game.Shapes.image():
                        pygame.draw.rect(screen, Color.colors[game.Shapes.color],
                                        [game.x + game.zoom * (j + game.Shapes.x) + 1,
                                        game.y + game.zoom * (i + game.Shapes.y) + 1,
                                        game.zoom - 2, game.zoom - 2])

        font = pygame.font.SysFont('Calibri', 25, True, False)
        font1 = pygame.font.SysFont('Calibri', 40, True, False)
        text = font.render("Score: " + str(game.score), True, Color.word_color[0])
        text_game_over = font1.render("Game Over! q to quit.", True, (255, 125, 0))
        text_game_over1 = font1.render("Press r to restart", True, (255, 215, 0))

        screen.blit(text, [0, 0])
        if game.state == "gameover":
            screen.blit(text_game_over, [20, 200])
            screen.blit(text_game_over1, [25, 265])

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
    sys.exit() 

if __name__ == "__main__":
    run_game = Main()