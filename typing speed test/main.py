import sys
import time
import random
import pygame
from pygame.locals import *


class Test:

    def __init__(self):
        self.color_heading = (255, 213, 102)
        self.color_text = (255, 0, 0)
        self.color_results = (255, 70, 70)
        self.w = 750
        self.h = 490
        self.reset = True
        self.wpm = 0
        self.end = False
        self.active = False
        self.input_text = ''
        self.word = ''
        self.results = 'Time:0 Accuracy:0 % WPM:0 '
        self.start_time = 0
        self.overall_time = 0
        self.accuracy = '0%'

        pygame.init()
        self.image_open = pygame.image.load('typing_speed.png')
        self.image_open = pygame.transform.scale(
            self.image_open, (self.w, self.h))

        self.bg = pygame.image.load('background.png')
        self.bg = pygame.transform.scale(self.bg, (900, 750))

        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Typing Speed Test')

    def draw_text(self, screen, message, y_val, f_size, color):
        font = pygame.font.Font(None, f_size)
        text = font.render(message, 1, color)
        text_rect = text.get_rect(center=(self.w/2, y_val))
        screen.blit(text, text_rect)
        pygame.display.update()

    def get_challenge(self):
        return random.choice(open('sentences.txt').read().split('\n'))

    def results_show(self, screen):
        if(not self.end):
            # Calculate time ellapsed
            self.overall_time = time.time() - self.start_time
            count = 0
            for i, c in enumerate(self.word):
                try:
                    if self.input_text[i] == c:
                        count = count + 1
                except:
                    pass
            # count is the number of correct typed characters
            # Calculate accuracy using given formula
            self.accuracy = (count*100)/len(self.word)

            # Calculate Words per Minute
            self.wpm = (len(self.input_text)*60)/(5*self.overall_time)
            self.end = True
            print(self.overall_time)

            self.results = 'Time:'+str(round(self.overall_time)) + " secs   Accuracy:" + str(
                round(self.accuracy)) + "%" + '   WPM: ' + str(round(self.wpm))

            # Draw Icon image
            self.time_img = pygame.image.load('icon.png')
            self.time_img = pygame.transform.scale(self.time_img, (150, 150))
            screen.blit(self.time_img, (self.w/2-75, self.h-140))
            self.draw_text(screen, "Reset", self.h - 70, 26, (255, 0, 0))

            print(self.results)
            pygame.display.update()

    def run(self):
        # everytime we run it should automatically reset the variables
        self.reset_game()

        # a variable which shows the state of game whether
        # it is running or not
        self.running = True

        # we will run an infinite loop till the running is True
        while(self.running):
            clock = pygame.time.Clock()
            self.screen.fill((0, 0, 0), (50, 250, 650, 50))
            pygame.draw.rect(self.screen, self.color_heading,
                             (50, 250, 650, 50), 2)
            # Update the text of user input dynamically
            self.draw_text(self.screen, self.input_text,
                           274, 26, (250, 250, 250))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    # get the position of mouse pointer x,y
                    x, y = pygame.mouse.get_pos()

                    # position of input box
                    # these x and y values should lie as
                    # x = [50,650] and y = [250,300] because the timer
                    # will start when user clicks the input box

                    if(x >= 50 and x <= 650 and y >= 250 and y <= 300):
                        self.active = True
                        self.input_text = ''
                        self.start_time = time.time()

                    # position of reset box
                    if(x >= 310 and x <= 510 and y >= 390 and self.end):
                        self.reset_game()
                        x, y = pygame.mouse.get_pos()

                elif event.type == pygame.KEYDOWN:
                    if self.active and not self.end:
                        if event.key == pygame.K_RETURN:
                            print(self.input_text)
                            self.results_show(self.screen)
                            print(self.results)
                            self.draw_text(self.screen, self.results,
                                           350, 28, self.color_results)
                            self.end = True

                        # event handler for backspace
                        # i.e simply take the string upto the second last character
                        elif event.key == pygame.K_BACKSPACE:
                            self.input_text = self.input_text[:-1]
                        else:
                            try:
                                self.input_text += event.unicode
                            except:
                                pass

            pygame.display.update()
        # clock timer
        clock.tick(60)

    def reset_game(self):
        self.screen.blit(self.image_open, (0, 0))

        pygame.display.update()
        time.sleep(1)

        # reset all the project variables.
        self.reset = False
        self.end = False

        self.input_text = ''
        self.word = ''
        self.start_time = 0
        self.overall_time = 0
        self.wpm = 0

        self.word = self.get_challenge()
        if (not self.word):
            self.reset_game()

        self.screen.fill((0, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        message = "Typing Speed Test"
        self.draw_text(self.screen, message, 80, 80, self.color_heading)

        pygame.draw.rect(self.screen, (255, 192, 25), (50, 250, 650, 50), 2)

        self.draw_text(self.screen, self.word, 200, 28, self.color_text)

        pygame.display.update()


if __name__ == '__main__':
    Test().run()
