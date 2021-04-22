# -*- coding: utf-8 -*-


import pygame as pg 

pg.init()

screen=pg.display.set_mode((500,500))
pg.display.set_caption('Buttons Pygame')


class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,screen,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pg.draw.rect(screen, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pg.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pg.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False
    
    
def redraw():
    screen.fill((164,235,243))
    greenButton.draw(screen,(0,0,0))
    redButton.draw(screen,(0,0,0))
    txt_surface1 = font.render(text1, True, color1)
       
    # Resize the box if the text is too long.
    width = max(200, txt_surface1.get_width()+10)
    input_box1.w = width
    
    # Blit the text.
    screen.blit(txt_surface1, (input_box1.x+5, input_box1.y+10))
    
    screen.blit(p1,textRectp1)
   
    # Blit the input_box rect.
    pg.draw.rect(screen,color1, input_box1,2)
    
    pg.display.flip()

def draw_enter():
    screen.fill((164,235,243))
    welcomeButton.draw(screen,(0,0,0))
    backButton.draw(screen,(0,0,0))

run=True
redButton=button((164,235,243),250,335,150,100,'Close')
greenButton=button((164,235,243),50,335,150,100,'Play')
welcomeButton=button((164,235,243),50,105,400,300,'Hi')

backButton=button((164,235,243),150,435,170,50,'Go Back')
game_is_going=True
enter_screen=False

input_box1 = pg.Rect(140, 170, 170, 50)
color_inactive = pg.Color((2, 0, 93))
color_active = pg.Color((33, 224, 239))
color1 = color_inactive
        
active1 = False
        
text1 = ''
font = pg.font.SysFont('comicsans', 60)
p1 = font.render('Enter Your Name ', True,(14, 43, 103))
        
textRectp1 = p1.get_rect()
   
textRectp1.center = (245, 115)


while(game_is_going):
    while(run):
        redraw()
        pg.display.update()
        
        for event in pg.event.get():
            pos=pg.mouse.get_pos()
            
            if event.type==pg.QUIT:
                run=False
                game_is_going=False
                pg.quit()
                
            
            if event.type == pg.KEYDOWN:
                if not active1:
                    if event.key == pg.K_RETURN:
                        print(text1)
                        
                    elif event.key == pg.K_BACKSPACE:
                        text1 = text1[:-1]
                    else:
                        text1 += event.unicode
                
        
            if event.type==pg.MOUSEBUTTONDOWN:
                
                if input_box1.collidepoint(event.pos):
                    # Toggle the active variable.
                    active1 = not active1
                else:
                    active1 = False
                color1 = color_active if active1 else color_inactive  
                if greenButton.isOver(pos):
                    print("Clicked Enter")
                    run=False
                    enter_screen=True
                elif redButton.isOver(pos):
                    print("Clicked Close")
                    run=False
                    game_is_going=False
                    pg.quit()
                    
            if event.type ==pg.MOUSEMOTION:
                if greenButton.isOver(pos):
                    greenButton.color=(158,222,11)
                elif redButton.isOver(pos):
                    redButton.color=(232, 69, 69)
                else:
                    greenButton.color=(164,235,243)
                    redButton.color=(164,235,243)
                
        
    while(enter_screen):
        draw_enter()
        pg.display.update()
        
        for event in pg.event.get():
            pos=pg.mouse.get_pos()
            welcomeButton.text="Hi "+str(text1)
            if event.type==pg.QUIT:
                enter_screen=False
                game_is_going=False
                pg.quit()
                
        
            if event.type==pg.MOUSEBUTTONDOWN:
                if backButton.isOver(pos):
                    print("Gone back")
                    run=True
                    enter_screen=False
            if event.type ==pg.MOUSEMOTION:
                if welcomeButton.isOver(pos):
                    welcomeButton.color=(158,222,11)
                elif backButton.isOver(pos):
                    backButton.color=(232, 69, 69)
                else:
                    welcomeButton.color=(164,235,243)
                    backButton.color=(164,235,243)
                
            
if __name__=="__main__":
    import ExampleButtons
    

