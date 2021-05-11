import math
import pygame
import copy
import time
import sys
import os
import random
import pygame.gfxdraw
from pygame.locals import *

FPS = 120
winwdth = 940
winhgt = 740
txthgt = 20
bubblerad = 20
bubblewdth = bubblerad * 2
bubblelyrs = 5
bubadjst = 5
strx = winwdth / 2
strY = winhgt - 26
arywdth = 25
aryhgt = 20

RIGHT = 'right'
LEFT = 'left'
blank = '.'

vblue = (51, 255, 255)
black = (0, 0, 0)
white = (255, 255, 255)
grey = (100, 100, 100)
blue = (0, 0, 205)
red = (255, 0, 0)
white = (255, 255, 255)
pink = (255, 192, 203)
lightpink = (255, 182, 193)
hotpink = (255, 105, 180)
deeppink = (255, 20, 147)
cyan = (0, 255, 255)
peacockblue = (0, 164, 180)
grapecolor = (128, 49, 167)
amber = (255, 198, 0)
comic = (0, 174, 239)
lytgray = (217, 217, 214)
peach = (255, 229, 180)
green = (0, 255, 0)
GRAY = (100, 100, 100)
white = (255, 255, 255)
cyan = (0, 255, 255)
black = (0, 0, 0)

bgcolor = vblue
clrlist = [grey, blue, red, white, pink, peach, hotpink, green,
           deeppink, peacockblue, grapecolor, amber, comic, lytgray]


class Bubble(pygame.sprite.Sprite):
    def __init__(self, color, row=0, col=0):
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect(0, 0, 30, 30)
        self.rect.centerx = int(strx)
        self.rect.centery = strY
        self.speed = 10
        self.color = color
        self.radius = bubblerad
        self.angle = 0
        self.row = row
        self.col = col

    def update(self):

        if self.angle == 90:
            xmove = 0
            ymove = self.speed * -1
        elif self.angle < 90:
            xmove = self.xcalc(self.angle)
            ymove = self.ycalc(self.angle)
        elif self.angle > 90:
            xmove = self.xcalc(180 - self.angle) * -1
            ymove = self.ycalc(180 - self.angle)

        self.rect.x += int(xmove)
        self.rect.y += int(ymove)

    def draw(self):
        pygame.gfxdraw.filled_circle(
            dispsurf, self.rect.centerx, self.rect.centery, self.radius, self.color)
        pygame.gfxdraw.aacircle(
            dispsurf, self.rect.centerx, self.rect.centery, self.radius, GRAY)

    def xcalc(self, angle):
        radians = math.radians(angle)

        xmove = math.cos(radians)*(self.speed)
        return xmove

    def ycalc(self, angle):
        radians = math.radians(angle)

        ymove = math.sin(radians)*(self.speed) * -1
        return ymove


