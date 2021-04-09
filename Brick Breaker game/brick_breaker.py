import pygame
from pygame.locals import *

pygame.init()

'''
Defining gaming window size
'''
Window_height = 500
Window_width = 500

window = pygame.display.set_mode((Window_height, Window_width))
pygame.display.set_caption('Brickstroy')  # game title

'''
Defining Bricks colour
'''
O_brick = (255, 100, 10)
w_brick = (255, 255, 255)
g_brick = (0, 255, 0)
black = (0, 0, 0)

game_rows = 6
game_coloumns = 6
clock = pygame.time.Clock()  # clock speed
frame_rate = 60


class Ball():
    '''
    Creating ball for the game
    '''

    def __init__(self, x, y):
        self.radius = 10
        self.x = x - self.radius
        self.y = y - 50
        self.rect = Rect(self.x, self.y, self.radius * 2, self.radius * 2)
        self.x_speed = 4
        self.y_speed = -4
        self.max_speed = 5
        self.game_over = 0

    def motion(self):

        collision_threshold = 5
        block_object = Blocks.brick
        brick_destroyed = 1  # flag set to 1
        count_row = 0
        for row in block_object:
            count_item = 0
            for item in row:
                if self.rect.colliderect(
                        item[0]):  # checks for each collission
                    if abs(
                            self.rect.bottom -
                            item[0].top) < collision_threshold and self.y_speed > 0:
                        self.y_speed *= -1
                    if abs(
                            self.rect.top -
                            item[0].bottom) < collision_threshold and self.y_speed < 0:
                        self.y_speed *= -1
                    if abs(
                            self.rect.right -
                            item[0].left) < collision_threshold and self.x_speed > 0:
                        self.x_speed *= -1
                    if abs(
                            self.rect.left -
                            item[0].right) < collision_threshold and self.x_speed < 0:
                        self.x_speed *= -1

                    if block_object[count_row][count_item][1] > 1:
                        block_object[count_row][count_item][1] -= 1
                    else:
                        block_object[count_row][count_item][0] = (0, 0, 0, 0)

                if block_object[count_row][count_item][0] != (0, 0, 0, 0):
                    brick_destroyed = 0
                count_item += 1
            count_row += 1
        if brick_destroyed == 1:
            self.game_over = 1

        # collision check for game window
        if self.rect.left < 0 or self.rect.right > Window_width:
            self.x_speed *= -1

        if self.rect.top < 0:
            self.y_speed *= -1

        if self.rect.bottom > Window_height:
            self.game_over = -1

        # collision check for base
        if self.rect.colliderect(user_basepad):
            if abs(
                    self.rect.bottom -
                    user_basepad.rect.top) < collision_threshold and self.y_speed > 0:
                self.y_speed *= -1
                self.x_speed += user_basepad.direction
                if self.x_speed > self.max_speed:
                    self.x_speed = self.max_speed
                elif self.x_speed < 0 and self.x_speed < -self.max_speed:
                    self.x_speed = -self.max_speed
                else:
                    self.x_speed *= -1

        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        return self.game_over

    def draw(self):
        pygame.draw.circle(
            window,
            (0,
             0,
             255),
            (self.rect.x +
             self.radius,
             self.rect.y +
             self.radius),
            self.radius)
        pygame.draw.circle(
            window,
            (255,
             255,
             255),
            (self.rect.x +
             self.radius,
             self.rect.y +
             self.radius),
            self.radius,
            1)


class Blocks():
    '''
    This class will help me create blocks/bricks of the game
    '''

    def __init__(self):
        self.width = Window_width // game_coloumns
        self.height = 40

    def make_brick(self):
        self.brick = []
        single_brick = []
        for row in range(game_rows):
            brick_row = []
            for coloumn in range(game_coloumns):
                x_brick = coloumn * self.width
                y_brick = row * self.height
                Reactangle = pygame.Rect(
                    x_brick, y_brick, self.width, self.height)
                if row < 2:
                    power = 3
                elif row < 4:
                    power = 2
                elif row < 6:
                    power = 1

                single_brick = [Reactangle, power]
                brick_row.append(single_brick)
            self.brick.append(brick_row)

    def draw_brick(self):
        for row in self.brick:
            for brick in row:
                if brick[1] == 3:
                    brick_colour = O_brick
                elif brick[1] == 2:
                    brick_colour = w_brick
                elif brick[1] == 1:
                    brick_colour = g_brick
                pygame.draw.rect(window, brick_colour, brick[0])
                pygame.draw.rect(window, (0, 0, 0), (brick[0]), 1)


class base():
    '''
    This class is to create the base pad of the game
    '''

    def __init__(self, x, y, size_x, size_y, color):
        self.image = pygame.Surface((size_x, size_y), 32)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y  # X,Y coordinates for our base

        self.image.fill(w_brick)

        self.movement = [0, 0]  # pixelsto be moved in (x,y) format
        self.speed = 8

        self.height = 20
        self.width = int(Window_width / game_coloumns)
        self.x = int((Window_width / 2) - (self.width / 2))
        self.y = Window_height - (self.height * 2)

        self.direction = 0

    def draw_base(self):
        pygame.draw.rect(window, (0, 0, 255), self.rect)
        pygame.draw.rect(window, (255, 255, 255), self.rect, 1)

    def update(self):
        self.rect = self.rect.move(self.movement)
        self.checkbounds()

    def checkbounds(self):
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > Window_width:
            self.rect.right = Window_width


# calling all classes an functions here

Blocks = Blocks()
Blocks.make_brick()

user_basepad = base(
    Window_width /
    2,
    Window_height -
    Window_height /
    10,
    80,
    10,
    w_brick)

ball = Ball(user_basepad.x + (user_basepad.width // 2),
            user_basepad.y + user_basepad.height)


game = True
while game:

    clock.tick(frame_rate)
    window.fill(black)
    user_basepad.update()
    user_basepad.draw_base()
    Blocks.draw_brick()
    ball.draw()
    ball.motion()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                user_basepad.movement[0] = -1 * user_basepad.speed
            if event.key == pygame.K_RIGHT:
                user_basepad.movement[0] = user_basepad.speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                user_basepad.movement[0] = 0

    # added for any updates that we make to the gaming window to become
    # visible.
    pygame.display.update()

pygame.quit()
