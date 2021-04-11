import os 
import sys 
import pygame 
import random 
from pygame import *

pygame.init()

screen_size_display=(width,height)=(600,150)
FPS=60
gravity=0.6

black=(0,0,0)
white=(255,255,255)
back=(235,235,235)

high_score=0    

screen=pygame.display.set_mode(screen_size_display)
clock=pygame.time.Clock()
pygame.display.set_caption("Dino Game ")

jump_sound=pygame.mixer.Sound('resource\JUMP.wav')
die_sound =pygame.mixer.Sound('resource\die.wav')
checkpoint_sound = pygame.mixer.Sound('resource\checkPoint.wav')

def load_Image(name,sizex=-1,sizey=-1,colorkey=None,):

    full_name=os.path.join('resource',name)
    image=pygame.image.load(full_name)
    image=image.convert()

    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey,RLEACCEL)

    if sizex != -1 or sizey != -1 :
        image=pygame.transform.scale(image,(sizex,sizey))
    
    return (image,image.get_rect())


def load_Sprite_Sheet(sh_name,namex,namey,scalex=-1,scaley=-1,colorkey=None,):

    full_name = os.path.join('resource',sh_name)
    sheet=pygame.image.load(full_name)
    sheet=sheet.convert()

    sheet_rect = sheet.get_rect()

    sprites=[]

    sizex=sheet_rect.width/namex
    sizey=sheet_rect.height/namey

    for i in range(0,namey):
        for j in range(0,namex):
            rect=pygame.Rect(j*sizex,i*sizey,sizex,sizey)
            image=pygame.Surface(rect.size)
            image=image.convert()
            image.blit(sheet,(0,0),rect)

            if colorkey is not None:
                if colorkey is -1:
                    colorkey = image.get_at((0,0))
                image.set_colorkey(colorkey,RLEACCEL)

            if  scalex != -1 or scaley != -1:
                image=pygame.transform.scale(image,(scalex,scaley))

            sprites.append(image)

    sprite_rect = sprites[0].get_rect()
    return sprites,sprite_rect

def gameOver_display_messages(rbutton_image,gameover_image):
    rbutton_rect = rbutton_image.get_rect()
    rbutton_rect.centerx=width / 2
    rbutton_rect.top = height * 0.52

    gameover_rect = gameover_image.get_rect()
    gameover_rect.centerx=width / 2 
    gameover_rect.top = height * 0.35

    screen.blit(rbutton_image,rbutton_rect)
    screen.blit(gameover_image,gameover_rect)

def extractDigits(number):
    if number > -1:
        d=[]
        i=0
        while (number/10!=0):
            d.append(number%10)
            number=int(number/10)

        d.append(number%10)
        for i in range(len(d),5):
            d.append(0)
        d.reverse()
        return d 

class Dino():
    def __init__(self,sizex=-1,sizey=-1):
        self.images,self.rect=load_Sprite_Sheet('Dino.png',5,1,sizex,sizey,-1)
        self.images1,self.rect1=load_Sprite_Sheet('dino_ducking.png',2,1,59,sizey,-1)
        self.rect.bottom=int(0.98 * height)
        self.rect.left=width/15
        self.image=self.images[0]
        self.index=0
        self.counter=0
        self.score=0
        self.jumping=False
        self.dead=False
        self.ducking=False
        self.blinking=False
        self.movement = [0,0]
        self.jumpspeed=11.5

        self.stand_position_width=self.rect.width
        self.duck_position_width=self.rect1.width

    def draw(self):
        screen.blit(self.image,self.rect)

    def Checkbounds(self):
        if self.rect.bottom > int(0.98 * height):
            self.rect.bottom = int(0.98 * height)
            self.jumping =False

    def update(self):
        if self.jumping:
            self.movement[1]=self.movement[1]+gravity

        if self.jumping:
            self.index=0
        elif self.blinking:
            if self.index ==0:
                if self.counter % 400 ==399:
                    self.index=(self.index+1)%2
            else:
                if self.counter % 20 ==19:
                    self.index=(self.index+1)%2
        
        elif self.ducking:
            if self.counter % 5 ==0:
                self.index=(self.index+1)%2
        else:
            if self.counter % 5 ==0:
                self.index=(self.index+1)%2 + 2 

        if self.dead:
            self.index=4
        
        if not self.ducking:
            self.image = self.images[self.index]
            self.rect.width = self.stand_position_width
        else:
            self.image = self.images1[(self.index) % 2]
            self.rect.width = self.duck_position_width

        self.rect = self.rect.move(self.movement)
        self.Checkbounds()

        if not self.dead and self.counter % 7 == 6 and self.blinking == False:
            self.score+=1
            if self.score % 100 == 0 and self.score !=0:
                if  pygame.mixer.get_init() != None:
                    checkpoint_sound.play()
        
        self.counter = (self.counter + 1) 

