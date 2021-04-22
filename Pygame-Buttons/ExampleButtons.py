# -*- coding: utf-8 -*-

import pygame
import os,sys


class Button(object):

    def __init__(self, position, size):

        # create 3 images
        self._images = [
            pygame.Surface(size),    
            pygame.Surface(size),    
            pygame.Surface(size),    
        ]

        # fill images with color - red, gree, blue
        self._images[0].fill((255, 226, 39))
        self._images[1].fill((235, 89, 110))
        self._images[2].fill((77, 55, 93))

        # get image size and position
        self._rect = pygame.Rect(position, size)

        # select first image
        self._index = 0

    def draw(self, screen):

        # draw selected image
        screen.blit(self._images[self._index], self._rect)

    def event_handler(self, event):

        # change selected color if rectange clicked
        if event.type == pygame.MOUSEBUTTONDOWN: # is some button clicked
            if event.button == 1: # is left button clicked
                if self._rect.collidepoint(event.pos): # is mouse over button
                    self._index = (self._index+1) % 3 # change image

# --- main ---

pygame.init()
w, h = 800, 800
screen = pygame.display.set_mode((w, h))
GREEN = (0, 255, 0)
GRAY= (174, 150, 255)
font = pygame.font.Font('freesansbold.ttf', 22)

# =============================================================================
# Rendring texts23564
# =============================================================================

p1 = font.render("A PNG button , Click it ", True,(233, 248, 103))
p2= font.render("A color img buttons", True,(254, 32, 107))
p0 = font.render('Go Back', True,(15, 28, 2))
textRectp0 = p0.get_rect()
textRectp1 = p1.get_rect()
textRectp2 = p2.get_rect()
textRectp0.center = (405, 225)
textRectp1.center = (200, 225)
textRectp2.center=(350,420)

#backButton=main.backButton

module = sys.modules['__main__']
path, name = os.path.split(module.__file__)
path = os.path.join(path, 'retry_button.png')

img0 = pygame.image.load(path)
img0.convert()
rect0 = img0.get_rect()
rect0.x=350
rect0.y=200
pygame.draw.rect(img0, GREEN, rect0, 1)
act=False


# create buttons

button1 = Button((205, 435), (100, 100))
button2 = Button((310, 435), (100, 100))
button3 = Button((420, 435), (100, 100))

# mainloop


running=True
while running:
    for event in pygame.event.get():
        pos=pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
            print("Job Done!!")
            #pygame.quit()
            pygame.quit()
            sys.exit()
        
        # --- buttons events ---

        button1.event_handler(event)
        button2.event_handler(event)
        button3.event_handler(event)
        
        
        if event.type==pygame.MOUSEBUTTONDOWN:
            if rect0.collidepoint(event.pos):
                    # Toggle the active variable.
                    act = not act
            else:
                    act = False
            if act:
                print("You Clicked PNG button")
                print("Gone back")
                running=False
                import main 
                
  
    screen.fill(GRAY)
    screen.blit(img0, rect0)
    screen.blit(p0,textRectp0)
    screen.blit(p1,textRectp1)
    screen.blit(p2,textRectp2)
    
    
    #---Buttons
    button1.draw(screen)
    button2.draw(screen)
    button3.draw(screen)
    pygame.display.update()