class Ary(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.angle = 90
        arrimg = pygame.image.load('Arrow.png')
        arrimg.convert_alpha()

        arrowRect = arrimg.get_rect()
        self.image = arrimg
        self.transformImage = self.image
        self.rect = arrowRect
        self.rect.centerx = int(strx)
        self.rect.centery = strY

    def update(self, dir):

        if (dir == LEFT and self.angle < 180):
            self.angle += 2
        elif (dir == RIGHT and self.angle > 0):
            self.angle -= 2

        self.transformImage = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.transformImage.get_rect()
        self.rect.centerx = int(strx)
        self.rect.centery = strY

    def draw(self):
        dispsurf.blit(self.transformImage, self.rect)


class Score(object):
    def __init__(self):
        self.total = 0
        self.font = pygame.font.SysFont('merlin', 35)
        self.render = self.font.render(
            'Score: ' + str(self.total), True, black, white)
        self.rect = self.render.get_rect()
        self.rect.left = 5
        self.rect.bottom = winhgt - 5

    def update(self, dellst):
        self.total += ((len(dellst)) * 10)
        self.render = self.font.render(
            'Score: ' + str(self.total), True, black, white)

    def draw(self):
        dispsurf.blit(self.render, self.rect)


def main():

    global fpsclock, dispsurf, disprect, mainfont
    pygame.init()

    fpsclock = pygame.time.Clock()
    pygame.display.set_caption('Bubble Shooter')
    mainfont = pygame.font.SysFont('Comic Sans MS', txthgt)
    dispsurf, disprect = makeDisplay()

    while True:
        score, winorlose = rngame()
        endScreen(score, winorlose)


def rngame():
    musclist = ['Whatever_It _Takes_OGG.ogg', 'bgmusic.ogg', 'Goofy_Theme.ogg']
    pygame.mixer.music.load(musclist[0])
    pygame.mixer.music.play()
    track = 0
    gameclrlist = copy.deepcopy(clrlist)
    dir = None
    launchbb = False
    newbb = None

    arrow = Ary()
    bbarr = mkeblkbrd()
    setbb(bbarr, gameclrlist)

    nxtbb = Bubble(gameclrlist[0])
    nxtbb.rect.right = winwdth - 5
    nxtbb.rect.bottom = winhgt - 5

    score = Score()

    while True:
        dispsurf.fill(bgcolor)

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            elif event.type == KEYDOWN:
                if (event.key == K_LEFT):
                    dir = LEFT
                elif (event.key == K_RIGHT):
                    dir = RIGHT

            elif event.type == KEYUP:
                dir = None
                if event.key == K_SPACE:
                    launchbb = True
                elif event.key == K_ESCAPE:
                    terminate()

        if launchbb == True:
            if newbb == None:
                newbb = Bubble(nxtbb.color)
                newbb.angle = arrow.angle

            newbb.update()
            newbb.draw()

            if newbb.rect.right >= winwdth - 5:
                newbb.angle = 180 - newbb.angle
            elif newbb.rect.left <= 5:
                newbb.angle = 180 - newbb.angle
            launchbb, newbb, score = stbb(bbarr, newbb, launchbb, score)

            fbblist = []
            for row in range(len(bbarr)):
                for col in range(len(bbarr[0])):
                    if bbarr[row][col] != blank:
                        fbblist.append(bbarr[row][col])
                        if bbarr[row][col].rect.bottom > (winhgt - arrow.rect.height - 10):
                            return score.total, 'lose'

            if len(fbblist) < 1:
                return score.total, 'win'
            gameclrlist = updtclrlist(bbarr)
            random.shuffle(gameclrlist)
            if launchbb == False:

                nxtbb = Bubble(gameclrlist[0])
                nxtbb.rect.right = winwdth - 5
                nxtbb.rect.bottom = winhgt - 5

        nxtbb.draw()
        if launchbb == True:
            covnxtbb()

        arrow.update(dir)
        arrow.draw()

        setarrpos(bbarr)
        drawbbary(bbarr)

        score.draw()

        if pygame.mixer.music.get_busy() == False:
            if track == len(musclist) - 1:
                track = 0
            else:
                track += 1

            pygame.mixer.music.load(musclist[track])
            pygame.mixer.music.play()

        pygame.display.update()
        fpsclock.tick(FPS)


def mkeblkbrd():
    array = []

    for row in range(aryhgt):
        col = []
        for i in range(arywdth):
            col.append(blank)
        array.append(col)

    return array


def setbb(array, gameclrlist):
    for row in range(bubblelyrs):
        for col in range(len(array[row])):
            random.shuffle(gameclrlist)
            newbb = Bubble(gameclrlist[0], row, col)
            array[row][col] = newbb

    setarrpos(array)


def setarrpos(array):
    for row in range(aryhgt):
        for col in range(len(array[row])):
            if array[row][col] != blank:
                array[row][col].rect.x = (bubblewdth * col) + 5
                array[row][col].rect.y = (bubblewdth * row) + 5

    for row in range(1, aryhgt, 2):
        for col in range(len(array[row])):
            if array[row][col] != blank:
                array[row][col].rect.x += bubblerad

    for row in range(1, aryhgt):
        for col in range(len(array[row])):
            if array[row][col] != blank:
                array[row][col].rect.y -= (bubadjst * row)

    delextrbb(array)


def delextrbb(array):
    for row in range(aryhgt):
        for col in range(len(array[row])):
            if array[row][col] != blank:
                if array[row][col].rect.right > winwdth:
                    array[row][col] = blank


def updtclrlist(bbarr):
    newColorList = []
    for row in range(len(bbarr)):
        for col in range(len(bbarr[0])):
            if bbarr[row][col] != blank:
                newColorList.append(bbarr[row][col].color)

    colorSet = set(newColorList)

    if len(colorSet) < 1:
        colorList = []
        colorList.append(white)
        return colorList
    else:

        return list(colorSet)


def chkfflotrs(bbarr):
    bubbleList = [col for col in range(len(bbarr[0]))
                  if bbarr[0][col] != blank]

    newbbList = []

    for i in range(len(bubbleList)):
        if i == 0:
            newbbList.append(bubbleList[i])
        elif bubbleList[i] > bubbleList[i - 1] + 1:
            newbbList.append(bubbleList[i])

    cpyofbrd = copy.deepcopy(bbarr)

    for row in range(len(bbarr)):
        for col in range(len(bbarr[0])):
            bbarr[row][col] = blank

    for col in newbbList:
        popflotrs(bbarr, cpyofbrd, col)


def popflotrs(bbarr, cpyofbrd, col, row=0):
    if (row < 0 or row > (len(bbarr)-1)
            or col < 0 or col > (len(bbarr[0])-1)):
        return
    elif cpyofbrd[row][col] == blank:
        return
    elif bbarr[row][col] == cpyofbrd[row][col]:
        return
    bbarr[row][col] = cpyofbrd[row][col]
    if(row == 0):
        popflotrs(bbarr, cpyofbrd, col + 1, row)
        popflotrs(bbarr, cpyofbrd, col - 1, row)
        popflotrs(bbarr, cpyofbrd, col, row + 1)
        popflotrs(bbarr, cpyofbrd, col - 1, row + 1)
    elif(row % 2 == 0):
        popflotrs(bbarr, cpyofbrd, col + 1, row)
        popflotrs(bbarr, cpyofbrd, col - 1, row)
        popflotrs(bbarr, cpyofbrd, col, row + 1)
        popflotrs(bbarr, cpyofbrd, col - 1, row + 1)
        popflotrs(bbarr, cpyofbrd, col, row - 1)
        popflotrs(bbarr, cpyofbrd, col - 1, row - 1)
    else:
        popflotrs(bbarr, cpyofbrd, col + 1, row)
        popflotrs(bbarr, cpyofbrd, col - 1, row)
        popflotrs(bbarr, cpyofbrd, col, row + 1)
        popflotrs(bbarr, cpyofbrd, col + 1, row + 1)
        popflotrs(bbarr, cpyofbrd, col, row - 1)
        popflotrs(bbarr, cpyofbrd, col + 1, row - 1)


def stbb(bbarr, newbb, launchbb, score):
    dellst = []
    popSound = pygame.mixer.Sound('popcork.ogg')

    for row in range(len(bbarr)):
        for col in range(len(bbarr[row])):

            if (bbarr[row][col] != blank and newbb != None):
                if (pygame.sprite.collide_rect(newbb, bbarr[row][col])) or newbb.rect.top < 0:
                    if newbb.rect.top < 0:
                        newRow, newcol = addbbtotop(bbarr, newbb)

                    elif newbb.rect.centery >= bbarr[row][col].rect.centery:

                        if newbb.rect.centerx >= bbarr[row][col].rect.centerx:
                            if row == 0 or (row) % 2 == 0:
                                newRow = row + 1
                                newcol = col
                                if bbarr[newRow][newcol] != blank:
                                    newRow = newRow - 1
                                bbarr[newRow][newcol] = copy.copy(newbb)
                                bbarr[newRow][newcol].row = newRow
                                bbarr[newRow][newcol].col = newcol

                            else:
                                newRow = row + 1
                                newcol = col + 1
                                if bbarr[newRow][newcol] != blank:
                                    newRow = newRow - 1
                                bbarr[newRow][newcol] = copy.copy(newbb)
                                bbarr[newRow][newcol].row = newRow
                                bbarr[newRow][newcol].col = newcol

                        elif newbb.rect.centerx < bbarr[row][col].rect.centerx:
                            if row == 0 or row % 2 == 0:
                                newRow = row + 1
                                newcol = col - 1
                                if newcol < 0:
                                    newcol = 0
                                if bbarr[newRow][newcol] != blank:
                                    newRow = newRow - 1
                                bbarr[newRow][newcol] = copy.copy(newbb)
                                bbarr[newRow][newcol].row = newRow
                                bbarr[newRow][newcol].col = newcol
                            else:
                                newRow = row + 1
                                newcol = col
                                if bbarr[newRow][newcol] != blank:
                                    newRow = newRow - 1
                                bbarr[newRow][newcol] = copy.copy(newbb)
                                bbarr[newRow][newcol].row = newRow
                                bbarr[newRow][newcol].col = newcol

                    elif(newbb.rect.centery < bbarr[row][col].rect.centery):
                        if(newbb.rect.centerx >= bbarr[row][col].rect.centerx):
                            if(row == 0 or row % 2 == 0):
                                newRow = row - 1
                                newcol = col
                                if(bbarr[newRow][newcol] != blank):
                                    newRow = newRow + 1
                                bbarr[newRow][newcol] = copy.copy(newbb)
                                bbarr[newRow][newcol].row = newRow
                                bbarr[newRow][newcol].col = newcol
                            else:
                                newRow = row - 1
                                newcol = col + 1
                                if bbarr[newRow][newcol] != blank:
                                    newRow = newRow + 1
                                bbarr[newRow][newcol] = copy.copy(newbb)
                                bbarr[newRow][newcol].row = newRow
                                bbarr[newRow][newcol].col = newcol

                        elif newbb.rect.centerx <= bbarr[row][col].rect.centerx:
                            if(row == 0 or row % 2 == 0):
                                newRow = row - 1
                                newcol = col - 1
                                if(bbarr[newRow][newcol] != blank):
                                    newRow = newRow + 1
                                bbarr[newRow][newcol] = copy.copy(newbb)
                                bbarr[newRow][newcol].row = newRow
                                bbarr[newRow][newcol].col = newcol

                            else:
                                newRow = row - 1
                                newcol = col
                                if(bbarr[newRow][newcol] != blank):
                                    newRow = newRow + 1
                                bbarr[newRow][newcol] = copy.copy(newbb)
                                bbarr[newRow][newcol].row = newRow
                                bbarr[newRow][newcol].col = newcol

                    popbb(bbarr, newRow, newcol, newbb.color, dellst)

                    if(len(dellst) >= 3):
                        for pos in dellst:
                            popSound.play()
                            row = pos[0]
                            col = pos[1]
                            bbarr[row][col] = blank
                        chkfflotrs(bbarr)

                        score.update(dellst)

                    launchbb = False
                    newbb = None

    return launchbb, newbb, score


def addbbtotop(bbarr, bubble):
    posx = bubble.rect.centerx
    leftSidex = posx-bubblerad
    coldiv = math.modf(float(leftSidex)/float(bubblewdth))
    col = int(coldiv[1])
    if (coldiv[0] < 0.5):
        bbarr[0][col] = copy.copy(bubble)
    else:
        col += 1
        bbarr[0][col] = copy.copy(bubble)
    row = 0
    return row, col


def popbb(bbarr, row, col, color, dellst):
    if(row < 0 or col < 0 or row > (len(bbarr)-1) or col > (len(bbarr[0])-1)):
        return
    elif (bbarr[row][col] == blank):
        return
    elif(bbarr[row][col].color != color):
        return
    for bubble in dellst:
        if(bbarr[bubble[0]][bubble[1]] == bbarr[row][col]):
            return
    dellst.append((row, col))
    if(row == 0):
        popbb(bbarr, row, col-1, color, dellst)
        popbb(bbarr, row, col+1, color, dellst)
        popbb(bbarr, row+1, col, color, dellst)
        popbb(bbarr, row+1, col-1, color, dellst)
    elif(row % 2 == 0):
        popbb(bbarr, row + 1, col, color, dellst)
        popbb(bbarr, row + 1, col-1, color, dellst)
        popbb(bbarr, row - 1, col, color, dellst)
        popbb(bbarr, row - 1, col - 1, color, dellst)
        popbb(bbarr, row, col+1, color, dellst)
        popbb(bbarr, row, col-1, color, dellst)

    else:
        popbb(bbarr, row - 1, col, color, dellst)
        popbb(bbarr, row - 1, col + 1, color, dellst)
        popbb(bbarr, row + 1, col, color, dellst)
        popbb(bbarr, row + 1, col + 1, color, dellst)
        popbb(bbarr, row, col + 1, color, dellst)
        popbb(bbarr, row, col - 1, color, dellst)


def drawbbary(array):
    for row in range(aryhgt):
        for col in range(len(array[row])):
            if(array[row][col] != blank):
                array[row][col].draw()


def makeDisplay():
    dispsurf = pygame.display.set_mode((winwdth, winhgt))
    disprect = dispsurf.get_rect()
    dispsurf.fill(bgcolor)
    dispsurf.convert()
    pygame.display.update()

    return dispsurf, disprect


def terminate():
    pygame.quit()
    sys.exit()


def covnxtbb():
    whiteRect = pygame.Rect(0, 0, bubblewdth, bubblewdth)
    whiteRect.bottom = winhgt
    whiteRect.right = winwdth
    pygame.draw.rect(dispsurf, bgcolor, whiteRect)


def endScreen(score, winorlose):
    endFont = pygame.font.SysFont('merlin', 50)
    endMessage1 = endFont.render('You ' + winorlose + '! Hey Your Scored  ' + str(
        score) + '. Press Enter to Play Again.', True, black, bgcolor)
    endMessage1Rect = endMessage1.get_rect()
    endMessage1Rect.center = disprect.center

    dispsurf.fill(bgcolor)
    dispsurf.blit(endMessage1, endMessage1Rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if(event.type == QUIT):
                terminate()
            elif(event.type == KEYUP):
                if(event.key == K_RETURN):
                    return
                elif(event.key == K_ESCAPE):
                    terminate()


if __name__ == '__main__':
    main()
