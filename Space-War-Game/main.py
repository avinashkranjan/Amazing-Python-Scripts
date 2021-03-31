# Importing the Modules

import pygame
import random
import math
from pygame import mixer

#initialise the pygame

pygame.init()

#creating the screen for our game

screen = pygame.display.set_mode((800,600))

# Embedding The backgroung Image

background = pygame.image.load('Images/background.png')

# Our Title of the game

pygame.display.set_caption("My Game")

# Our Logo Of the game

icon = pygame.image.load('Images/Image.png')
pygame.display.set_icon(icon)

# Main Player Image

PlayerImg = pygame.image.load('Images/SpaceShip.png')

# Main Player Position

playerX = 370
playerY = 480
playerX_change = 0

# Enemy Image

enemyImg = pygame.image.load('Images/enemy.png')

# Creating Variables for Multiple Enemies

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

number_of_enemies = 6

for i in range(number_of_enemies):

    # Enemy position
    enemyImg.append(pygame.image.load('Images/enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(0, 50))
    enemyX_change.append(0.3)
    enemyY_change.append(40)

# Loading The Image of the Bullet
 
bulletImg = pygame.image.load('Images/bullet.png')

# Bullet position

bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 3
bulelt_state = "ready"

# Score Logic

score_value = 0

font = pygame.font.Font('Fonts/Cartoon_cookies_Tilted.ttf',32)

textX = 10
textY = 10

# Game Over Text

game_over_font = pygame.font.Font('Fonts/CHICKEN_Pie.ttf',60)

# Your Score Text

Your_score_Font = pygame.font.Font('Fonts/CHICKEN_Pie.ttf',30)

# Game Over Function

def game_over():
    game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over_text, (200 , 250))

def your_score():
    your_score_text = Your_score_Font.render("Your Score: "+ str(score_value), True, (255, 255, 255))
    screen.blit(your_score_text, (220 , 350))


def ShowScore(x, y):
    score = font.render("Score:" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x , y))

# Main Player Function

def player(x, y):
    screen.blit(PlayerImg, (x, y))

# Enemy Function

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))    

def fire_bullet(x,y):   
    global bulelt_state
    bulelt_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))   

# Logic of collision

def iscollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    
    if distance < 27:
        return True
    
    else:
        return False

# The main Game loop

running = True

while running:
    
    # Changing The background color of the window

    screen.fill((0,0,0))    #  RGB wise parameters

    # Including our Background Image

    screen.blit(background, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Getting Our Animations Done when a keystroke is pressed

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                playerX_change = -5
                
            if event.key == pygame.K_RIGHT:
                playerX_change = 5

            # Shooting Our Bullet
             
            if event.key == pygame.K_SPACE:
                if bulelt_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)        

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                playerX_change = 0               

            if event.key == pygame.K_RIGHT:
                playerX_change = 0   

    # Player Motion

    playerX = playerX + playerX_change

    # Making the Boundaries for the main player

    if playerX <= 0:
        playerX = 0

    elif playerX >= 736:
        playerX = 736

    # Enemy Motion

    for i in range(number_of_enemies):

        # Game Over Logic

        if enemyY[i] > 440:
            for j in range(number_of_enemies):
                enemyY[j] = 2500

            game_over()
            your_score()
            break

        enemyX[i] = enemyX[i] + enemyX_change[i]

        # Making The boundaries for the enemy

        if enemyX[i] <= 0:
            enemyX_change[i] = 0.7
            enemyY[i] = enemyY[i] + enemyY_change[i]

        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.7    
            enemyY[i] = enemyY[i] + enemyY_change[i]

        # Collision Function Call

        collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY) 

        if collision:
            bulletY = 480
            bulelt_state = "ready"
            score_value = score_value + 1
            # print(score) 
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)    

        # Calling The Enemy Player Function

        enemy(enemyX[i], enemyY[i], i)    

    # Movement of the bullet

    if bulletY < 0:
        bulletY = 480
        bulelt_state = "ready"     
     
    if bulelt_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY = bulletY - bulletY_change        

    # Calling The main Player Function

    player(playerX, playerY)

    # Calling The Text Function

    ShowScore(textX, textY)

    # Updating Our Game

    pygame.display.update()    