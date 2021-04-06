import math,pygame,copy,time,sys,os,random
import pygame.gfxdraw
from pygame.locals import *

FPS          = 120
winwdth  = 940
winhgt = 740
txthgt   = 20
bubblerad = 20
bubblewdth  = bubblerad * 2
bubblelyrs = 5
bubadjst = 5
strx = winwdth /2
strY = winhgt - 26
arywdth = 25
aryhgt = 20

RIGHT = 'right'
LEFT  = 'left'
blank = '.'

vblue=(51,255,255)
black=(0,0,0)
white=(255,255,255)
grey=(100,100,100)
blue=(0,0,205)
red=(255,0,0)
white=(255,255,255)
pink=(255,192,203)
lightpink=(255,182,193)
hotpink=(255,105,180)
deeppink=(255,20,147)
cyan=(0,255,255)
peacockblue=(0,164,180)
grapecolor=(128,49,167)
amber=(255,198,0)
comic=(0,174,239)
lytgray=(217,217,214)
peach=(255,229,180)
green=(0, 255,0)
GRAY     = (100, 100, 100)
white    = (255, 255, 255)
cyan     = (  0, 255, 255)
black    = (  0,   0,   0)



bgcolor    = vblue
clrlist =[grey,blue,red,white,pink,peach,hotpink,green,deeppink,peacockblue,grapecolor,amber,comic,lytgray] 

class Bubble(pygame.sprite.Sprite):
    def __init__(self, color, row=0, column=0):
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect(0, 0, 30, 30)
        self.rect.centerx = int(strx)
        self.rect.centery = strY
        self.speed = 10
        self.color = color
        self.radius = bubblerad
        self.angle = 0
        self.row = row
        self.column = column
        
    def update(self):

        if self.angle == 90:
            xmove = 0
            ymove = self.speed * -1
        elif self.angle < 90:
            xmove = self.xcalculate(self.angle)
            ymove = self.ycalculate(self.angle)
        elif self.angle > 90:
            xmove = self.xcalculate(180 - self.angle) * -1
            ymove = self.ycalculate(180 - self.angle)
        

        self.rect.x += int(xmove)
        self.rect.y += int(ymove)


    def draw(self):
        pygame.gfxdraw.filled_circle(DISPLAYSURF, self.rect.centerx, self.rect.centery, self.radius, self.color)
        pygame.gfxdraw.aacircle(DISPLAYSURF, self.rect.centerx, self.rect.centery, self.radius, GRAY)
        


    def xcalculate(self, angle):
        radians = math.radians(angle)
        
        xmove = math.cos(radians)*(self.speed)
        return xmove

    def ycalculate(self, angle):
        radians = math.radians(angle)
        
        ymove = math.sin(radians)*(self.speed) * -1
        return ymove




