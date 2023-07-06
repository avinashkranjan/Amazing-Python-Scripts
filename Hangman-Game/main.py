import pygame
import math
import random

# setup display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

# button variables
radius = 20
gap = 15
letters = []
startx = round((WIDTH - (radius * 2 + gap) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + gap * 2 + ((radius * 2 + gap) * (i % 13))
    y = starty + ((i//13) * (gap + radius * 2))
    letters.append([x, y, chr(A+i), True])

# load images
images = []
for i in range(7):
    img = pygame.image.load("./Hangman-Game/hangman" + str(i) + ".png")
    images.append(img)

# game variables
hangman_status = 0
with open("./Hangman-Game/words.txt", 'r') as f:
    content = f.read()
list_of_words = content.split(",")
word = random.choice(list_of_words).upper()
guessed = []

# colors
white = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (180, 219, 251)
PINK = (232, 90, 202)

# fonts
LETTER_FONTS = pygame.font.SysFont('comicsans', 40)
WORD_FONTS = pygame.font.SysFont('comicsans', 60)
TITLE_FONTS = pygame.font.SysFont('comicsans', 70)


def draw():
    win.fill(BLUE)
    # draw title
    text = TITLE_FONTS.render("HANGMAN GAME", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))
    # draw word
    display_word = ""
    for i in word:
        if i in guessed:
            display_word += i + " "
        else:
            display_word += "_ "

    text = WORD_FONTS.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))
    # draw buttons
    for i in letters:
        x, y, ltr, visible = i
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), radius, 3)
            text = LETTER_FONTS.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()

# win/loose msg printing msg on screen


def display_message(message):
    pygame.time.delay(1000)
    win.fill(PINK)
    text = WORD_FONTS.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width() /
             2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)


# setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(FPS)
    draw()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        if i.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for i in letters:
                x, y, ltr, visible = i
                if visible:
                    dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                    if dis < radius:
                        i[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1
    draw()
    # checking for winner
    won = True
    for i in word:
        if i not in guessed:
            won = False
            break
    if won:
        display_message("Wohooo...!! You Won!")
        break
    if hangman_status == 6:
        display_message(f"Oopss..!! It was {word} You Lost!")
        break
pygame.quit()
