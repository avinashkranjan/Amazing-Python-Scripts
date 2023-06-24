from tkinter import *
from tkinter import font

# Constants
TOL = 8
CELLSIZE = 40
OFFSET = 10
CIRCLERAD = 2
DOTOFFSET = OFFSET + CIRCLERAD
GAME_H = 400
GAME_W = 400

# Player Class
class Player(object):
    def __init__(self, name, color="black"):
        self.score = 0
        self.str = StringVar()
        self.name = name
        self.color = color

    def update(self):
        self.str.set(self.name + ": %d" % self.score)


# Main Frame Class
class MyFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # Fonts
        self.GO_font = font.Font(self, name="GOFont", family="Comic Sans MS", weight="bold", size=36)

        # Canvas
        self.canvas = Canvas(self, height=GAME_H, width=GAME_W, bg="gray")
        self.canvas.bind("<Button-1>", lambda e: self.click(e))
        self.canvas.grid(row=0, column=0)

        # Dots
        self.dots = [[self.canvas.create_oval(CELLSIZE*i+OFFSET, CELLSIZE*j+OFFSET, CELLSIZE*i+OFFSET+2*CIRCLERAD, CELLSIZE*j+OFFSET+2*CIRCLERAD, fill="black") for j in range(10)] for i in range(10)]
        self.lines = []

        # Info Frame
        self.infoframe = Frame(self, bg="gray")
        self.players = [Player("Player A", "blue"), Player("Player B", "green")]
        self.infoframe.players = [Label(self.infoframe, textvariable=i.str, bg="white", font="Arial 20 bold") for i in self.players]
        for i in self.infoframe.players:
            i.grid()
        self.turn = self.players[0]
        self.update_players()
        self.infoframe.grid(row=0, column=1, sticky=N)

        # Reset Game Button
        self.reset_button = Button(self, text="Reset Game", command=self.reset_game)
        self.reset_button.grid(row=1, column=0)

        self.grid()

    def update_players(self):
        for i in self.players:
            i.update()

    def click(self, event):
        x, y = event.x, event.y
        orient = self.isclose(x, y)

        if orient:
            if self.line_exists(x, y, orient):
                return
            l = self.create_line(x, y, orient)
            score = self.new_box_made(l)
            if score:
                self.turn.score += score
                self.turn.update()
                self.check_game_over()
            else:
                index = self.players.index(self.turn)
                self.turn = self.players[1-index]
            self.lines.append(l)

    def create_line(self, x, y, orient):
        startx = CELLSIZE * ((x-OFFSET)//CELLSIZE) + DOTOFFSET
        starty = CELLSIZE * ((y-OFFSET)//CELLSIZE) + DOTOFFSET
        tmpx = (x-OFFSET)//CELLSIZE
        tmpy = (y-OFFSET)//CELLSIZE
        
        if orient == HORIZONTAL:
            endx = startx + CELLSIZE
            endy = starty
        else:
            endx = startx
            endy = starty + CELLSIZE

        return self.canvas.create_line(startx, starty, endx, endy)

    def new_box_made(self, line):
        score = 0
        x0, y0, x1, y1 = self.canvas.coords(line)
        if x0 == x1:  # vertical line
            midx = x0
            midy = (y0+y1)/2
            pre = (x0 - CELLSIZE/2, midy)
            post = (x0 + CELLSIZE/2, midy)
        elif y0 == y1:  # horizontal line
            midx = (x0 + x1)/2
            midy = y0
            pre = (midx, y0 - CELLSIZE/2)
            post = (midx, y0 + CELLSIZE/2)
        
        if len(self.find_lines(pre)) == 3:  
            self.fill_in(pre)               
            score += 1
        if len(self.find_lines(post)) == 3:
            self.fill_in(post)
            score += 1
        return score

    def find_lines(self, coords):
        x, y = coords
        if x < 0 or x > GAME_W:
            return []
        if y < 0 or y > GAME_W:
            return []

        lines = [x for x in self.canvas.find_enclosed(x-CELLSIZE, y-CELLSIZE, x+CELLSIZE, y+CELLSIZE) if x in self.lines]
        return lines

    def fill_in(self, coords):
        x, y = coords
        self.canvas.create_text(x, y, text=self.turn.name, fill=self.turn.color, font="Arial 5 bold")

    def isclose(self, x, y):
        x -= OFFSET
        y -= OFFSET
        dx = x - (x//CELLSIZE)*CELLSIZE
        dy = y - (y//CELLSIZE)*CELLSIZE

        if abs(dx) < TOL:
            if abs(dy) < TOL:
                return None  
            else:
                return VERTICAL
        elif abs(dy) < TOL:
            return HORIZONTAL
        else:
            return None

    def line_exists(self, x, y, orient):
        id_ = self.canvas.find_closest(x, y, halo=TOL)[0]
        if id_ in self.lines:
            return True
        else:
            return False

    def check_game_over(self):
        total = sum([x.score for x in self.players])
        if total == 81:
            self.canvas.create_text(GAME_W/2, GAME_H/2, text="GAME OVER", font=self.GO_font, fill="#888", justify=CENTER)

    def reset_game(self):
        self.canvas.delete("all")
        self.lines = []
        for i in range(10):
            for j in range(10):
                self.dots[i][j] = self.canvas.create_oval(CELLSIZE*i+OFFSET, CELLSIZE*j+OFFSET, CELLSIZE*i+OFFSET+2*CIRCLERAD, CELLSIZE*j+OFFSET+2*CIRCLERAD, fill="black")
        for player in self.players:
            player.score = 0
            player.update()
        self.turn = self.players[0]


# Main Tkinter Window
mainw = Tk()
mainw.title("Dot Connect")
mainw.config(bg="white")
mainw.f = MyFrame(mainw)
mainw.mainloop()