class Ary(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.angle = 90
        arrowImage = pygame.image.load('Arrow.png')
        arrowImage.convert_alpha()
       
        arrowRect = arrowImage.get_rect()
        self.image = arrowImage
        self.transformImage = self.image
        self.rect = arrowRect
        self.rect.centerx = int(strx) 
        self.rect.centery = strY
        


    def update(self, direction):
        
        if direction == LEFT and self.angle < 180:
            self.angle += 2
        elif direction == RIGHT and self.angle > 0:        
            self.angle -= 2

        self.transformImage = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.transformImage.get_rect()
        self.rect.centerx = int(strx) 
        self.rect.centery = strY

        
    def draw(self):
        DISPLAYSURF.blit(self.transformImage, self.rect)
        


class Score(object):
    def __init__(self):
        self.total = 0
        self.font = pygame.font.SysFont('merlin', 35)
        self.render = self.font.render('Score: ' + str(self.total), True, black, white)
        self.rect = self.render.get_rect()
        self.rect.left = 5
        self.rect.bottom = winhgt - 5
        
        
    def update(self, deleteList):
        self.total += ((len(deleteList)) * 10)
        self.render = self.font.render('Score: ' + str(self.total), True, black, white)

    def draw(self):
        DISPLAYSURF.blit(self.render, self.rect)







def main():
 
    global FPSCLOCK, DISPLAYSURF, DISPLAYRECT, MAINFONT
    pygame.init()
    


    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Bubble Shooter')
    MAINFONT = pygame.font.SysFont('Comic Sans MS', txthgt)
    DISPLAYSURF, DISPLAYRECT = makeDisplay()
    
    

    while True:
        score, winorlose = runGame()
        endScreen(score, winorlose)
            
        



def runGame():
    musicList =['Whatever_It _Takes_OGG.ogg','bgmusic.ogg','Goofy_Theme.ogg']
    pygame.mixer.music.load(musicList[0])
    pygame.mixer.music.play()
    track = 0
    gameColorList = copy.deepcopy(clrlist)
    direction = None
    launchBubble = False
    newBubble = None
    
    
    
    arrow = Ary()
    bubbleArray = makeBlankBoard()
    setBubbles(bubbleArray, gameColorList)
    
    nextBubble = Bubble(gameColorList[0])
    nextBubble.rect.right = winwdth - 5
    nextBubble.rect.bottom = winhgt - 5

    score = Score()
    
    
    
   
    while True:
        DISPLAYSURF.fill(bgcolor)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
                
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT):
                    direction = LEFT
                elif (event.key == K_RIGHT):
                    direction = RIGHT
                    
            elif event.type == KEYUP:
                direction = None
                if event.key == K_SPACE:
                    launchBubble = True
                elif event.key == K_ESCAPE:
                    terminate()

        if launchBubble == True:
            if newBubble == None:
                newBubble = Bubble(nextBubble.color)
                newBubble.angle = arrow.angle
                

            newBubble.update()
            newBubble.draw()
            
            
            if newBubble.rect.right >= winwdth - 5:
                newBubble.angle = 180 - newBubble.angle
            elif newBubble.rect.left <= 5:
                newBubble.angle = 180 - newBubble.angle


            launchBubble, newBubble, score = stopBubble(bubbleArray, newBubble, launchBubble, score)

            finalBubbleList = []
            for row in range(len(bubbleArray)):
                for column in range(len(bubbleArray[0])):
                    if bubbleArray[row][column] != blank:
                        finalBubbleList.append(bubbleArray[row][column])
                        if bubbleArray[row][column].rect.bottom > (winhgt - arrow.rect.height - 10):
                            return score.total, 'lose'

            
            
            if len(finalBubbleList) < 1:
                return score.total, 'win'
                                        
                        
            
            gameColorList = updateColorList(bubbleArray)
            random.shuffle(gameColorList)
            
                    
                            
            if launchBubble == False:
                
                nextBubble = Bubble(gameColorList[0])
                nextBubble.rect.right = winwdth - 5
                nextBubble.rect.bottom = winhgt - 5

        
        
                            
        nextBubble.draw()
        if launchBubble == True:
            coverNextBubble()
        
        arrow.update(direction)
        arrow.draw()


        
        setArrayPos(bubbleArray)
        drawBubbleArray(bubbleArray)

        score.draw()

        if pygame.mixer.music.get_busy() == False:
            if track == len(musicList) - 1:
                track = 0
            else:
                track += 1

            pygame.mixer.music.load(musicList[track])
            pygame.mixer.music.play()

            
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)




def makeBlankBoard():
    array = []
    
    for row in range(aryhgt):
        column = []
        for i in range(arywdth):
            column.append(blank)
        array.append(column)

    return array




def setBubbles(array, gameColorList):
    for row in range(bubblelyrs):
        for column in range(len(array[row])):
            random.shuffle(gameColorList)
            newBubble = Bubble(gameColorList[0], row, column)
            array[row][column] = newBubble 
            
    setArrayPos(array)





