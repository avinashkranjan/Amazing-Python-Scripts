import pygame
from pygame.locals import *

pygame.init()

'''
Defining gaming window size 
'''
Window_height = 500
Window_width = 500

window = pygame.display.set_mode((Window_height,Window_width))
pygame.display.set_caption('Brickstroy')        #game title

'''
Defining Bricks colour
'''
O_brick = (255,100,10)
w_brick = (255,255,255)
g_brick = (0,255,0)
black = (0,0,0)

game_rows = 6
game_coloumns = 6
clock =pygame.time.Clock()        #clock speed
frame_rate = 60

class bricks():
    
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
                Reactangle = pygame.Rect(x_brick, y_brick, self.width, self.height)
                if row < 2:
                    power = 3
                elif row < 4:
                    power = 2
                elif row < 6:
                    power= 1
                
                single_brick = [Reactangle, power]
                brick_row.append(single_brick)
            self.brick.append(brick_row)

    def draw_brick(self):
        for row in self.brick:
            for brick in row:
                if brick[1] == 3:
                    brick_colour =   O_brick
                elif brick[1] == 2:
                    brick_colour = w_brick
                elif brick[1] == 1:
                    brick_colour = g_brick
                pygame.draw.rect(window, brick_colour, brick[0])    
                pygame.draw.rect(window, (0,0,0), (brick[0]),1)

class base():
    def __init__(self,x,y,size_x,size_y,color):
        self.image = pygame.Surface((size_x,size_y),SRCALPHA,32)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y  # X,Y coordinates for our base
        
        self.image.fill(w_brick)
        
        self.movement = [0,0] #pixelsto be moved in (x,y) format
        self.speed= 8

    def draw_base(self):
        pygame.draw.rect(window, (0,0,255), self.rect)
        pygame.draw.rect(window, (255,255,255), self.rect,1)

    def update(self):
        self.rect = self.rect.move(self.movement)
        self.checkbounds()

    def checkbounds(self):
        if self.rect.left < 0:
            self.rect.left = 0
        
        if self.rect.right > Window_width:
            self.rect.right = Window_width

brick = bricks()
brick.make_brick()

user_basepad = base(Window_width/2,Window_height - Window_height/10,80,10,w_brick)

#ball = ball(user_basepad.x + (user_basepad.width//2), user_basepad.y + user_basepad.height)

game= True
while game:

    clock.tick(frame_rate)
    window.fill(black)
    user_basepad.update()
    user_basepad.draw_base()
    brick.draw_brick()
 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game=False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                user_basepad.movement[0] = -1*user_basepad.speed
            if event.key == pygame.K_RIGHT:
                user_basepad.movement[0]= user_basepad.speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                user_basepad.movement[0] = 0

    
    pygame.display.update()   # added for any updates that we make to the gaming window to become visible.
    
pygame.quit()