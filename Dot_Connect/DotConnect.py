from tkinter import *
from tkinter import font

# Constants
TOLERANCE = 8
CELL_SIZE = 40
OFFSET = 10
CIRCLE_RADIUS = 5
DOT_OFFSET = OFFSET + CIRCLE_RADIUS
GAME_HEIGHT = 400
GAME_WIDTH = 400

# Player Class


class Player:
    def __init__(self, name, color="#00BFFF"):  # Blue color
        self.score = 0
        self.text_var = StringVar()
        self.name = name
        self.color = color

    def update(self):
        self.text_var.set(f"{self.name}: {self.score}")


# Main Frame Class
class DotConnectFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # Fonts
        self.title_font = font.Font(
            self, name="TitleFont", family="Arial", weight="bold", size=36)

        # Info Frame
        self.info_frame = Frame(self, bg="#333333")  # Dark gray background
        self.players = [Player("Player A", "#00BFFF"), Player(
            "Player B", "#00FF00")]  # Blue and Green colors
        self.info_frame.players = [Label(self.info_frame, textvariable=i.text_var, bg="#FFFFFF", fg="#333333",
                                         font="Arial 20 bold") for i in self.players]  # White text on dark gray background
        for i in self.info_frame.players:
            i.grid()
        self.info_frame.grid(row=0, column=0, columnspan=2, pady=10)

        # Canvas
        # Dark gray background
        self.canvas = Canvas(self, height=GAME_HEIGHT,
                             width=GAME_WIDTH, bg="#333333")
        self.canvas.bind("<Button-1>", lambda e: self.click(e))
        self.canvas.grid(row=1, column=0, padx=10)

        # Dots
        self.dots = [[self.canvas.create_oval(CELL_SIZE*i+OFFSET, CELL_SIZE*j+OFFSET, CELL_SIZE*i+OFFSET+2*CIRCLE_RADIUS,
                                              CELL_SIZE*j+OFFSET+2*CIRCLE_RADIUS, fill="#000000") for j in range(10)] for i in range(10)]  # Black dots
        self.lines = []

        # Reset Game Button
        self.reset_button = Button(self, text="Reset Game", command=self.reset_game,
                                   font="Arial 14 bold", bg="#FF0000", fg="#000000")  # Red button with white text
        self.reset_button.grid(row=2, column=0, pady=10)

        self.turn = self.players[0]
        self.update_players()

        self.grid()

    def update_players(self):
        for player in self.players:
            player.update()

    def click(self, event):
        x, y = event.x, event.y
        orientation = self.check_proximity(x, y)

        if orientation:
            if self.line_exists(x, y, orientation):
                return
            line = self.create_line(x, y, orientation)
            score = self.update_score(line)
            if score:
                self.turn.score += score
                self.turn.update()
                self.check_game_over()
            else:
                index = self.players.index(self.turn)
                self.turn = self.players[1 - index]
            self.lines.append(line)

    def create_line(self, x, y, orientation):
        start_x = CELL_SIZE * ((x - OFFSET) // CELL_SIZE) + DOT_OFFSET
        start_y = CELL_SIZE * ((y - OFFSET) // CELL_SIZE) + DOT_OFFSET
        tmp_x = (x - OFFSET) // CELL_SIZE
        tmp_y = (y - OFFSET) // CELL_SIZE

        if orientation == "horizontal":
            end_x = start_x + CELL_SIZE
            end_y = start_y
        else:
            end_x = start_x
            end_y = start_y + CELL_SIZE

        return self.canvas.create_line(start_x, start_y, end_x, end_y, width=2, fill=self.turn.color)

    def update_score(self, line):
        score = 0
        x0, y0, x1, y1 = self.canvas.coords(line)
        if x0 == x1:  # Vertical line
            mid_x = x0
            mid_y = (y0 + y1) / 2
            pre = (x0 - CELL_SIZE / 2, mid_y)
            post = (x0 + CELL_SIZE / 2, mid_y)
        elif y0 == y1:  # Horizontal line
            mid_x = (x0 + x1) / 2
            mid_y = y0
            pre = (mid_x, y0 - CELL_SIZE / 2)
            post = (mid_x, y0 + CELL_SIZE / 2)

        if len(self.find_lines(pre)) == 3:
            self.fill_box(pre)
            score += 1
        if len(self.find_lines(post)) == 3:
            self.fill_box(post)
            score += 1
        return score

    def find_lines(self, coords):
        x, y = coords
        if x < 0 or x > GAME_WIDTH:
            return []
        if y < 0 or y > GAME_WIDTH:
            return []

        lines = [x for x in self.canvas.find_enclosed(
            x - CELL_SIZE, y - CELL_SIZE, x + CELL_SIZE, y + CELL_SIZE) if x in self.lines]
        return lines

    def fill_box(self, coords):
        x, y = coords
        self.canvas.create_text(x, y, text=self.turn.name,
                                fill=self.turn.color, font="Arial 5 bold")

    def check_proximity(self, x, y):
        x -= OFFSET
        y -= OFFSET
        dx = x - (x // CELL_SIZE) * CELL_SIZE
        dy = y - (y // CELL_SIZE) * CELL_SIZE

        if abs(dx) < TOLERANCE:
            if abs(dy) < TOLERANCE:
                return None
            else:
                return "vertical"
        elif abs(dy) < TOLERANCE:
            return "horizontal"
        else:
            return None

    def line_exists(self, x, y, orientation):
        id_ = self.canvas.find_closest(x, y, halo=TOLERANCE)[0]
        if id_ in self.lines:
            return True
        else:
            return False

    def check_game_over(self):
        total = sum([player.score for player in self.players])
        if total == 81:
            self.canvas.create_text(GAME_WIDTH / 2, GAME_HEIGHT / 2, text="GAME OVER", font=self.title_font, fill="#888888",
                                    justify=CENTER)

    def reset_game(self):
        self.canvas.delete("all")
        self.lines = []
        for i in range(10):
            for j in range(10):
                self.dots[i][j] = self.canvas.create_oval(CELL_SIZE * i + OFFSET, CELL_SIZE * j + OFFSET, CELL_SIZE * i + OFFSET + 2 * CIRCLE_RADIUS,
                                                          CELL_SIZE * j + OFFSET + 2 * CIRCLE_RADIUS, fill="#000000")
        for player in self.players:
            player.score = 0
            player.update()
        self.turn = self.players[0]


# Main Tkinter Window
main_window = Tk()
main_window.title("Dot Connect")
main_window.config(bg="#000000")
main_window.frame = DotConnectFrame(main_window)
main_window.mainloop()