def setArrayPos(array):
    for row in range(aryhgt):
        for column in range(len(array[row])):
            if array[row][column] != blank:
                array[row][column].rect.x = (bubblewdth * column) + 5
                array[row][column].rect.y = (bubblewdth * row) + 5

    for row in range(1, aryhgt, 2):
        for column in range(len(array[row])):
            if array[row][column] != blank:
                array[row][column].rect.x += bubblerad
                

    for row in range(1, aryhgt):
        for column in range(len(array[row])):
            if array[row][column] != blank:
                array[row][column].rect.y -= (bubadjst * row)

    deleteExtraBubbles(array)



def deleteExtraBubbles(array):
    for row in range(aryhgt):
        for column in range(len(array[row])):
            if array[row][column] != blank:
                if array[row][column].rect.right > winwdth:
                    array[row][column] = blank



def updateColorList(bubbleArray):
    newColorList = []

    for row in range(len(bubbleArray)):
        for column in range(len(bubbleArray[0])):
            if bubbleArray[row][column] != blank:
                newColorList.append(bubbleArray[row][column].color)

    colorSet = set(newColorList)

    if len(colorSet) < 1:
        colorList = []
        colorList.append(white)
        return colorList

    else:

        return list(colorSet)
    
    



def checkForFloaters(bubbleArray):
    bubbleList = [column for column in range(len(bubbleArray[0]))
                         if bubbleArray[0][column] != blank]

    newBubbleList = []

    for i in range(len(bubbleList)):
        if i == 0:
            newBubbleList.append(bubbleList[i])
        elif bubbleList[i] > bubbleList[i - 1] + 1:
            newBubbleList.append(bubbleList[i])

    copyOfBoard = copy.deepcopy(bubbleArray)

    for row in range(len(bubbleArray)):
        for column in range(len(bubbleArray[0])):
            bubbleArray[row][column] = blank
    

    for column in newBubbleList:
        popFloaters(bubbleArray, copyOfBoard, column)



def popFloaters(bubbleArray, copyOfBoard, column, row=0):
    if (row < 0 or row > (len(bubbleArray)-1)
                or column < 0 or column > (len(bubbleArray[0])-1)):
        return
    
    elif copyOfBoard[row][column] == blank:
        return

    elif bubbleArray[row][column] == copyOfBoard[row][column]:
        return

    bubbleArray[row][column] = copyOfBoard[row][column]
    

    if row == 0:
        popFloaters(bubbleArray, copyOfBoard, column + 1, row)
        popFloaters(bubbleArray, copyOfBoard, column - 1, row)
        popFloaters(bubbleArray, copyOfBoard, column,row + 1)
        popFloaters(bubbleArray, copyOfBoard, column - 1, row + 1)

    elif row % 2 == 0:
        popFloaters(bubbleArray, copyOfBoard, column + 1, row)
        popFloaters(bubbleArray, copyOfBoard, column - 1, row)
        popFloaters(bubbleArray, copyOfBoard, column,row + 1)
        popFloaters(bubbleArray, copyOfBoard, column - 1, row + 1)
        popFloaters(bubbleArray, copyOfBoard, column,row - 1)
        popFloaters(bubbleArray, copyOfBoard, column - 1, row - 1)

    else:
        popFloaters(bubbleArray, copyOfBoard, column + 1, row)
        popFloaters(bubbleArray, copyOfBoard, column - 1, row)
        popFloaters(bubbleArray, copyOfBoard, column,row + 1)
        popFloaters(bubbleArray, copyOfBoard, column + 1, row + 1)
        popFloaters(bubbleArray, copyOfBoard, column,row - 1)
        popFloaters(bubbleArray, copyOfBoard, column + 1, row - 1)
        