class Cactus(pygame.sprite.Sprite):
    def __init__(self,speed=5,sizex=-1,sizey=-1):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.images,self.rect = load_Sprite_Sheet('cactus-small.png',3,1,sizex,sizey,-1)
        self.rect.bottom = int(0.98 * height)
        self.rect.left=width+self.rect.width
        self.image =self.images[random.randrange(0,3)]
        self.movement = [-1*speed,0]


    def draw(self):
        screen.blit(self.image,self.rect)

    def update(self):
        self.rect=self.rect.move(self.movement)

        if self.rect.right < 0:
            self.kill()

class Birds(pygame.sprite.Sprite):
    def __init__(self,speed=5,sizex=-1,sizey=-1):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.images,self.rect = load_Sprite_Sheet('birds.png',2,1,sizex,sizey,-1)
        self.birds_height = [height * 0.82,height * 0.75,height * 0.60]
        self.rect.centery=self.birds_height[random.randrange(0,3)]
        self.rect.left=width +self.rect.width
        self.image = self.images[0]
        self.movement = [-1*speed,0]
        self.index=0
        self.counter=0
    
    def draw(self):
        screen.blit(self.image,self.rect)

    def update(self):
        if self.counter % 10 == 0:
            self.index = (self.index + 1) % 2
        self.image = self.images[self.index]
        self.rect = self.rect.move(self.movement)
        self.counter = (self.counter +1)
        if self.rect.right < 0:
            self.kill()

class Ground():
    def __init__(self,speed=-5):
        self.image,self.rect = load_Image('ground.png',-1,-1,-1)
        self.image1,self.rect1 = load_Image('ground.png',-1,-1,-1)
        self.rect.bottom = height
        self.rect1.bottom = height
        self.rect1.left = self.rect.right 
        self.speed = speed

    def draw(self):
        screen.blit(self.image,self.rect)
        screen.blit(self.image1,self.rect1)

    def update(self):
        self.rect.left +=self.speed
        self.rect1.left +=self.speed

        if self.rect.right < 0:
            self.rect.left = self.rect1.right 

        if self.rect1.right < 0:
            self.rect1.right = self.rect.right

