"""
Author : Robin Singh
Flapy Bird Game Devlopment

"""
import random
import sys
import pygame
from pygame.locals import *

pygame.init()


# Game specific Variables for the game
FPS = 40
screen_width = 300
screen_height = 500
game_window = pygame.display.set_mode((screen_width,screen_height))
ground_y =screen_height * 0.8
images = {}
sounds= {}
bird = 'images/bird.png'
backGround = 'images/background.png'
pipee = 'images/pipe.png'

def welcomeScreen():


    player_x = int(screen_width/5)
    player_y = int((screen_height -images['bird'].get_height())/2)
    message_x = int((screen_width -images['message'].get_width())/2)
    message_y = int(screen_height*0.13)
    base = 0
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # If the user presses space or up key, start the game for them
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                return
            else:
                game_window.blit(images['background'], (0, 0))
                # game_window.blit(images['bird'], (player_x, player_y))
                game_window.blit(images['message'], (message_x,message_y ))
                game_window.blit(images['base'], (base,ground_y))
                pygame.display.update()
                clock.tick(FPS)

def mainGame():
    score = 0
    player_x = int(screen_width/5)
    player_y = int(screen_width/2)
    base_x = 0

    pipe_1 = getRandomPipe()
    pipe_2 = getRandomPipe()


    upperPipes = [
        {'x':screen_width+200, 'y':pipe_1[0]['y']},
        {'x':screen_width+200+(screen_width/2), 'y':pipe_2[0]['y']},
    ]

    lowerPipes = [
        {'x':screen_width+200, 'y':pipe_1[1]['y']},
        {'x':screen_width+200+(screen_width/2), 'y':pipe_2[1]['y']},
    ]

    pipe_Vel_X = -4

    playerVelY = -9
    playerMaxVelY = 10
    playerMinVelY = -8
    player_speed = 1

    Flap_speed = -8 #flapping speed
    playerFlapped = False #when bird is flapping then this value will be true


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    if player_y > 0:
                        playerVelY = Flap_speed
                        playerFlapped = True
                        sounds['wing'].play()
                if event.key == K_DOWN:
                    score+=1


        # if the bird is crashed then isCollide Function Will  return True
        crashTest = isCollide(player_x, player_y, upperPipes, lowerPipes) # This function will return true if the player gets crashed
        if crashTest:
            return     

        #checking score
        playerMidPos = player_x +images['bird'].get_width()/2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] +images['pipe'][0].get_width()/2
            if pipeMidPos<= playerMidPos < pipeMidPos +4:
                score +=1
                # print(f"Your score is {score}")
                sounds['point'].play()


        if playerVelY <playerMaxVelY and not playerFlapped:
            playerVelY += player_speed

        if playerFlapped:
            playerFlapped = False            
        playerHeight =images['bird'].get_height()
        player_y = player_y + min(playerVelY,ground_y - player_y - playerHeight) #When Bird touches the base then we will take  min() function to determine if bird touches the ground or not if yes then we will get (ground_y-play_y-player_Height = 0)

        # will moves lower and upper pipes to left
        for upperPipe , lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipe_Vel_X
            lowerPipe['x'] += pipe_Vel_X

        # before removig a pipe we will add a new pipe into the scrren
        if 0<upperPipes[0]['x']<5:
            newpipe = getRandomPipe()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])

        # when pipes are getting out of the scrren then remove it
        if upperPipes[0]['x'] < -images['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)
        
        #now we will blit all the images
        game_window.blit(images['background'], (0, 0))
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            game_window.blit(images['pipe'][0], (upperPipe['x'], upperPipe['y']))
            game_window.blit(images['pipe'][1], (lowerPipe['x'], lowerPipe['y']))

        game_window.blit(images['base'], (base_x,ground_y))
        game_window.blit(images['bird'], (player_x, player_y))
        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += images['numbers'][digit].get_width()
        Xoffset = (screen_width - width)/2

        for digit in myDigits:
            game_window.blit(images['numbers'][digit], (Xoffset,screen_height*0.12))
            Xoffset +=images['numbers'][digit].get_width()
        pygame.display.update()
        clock.tick(FPS)

def isCollide(player_x, player_y, upperPipes, lowerPipes):
    if player_y>ground_y- 25  or player_y<0:
        sounds['hit'].play()
        sounds['die'].play()
        return True
    
    for pipe in upperPipes:
        pipeHeight =images['pipe'][0].get_height()
        if(player_y < pipeHeight + pipe['y'] and abs(player_x - pipe['x']) <images['pipe'][0].get_width()):
            sounds['hit'].play()
            sounds['die'].play()
            return True

    for pipe in lowerPipes:
        if (player_y +images['bird'].get_height() > pipe['y']) and abs(player_x - pipe['x']) <images['pipe'][0].get_width():
            sounds['hit'].play()
            sounds['die'].play()
            return True
    return False

#function for generating random postions of pipes on the screen
#Very Important Function
def getRandomPipe():
    pipe_height =images['pipe'][0].get_height()
    offset =screen_height/3
    y2 = offset + random.randrange(0, int(screen_height -images['base'].get_height()  - 1.2 *offset))
    pipeX = screen_width + 10
    y1 = pipe_height - y2 + offset
    pipe = [
        {'x': pipeX, 'y': -y1}, #upper Pipe
        {'x': pipeX, 'y': y2} #lower Pipe
    ]
    return pipe


if __name__ == "__main__":

    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('FLAPPY BIRD')
    images['numbers'] = (
        pygame.image.load('images/0.png'),
        pygame.image.load('images/1.png'),
        pygame.image.load('images/2.png'),
        pygame.image.load('images/3.png'),
        pygame.image.load('images/4.png'),
        pygame.image.load('images/5.png'),
        pygame.image.load('images/6.png'),
        pygame.image.load('images/7.png'),
        pygame.image.load('images/8.png'),
        pygame.image.load('images/9.png'),
    )

    images['message'] =pygame.image.load('images/message.png')
    images['base'] =pygame.image.load('images/base.png')
    images['pipe'] =(pygame.transform.rotate(pygame.image.load(pipee).convert_alpha(),180),
    pygame.image.load(pipee)
    )


    sounds['die'] = pygame.mixer.Sound('sounds/die.wav')
    sounds['hit'] = pygame.mixer.Sound('sounds/hit.wav')
    sounds['point'] = pygame.mixer.Sound('sounds/point.wav')
    sounds['swoosh'] = pygame.mixer.Sound('sounds/swoosh.wav')
    sounds['wing'] = pygame.mixer.Sound('sounds/wing.wav')

    images['background'] = pygame.image.load(backGround)
    images['bird'] = pygame.image.load(bird)

    while True:
        welcomeScreen()

        mainGame()