def stopBubble(bubbleArray, newBubble, launchBubble, score):
    deleteList = []
    popSound = pygame.mixer.Sound('popcork.ogg')
    
    for row in range(len(bubbleArray)):
        for column in range(len(bubbleArray[row])):
            
            if (bubbleArray[row][column] != blank and newBubble != None):
                if (pygame.sprite.collide_rect(newBubble, bubbleArray[row][column])) or newBubble.rect.top < 0:
                    if newBubble.rect.top < 0:
                        newRow, newColumn = addBubbleToTop(bubbleArray, newBubble)
                        
                    elif newBubble.rect.centery >= bubbleArray[row][column].rect.centery:

                        if newBubble.rect.centerx >= bubbleArray[row][column].rect.centerx:
                            if row == 0 or (row) % 2 == 0:
                                newRow = row + 1
                                newColumn = column
                                if bubbleArray[newRow][newColumn] != blank:
                                    newRow = newRow - 1
                                bubbleArray[newRow][newColumn] = copy.copy(newBubble)
                                bubbleArray[newRow][newColumn].row = newRow
                                bubbleArray[newRow][newColumn].column = newColumn
                                
                            else:
                                newRow = row + 1
                                newColumn = column + 1
                                if bubbleArray[newRow][newColumn] != blank:
                                    newRow = newRow - 1
                                bubbleArray[newRow][newColumn] = copy.copy(newBubble)
                                bubbleArray[newRow][newColumn].row = newRow
                                bubbleArray[newRow][newColumn].column = newColumn
                                                    
                        elif newBubble.rect.centerx < bubbleArray[row][column].rect.centerx:
                            if row == 0 or row % 2 == 0:
                                newRow = row + 1
                                newColumn = column - 1
                                if newColumn < 0:
                                    newColumn = 0
                                if bubbleArray[newRow][newColumn] != blank:
                                    newRow = newRow - 1
                                bubbleArray[newRow][newColumn] = copy.copy(newBubble)
                                bubbleArray[newRow][newColumn].row = newRow
                                bubbleArray[newRow][newColumn].column = newColumn
                            else:
                                newRow = row + 1
                                newColumn = column
                                if bubbleArray[newRow][newColumn] != blank:
                                    newRow = newRow - 1
                                bubbleArray[newRow][newColumn] = copy.copy(newBubble)
                                bubbleArray[newRow][newColumn].row = newRow
                                bubbleArray[newRow][newColumn].column = newColumn
                                
                            
                    elif newBubble.rect.centery < bubbleArray[row][column].rect.centery:
                        if newBubble.rect.centerx >= bubbleArray[row][column].rect.centerx:
                            if row == 0 or row % 2 == 0:
                                newRow = row - 1
                                newColumn = column
                                if bubbleArray[newRow][newColumn] != blank:
                                    newRow = newRow + 1
                                bubbleArray[newRow][newColumn] = copy.copy(newBubble)
                                bubbleArray[newRow][newColumn].row = newRow
                                bubbleArray[newRow][newColumn].column = newColumn
                            else:
                                newRow = row - 1
                                newColumn = column + 1
                                if bubbleArray[newRow][newColumn] != blank:
                                    newRow = newRow + 1
                                bubbleArray[newRow][newColumn] = copy.copy(newBubble)
                                bubbleArray[newRow][newColumn].row = newRow
                                bubbleArray[newRow][newColumn].column = newColumn
                            
                        elif newBubble.rect.centerx <= bubbleArray[row][column].rect.centerx:
                            if row == 0 or row % 2 == 0:
                                newRow = row - 1
                                newColumn = column - 1
                                if bubbleArray[newRow][newColumn] != blank:
                                    newRow = newRow + 1
                                bubbleArray[newRow][newColumn] = copy.copy(newBubble)
                                bubbleArray[newRow][newColumn].row = newRow
                                bubbleArray[newRow][newColumn].column = newColumn
                                
                            else:
                                newRow = row - 1
                                newColumn = column
                                if bubbleArray[newRow][newColumn] != blank:
                                    newRow = newRow + 1
                                bubbleArray[newRow][newColumn] = copy.copy(newBubble)
                                bubbleArray[newRow][newColumn].row = newRow
                                bubbleArray[newRow][newColumn].column = newColumn


                    popBubbles(bubbleArray, newRow, newColumn, newBubble.color, deleteList)
                    
                    
                    if len(deleteList) >= 3:
                        for pos in deleteList:
                            popSound.play()
                            row = pos[0]
                            column = pos[1]
                            bubbleArray[row][column] = blank
                        checkForFloaters(bubbleArray)
                        
                        score.update(deleteList)

                    launchBubble = False
                    newBubble = None

    return launchBubble, newBubble, score

                    

