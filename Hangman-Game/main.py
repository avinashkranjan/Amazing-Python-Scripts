import pygame, math, random

#setup display
pygame.init() #initializing pygame module
WIDTH, HEIGHT= 800,500 #width and height in pixels background (where we want our game to be played)
win = pygame.display.set_mode((WIDTH,HEIGHT)) #creating dimensions for pygame, accepts tuple only
pygame.display.set_caption("Hangman Game") #give name to the game


#button variables
radius = 20
gap= 15
letters = []
startx= round((WIDTH - (radius * 2 + gap) * 13) / 2) #getting the x pos after some space, where we start at, /2-->coz one side
starty= 400 #x is more imp so set any value of y

A= 65

for i in range(26): #tells which button we are on
  x= startx + gap * 2+ ((radius * 2 + gap)* (i%13))
  y= starty + ((i//13) * (gap + radius * 2))
  letters.append([x, y, chr(A+i), True]) 



#load images
images = []
for i in range(7):
  img = pygame.image.load("hangman" + str(i) + ".png")
  images.append(img)




#game variables
hangman_status = 0 #the hangman img will display accordingly
list_of_words= ["abruptly","avenue","awkward","azure","galaxy","gossip","icebox","injury","ivory","ivy","jackpot","jaundice","joyful","juicy","jukebox","jumbo","kiwifruit","matrix","microwave","nightclub","nowadays","oxidize","oxygen","peekaboo","pixel","pneumonia","puppy","puzzling","queue","quizzes","quorum","rhythm","rickshaw","scratch","staff","strengths","stretch","subway","syndrome","thumbscrew","transcript","transplant","twelfth","unknown","unworthy","unzip","uptown","vodka","vortex","walkway","wave","wavy","whiskey","whizzing","wizard","wristwatch","xylophone","yachtsman", "youthful","yummy","zigzag" ,"zodiac" ,"zombie"]
word = random.choice(list_of_words).upper()
#print(word)
guessed = [] #to keep track of guessed words



#colors
white = (255,255,255)
BLACK =(0,0,0)
BLUE= (180, 219, 251)
PINK= (232, 90, 202)

#fonts
LETTER_FONTS= pygame.font.SysFont('comicsans', 40) #-> font name, size
WORD_FONTS = pygame.font.SysFont('comicsans', 60)
TITLE_FONTS = pygame.font.SysFont('comicsans', 70)



def draw():
  win.fill(BLUE) #setting the bg color with rgb values (0-255) 

  #draw title
  text = TITLE_FONTS.render("HANGMAN GAME", 1, BLACK)
  win.blit(text, (WIDTH/2 - text.get_width()/2, 20)) #here we set width of title at very center and height to somewhat top

  #draw word
  display_word= "" #this will keep on adding correct letters as we guess
  for i in word:
    if i in guessed: #if letter we click is guessed correctly, or present in the word we have to guess
      display_word += i + " "
    else:
      display_word += "_ "

  text = WORD_FONTS.render(display_word, 1, BLACK) #rendering diplay_word and displaying it on screen
  win.blit(text, (400, 200)) #drawing it on screen



  #draw buttons
  for i in letters:
    x, y, ltr, visible = i #suppose i= [4,5] so x= 4 and y= 5, unpacking data
    if visible:
      pygame.draw.circle(win, BLACK, (x, y) , radius, 3) #saying pygame to draw circle on win(window), color black, (x, y)-> center where draw the button, 3px-> radius for the circle 
      text = LETTER_FONTS.render(ltr,1,BLACK) #using font we just created, we render the text on screen, 
      #ltr-> text you want to render, BLACK --> color you want to render with
      win.blit(text, (x - text.get_width()/2, y - text.get_height()/2) ) #what we want to draw(here text), where
      #text.get_width()--> tells how wide is the surface 'text' that we created

  win.blit(images[hangman_status],(150,100)) #to draw image/some kind of surface, give image and location 
  pygame.display.update() #to reflect any kind of changes we have to update


#win/loose msg printing msg on screen
def display_message(message):
  pygame.time.delay(1000)
  win.fill(PINK)
  text = WORD_FONTS.render(message,1,BLACK)
  win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2)) #printing the won msg right at the center
  pygame.display.update()
  pygame.time.delay(3000) #will display the msg on screen for 3 secs


#setup game loop
FPS = 60 #max speed of game is 60 frames/sec
clock= pygame.time.Clock() #to make loop run at this speed 
run = True #var to control while loop

while run:
  clock.tick(FPS) # use 'clock' to make sure our loop runs in the FPS speed 

  draw()

  for i in pygame.event.get(): #any event(any click by user) that happens will be stored inside i
    if i.type == pygame.QUIT:
      run = False
    if i.type == pygame.MOUSEBUTTONDOWN: #getting position of mouse when pressed on screen
      m_x, m_y = pygame.mouse.get_pos() 
      for i in letters:
        x, y, ltr, visible = i 
        if visible: #checking for collision 
          dis= math.sqrt((x - m_x)**2 + (y- m_y)**2) 
          #adding distance from x and y, and take root, determining distance b/w tow points, we the get distance b/w mouse postion and side of button
          if dis< radius:
            i[3] = False # so it will set the last element of i i.e visible to false
            guessed.append(ltr)
            if ltr not in word:
              hangman_status += 1
            #print(ltr)
      #print(pos)  --> prints position of mouse


  draw() #when we win/loose the msg displays, but the last letter added is not shown on screen, so to show
  #we redraw each time we click on screen, then check


      
  #checking for winner
  won = True
  for i in word:#loops through all letters in word
    if i not in guessed:#if it not in guessed letter
      won = False
      break

  if won:
    display_message("Wohooo...!! You Won!")
    break

  if hangman_status == 6:
    display_message(f"Oopss..!! It was {word} You Lost!")
    break


pygame.quit()