class Cloud(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.image,self.rect=load_Image('cloud.png',int(90*30/42),30,-1)
        self.speed=1
        self.rect.left =x
        self.rect.top=y
        self.movement = [-1*self.speed,0]

    def draw(self):
        screen.blit(self.image, self.rect)
    
    def update(self):
        self.rect =self.rect.move(self.movement)
        if self.rect.right < 0:
            self.kill()

class Scoreboard():
    def __init__(self,x=-1,y=-1):
        self.score =0
        self.scr_image,self.scrrect =load_Sprite_Sheet('numbers.png',12,1,11,int(11*6/5),-1)
        self.image = pygame.Surface((55,int(11*6/5)))
        self.rect=self.image.get_rect()

        if x == -1:
            self.rect.left = width * 0.89
        else:
            self.rect.left = x 

        if y == -1:
            self.rect.top = height * 0.1
        else:
            self.rect.top = y

    def draw(self):
        screen.blit(self.image,self.rect)

    def update(self,score): 
        score_num=extractDigits(score)
        self.image.fill(back)
        for i in score_num:
            self.image.blit(self.scr_image[i],self.scrrect)
            self.scrrect.left += self.scrrect.width
        self.scrrect.left = 0

def Indroduction_screen():
    ad_dino = Dino(44,47)
    ad_dino.blinking = True
    starting_game = False

    temp_ground,temp_ground_rect = load_Sprite_Sheet('ground.png',15,1,-1,-1,-1 )
    temp_ground_rect.left = width/20
    temp_ground_rect.bottom = height

    logo,l_rect = load_Image('logo.png',300,140,-1)
    l_rect.centerx=width * 0.6
    l_rect.centery=height * 0.6

    while not starting_game:
        if pygame.display.get_surface() == None:
            print("Unable to load display screen")
            return True
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key==pygame.K_UP:
                        ad_dino.jumping = True 
                        ad_dino.blinking = False
                        ad_dino.movement[1]= -1*ad_dino.jumpspeed

        ad_dino.update()

        if pygame.display.get_surface() != None:
            screen.fill(back)
            screen.blit(temp_ground[0],temp_ground_rect)
            if ad_dino.blinking:
                screen.blit(logo,l_rect)
            ad_dino.draw()

            pygame.display.update()

            clock.tick(FPS)
            if ad_dino.jumping ==False and ad_dino.blinking == False:
                starting_game =  True 


def Gameplay():
    global high_score
    gameplay=4
    start_menu = False 
    Game_over = False
    Game_exit = False
    Gamer_Dino = Dino(44,47)
    new_ground = Ground(-1 * gameplay)
    score_boards = Scoreboard()
    highscore = Scoreboard(width * 0.78) 
    counter = 0 

    cacti = pygame.sprite.Group() 
    SmallBirds = pygame.sprite.Group() 
    SkyCloud = pygame.sprite.Group() 
    last_end = pygame.sprite.Group() 

    Cactus.containers = cacti
    Birds.containers = SmallBirds
    Cloud.containers = SkyCloud

    rbutton_image,rbutton_rect = load_Image('replay_button.png',35,31,-1)
    gameover_image,gameover_rect = load_Image('game_over.png',190,11,-1)

    temp_image,temp_rect = load_Sprite_Sheet('numbers.png',12,1,11,int(11*6/5),-1)
    ad_image = pygame.Surface((22,int(11*6/5)))
    ad_rect = ad_image.get_rect()
    ad_image.fill(back)
    ad_image.blit(temp_image[10],temp_rect)
    temp_rect.left += temp_rect.width
    ad_image.blit(temp_image[11],temp_rect)
    ad_rect.top = height * 0.1
    ad_rect.left = width * 0.73 

    while not Game_exit:
        while start_menu:
            pass
        while not Game_over:
            if pygame.display.get_surface() == None :
                print('Unable to display the screen')
                Game_exit = True 
                Game_over = True
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        Game_exit = True 
                        Game_over = True
                    
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            if Gamer_Dino.rect.bottom == int(0.98 * height):
                                Gamer_Dino.jumping = True
                                if pygame.mixer.get_init() != None:
                                    jump_sound.play()
                                Gamer_Dino.movement[1] = -1*Gamer_Dino.jumpspeed

                        if event.key == pygame.K_DOWN:
                            if not (Gamer_Dino.jumping and Gamer_Dino.dead):
                                Gamer_Dino.ducking = True

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_DOWN:
                            Gamer_Dino.ducking = False
            for c in cacti:
                c.movement[0] = -1*gameplay
                if pygame.sprite.collide_mask(Gamer_Dino, c):
                    Gamer_Dino.dead = True 
                    if pygame.mixer.get_init() != None:
                        die_sound.play()

            for b in SmallBirds:
                b.movement[0] = -1*gameplay
                if pygame.sprite.collide_mask(Gamer_Dino, b):
                    Gamer_Dino.dead = True 
                    if pygame.mixer.get_init() != None:
                        die_sound.play()

            if len(cacti) < 2:
                if len(cacti) == 0:
                    last_end.empty()
                    last_end.add(Cactus(gameplay,40,40))
                else:
                    for l in last_end:
                        if l.rect.right < width * 0.7 and random.randrange(0,50) == 10:
                            last_end.empty()
                            last_end.add(Cactus(gameplay,40,40))

            if len(SmallBirds) == 0 and random.randrange(0,200) == 10 and counter > 500:
                for l in last_end:
                    if l.rect.right < width * 0.8:
                        last_end.empty()
                        last_end.add(Birds(gameplay,46,40))

            if len(SkyCloud) < 5 and random.randrange(0,300) == 10:
                Cloud(width,random.randrange(height/5,height/2))

            Gamer_Dino.update()
            cacti.update()
            SmallBirds.update()
            SkyCloud.update()
            new_ground.update()
            score_boards.update(Gamer_Dino.score)
            highscore.update(high_score)

            if pygame.display.get_surface() != None:
                screen.fill(back)
                new_ground.draw()
                SkyCloud.draw(screen)
                score_boards.draw()
                if high_score != 0:
                    highscore.draw()
                    screen.blit(ad_image,ad_rect)
                cacti.draw(screen)
                SmallBirds.draw(screen)
                Gamer_Dino.draw()

                pygame.display.update()
            clock.tick(FPS)

            if Gamer_Dino.dead:
                Game_over = True
                if Gamer_Dino.score > high_score:
                    high_score = Gamer_Dino.score
            
            if counter % 700 == 699:
                new_ground.speed -= 1
                gameplay += 1

            counter += 1 

            if Game_exit:
                break
        
            while Game_over:
                if pygame.display.get_surface() == None:
                    print("Unable to load display surface ")
                    Game_exit = True
                    Game_over = False
                else:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            Game_exit = True
                            Game_over = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                Game_exit = True
                                Game_over = False
                        
                            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                                Game_over = False
                                Gameplay()
                highscore.update(high_score)
                if pygame.display.get_surface() != None:
                    gameOver_display_messages(rbutton_image,gameover_image)
                    if high_score != 0:
                        highscore.draw()
                        screen.blit(ad_image,ad_rect)
                    pygame.display.update()
                clock.tick(FPS)

    pygame.quit()
    quit() 

def main():
    GameQuit = Indroduction_screen()
    if not GameQuit:
        Gameplay()

main()