def addBubbleToTop(bubbleArray, bubble):
    posx = bubble.rect.centerx
    leftSidex = posx - bubblerad

    columnDivision = math.modf(float(leftSidex) / float(bubblewdth))
    column = int(columnDivision[1])

    if columnDivision[0] < 0.5:
        bubbleArray[0][column] = copy.copy(bubble)
    else:
        column += 1
        bubbleArray[0][column] = copy.copy(bubble)

    row = 0
    

    return row, column
    
    


def popBubbles(bubbleArray, row, column, color, deleteList):
    if row < 0 or column < 0 or row > (len(bubbleArray)-1) or column > (len(bubbleArray[0])-1):
        return

    elif bubbleArray[row][column] == blank:
        return
    
    elif bubbleArray[row][column].color != color:
        return

    for bubble in deleteList:
        if bubbleArray[bubble[0]][bubble[1]] == bubbleArray[row][column]:
            return

    deleteList.append((row, column))

    if row == 0:
        popBubbles(bubbleArray, row,column - 1, color, deleteList)
        popBubbles(bubbleArray, row,column + 1, color, deleteList)
        popBubbles(bubbleArray, row + 1, column,     color, deleteList)
        popBubbles(bubbleArray, row + 1, column - 1, color, deleteList)

    elif row % 2 == 0:
        
        popBubbles(bubbleArray, row + 1, column,color, deleteList)
        popBubbles(bubbleArray, row + 1, column - 1,color, deleteList)
        popBubbles(bubbleArray, row - 1, column,color, deleteList)
        popBubbles(bubbleArray, row - 1, column - 1,color, deleteList)
        popBubbles(bubbleArray, row,column + 1,color, deleteList)
        popBubbles(bubbleArray, row,column - 1,color, deleteList)

    else:
        popBubbles(bubbleArray, row - 1, column,color, deleteList)
        popBubbles(bubbleArray, row - 1, column + 1, color, deleteList)
        popBubbles(bubbleArray, row + 1, column,color, deleteList)
        popBubbles(bubbleArray, row + 1, column + 1, color, deleteList)
        popBubbles(bubbleArray, row,column + 1, color, deleteList)
        popBubbles(bubbleArray, row,column - 1, color, deleteList)
            


def drawBubbleArray(array):
    for row in range(aryhgt):
        for column in range(len(array[row])):
            if array[row][column] != blank:
                array[row][column].draw()


                    

def makeDisplay():
    DISPLAYSURF = pygame.display.set_mode((winwdth, winhgt))
    DISPLAYRECT = DISPLAYSURF.get_rect()
    DISPLAYSURF.fill(bgcolor)
    DISPLAYSURF.convert()
    pygame.display.update()

    return DISPLAYSURF, DISPLAYRECT
    
 
def terminate():
    pygame.quit()
    sys.exit()


def coverNextBubble():
    whiteRect = pygame.Rect(0, 0, bubblewdth, bubblewdth)
    whiteRect.bottom = winhgt
    whiteRect.right = winwdth
    pygame.draw.rect(DISPLAYSURF, bgcolor, whiteRect)



def endScreen(score, winorlose):
    endFont = pygame.font.SysFont('merlin', 50)
    endMessage1 = endFont.render('You ' + winorlose + '! Hey Your Scored  ' + str(score) + '. Press Enter to Play Again.', True, black, bgcolor)
    endMessage1Rect = endMessage1.get_rect()
    endMessage1Rect.center = DISPLAYRECT.center

    DISPLAYSURF.fill(bgcolor)
    DISPLAYSURF.blit(endMessage1, endMessage1Rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYUP:
                if event.key == K_RETURN:
                    return
                elif event.key == K_ESCAPE:
                    terminate()
        
        
if __name__ == '__main__':
    main()
    

