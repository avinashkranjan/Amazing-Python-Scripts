import pygame
import random
import sys
import copy

vec = pygame.math.Vector2
'''                                        DEFINING PLAYER FUNCTIONS                                                    '''      
class Player:
    def __init__(self, app, pos):
        self.app = app
        self.starting_pos = [pos.x, pos.y]
        self.grid_pos = pos
        self.pixel_pos = self.get_pixel_pos()
        self.directions = vec(1, 0)
        self.stored_directions = None
        self.moveable = True
        self.current_score = 0
        self.lives = 3

    def update_player(self):
        if self.moveable:
            self.pixel_pos += self.directions
        if self.movement_time():
            if self.stored_directions != None:
                self.directions = self.stored_directions
            self.moveable = self.can_move()
        
        self.grid_pos[0] = (self.pixel_pos[0]-TOP_BOTTOM_BUFFER +self.app.cell_width//2)//self.app.cell_width+1
        self.grid_pos[1] = (self.pixel_pos[1]-TOP_BOTTOM_BUFFER +self.app.cell_height//2)//self.app.cell_height+1
        if self.when_on_coin():
            self.eat_coin()

    def draw_player(self):
        pygame.draw.circle(self.app.screen, PLAYER_COLOUR, (int(self.pixel_pos.x),int(self.pixel_pos.y)), self.app.cell_width//2-2)

        
        for x in range(self.lives):
            pygame.draw.circle(self.app.screen, PLAYER_COLOUR, (30 + 20*x, HEIGHT - 15), 7)


    def when_on_coin(self):
        if self.grid_pos in self.app.coins:
            if int(self.pixel_pos.x+TOP_BOTTOM_BUFFER//2) % self.app.cell_width == 0:
                if self.directions == vec(1, 0) or self.directions == vec(-1, 0):
                    return True
            if int(self.pixel_pos.y+TOP_BOTTOM_BUFFER//2) % self.app.cell_height == 0:
                if self.directions == vec(0, 1) or self.directions == vec(0, -1):
                    return True
        return False

    def eat_coin(self):
        self.app.coins.remove(self.grid_pos)
        self.current_score += 1

    def move_player(self, direction):
        self.stored_directions = directions

    def get_pixel_pos(self):
        return vec((self.grid_pos[0]*self.app.cell_width)+TOP_BOTTOM_BUFFER//2+self.app.cell_width//2,(self.grid_pos[1]*self.app.cell_height) + TOP_BOTTOM_BUFFER//2+self.app.cell_height//2)

        print(self.grid_pos, self.pixel_pos)

    def movement_time(self):
        if int(self.pixel_pos.x+TOP_BOTTOM_BUFFER//2) % self.app.cell_width == 0:
            if self.directions == vec(1, 0) or self.directions == vec(-1, 0) or self.directions == vec(0, 0):
                return True
        if int(self.pixel_pos.y+TOP_BOTTOM_BUFFER//2) % self.app.cell_height == 0:
            if self.directions == vec(0, 1) or self.directions == vec(0, -1) or self.directions == vec(0, 0):
                return True

    def can_move(self):
        for walls in self.app.walls:
            if vec(self.grid_pos+self.directions) == walls:
                return False
        return True
    
'''                                          DEFINING ENEMY FUNCTIONS                                                  '''  
class Enemies:
    def __init__(self, app, pos, number):
        self.app = app
        self.grid_pos = pos
        self.starting_pos = [pos.x, pos.y]
        self.pixel_pos = self.get_pixel_pos()
        self.radius = int(self.app.cell_width//2.3)
        self.numbers = random.randint(0,4)
        self.color = self.set_color()
        self.directions = vec(0, 0)
        self.personality = self.personality_set()
        self.target = None
        self.speed = self.set_speed()

    def update_enemies(self):
        self.target = self.set_target()
        if self.target != self.grid_pos:
            self.pixel_pos += self.directions * self.speed
            if self.movement_time():
                self.move_enemies()

        
        self.grid_pos[0] = (self.pixel_pos[0]-TOP_BOTTOM_BUFFER + self.app.cell_width//2)//self.app.cell_width+1
        self.grid_pos[1] = (self.pixel_pos[1]-TOP_BOTTOM_BUFFER + self.app.cell_height//2)//self.app.cell_height+1

    def draw_enemies(self):
        pygame.draw.circle(self.app.screen, self.color,
                           (int(self.pixel_pos.x), int(self.pixel_pos.y)), self.radius)

    def set_speed(self):
        if self.personality in ["speedy", "scared"]:
            speed = 2
        else:
            speed = 1
        return speed

    def set_target(self):
        if self.personality == "speedy" or self.personality == "slow":
            return self.app.player.grid_pos
        else:
            if self.app.player.grid_pos[0] > COLS//2 and self.app.player.grid_pos[1] > ROWS//2:
                return vec(1, 1)
            if self.app.player.grid_pos[0] > COLS//2 and self.app.player.grid_pos[1] < ROWS//2:
                return vec(1, ROWS-2)
            if self.app.player.grid_pos[0] < COLS//2 and self.app.player.grid_pos[1] > ROWS//2:
                return vec(COLS-2, 1)
            else:
                return vec(COLS-2, ROWS-2)

    def movement_time(self):
        if int(self.pixel_pos.x+TOP_BOTTOM_BUFFER//2) % self.app.cell_width == 0:
            if self.directions == vec(1, 0) or self.directions == vec(-1, 0) or self.directions == vec(0, 0):
                return True
        if int(self.pixel_pos.y+TOP_BOTTOM_BUFFER//2) % self.app.cell_height == 0:
            if self.directions == vec(0, 1) or self.directions == vec(0, -1) or self.directions == vec(0, 0):
                return True
        return False

    def move_enemies(self):
        if self.personality == "random":
            self.directions = self.get_random_directions()
        if self.personality == "slow":
            self.directions = self.get_path_direction(self.target)
        if self.personality == "speedy":
            self.directions = self.get_path_direction(self.target)
        if self.personality == "scared":
            self.directions = self.get_path_direction(self.target)

    def get_path_direction(self, target):
        next_cell = self.find_next_cell_in_path(target)
        xdir = next_cell[0] - self.grid_pos[0]
        ydir = next_cell[1] - self.grid_pos[1]
        return vec(xdir, ydir)

    def find_next_cell_in_path(self, target):
        path = self.BFS([int(self.grid_pos.x), int(self.grid_pos.y)], [int(target[0]), int(target[1])])
        return path[1]

    def BFS(self, start, target):
        grid = [[0 for x in range(28)] for x in range(30)]
        for cell in self.app.walls:
            if cell.x < 28 and cell.y < 30:
                grid[int(cell.y)][int(cell.x)] = 1
        queue = [start]
        path = []
        visited = []
        while queue:
            current = queue[0]
            queue.remove(queue[0])
            visited.append(current)
            if current == target:
                break
            else:
                neighbours = [[0, -1], [1, 0], [0, 1], [-1, 0]]
                for neighbour in neighbours:
                    if neighbour[0]+current[0] >= 0 and neighbour[0] + current[0] < len(grid[0]):
                        if neighbour[1]+current[1] >= 0 and neighbour[1] + current[1] < len(grid):
                            next_cell = [neighbour[0] + current[0], neighbour[1] + current[1]]
                            if next_cell not in visited:
                                if grid[next_cell[1]][next_cell[0]] != 1:
                                    queue.append(next_cell)
                                    path.append({"Current": current, "Next": next_cell})
        shortest = [target]
        while target != start:
            for step in path:
                if step["Next"] == target:
                    target = step["Current"]
                    shortest.insert(0, step["Current"])
        return shortest

    def get_random_directions(self):
        while True:
            numbers = random.randint(-2, 1)
            if numbers == -2:
                x_dir, y_dir = 1, 0
            elif numbers == -1:
                x_dir, y_dir = 0, 1
            elif numbers == 0:
                x_dir, y_dir = -1, 0
            else:
                x_dir, y_dir = 0, -1
            next_pos = vec(self.grid_pos.x + x_dir, self.grid_pos.y + y_dir)
            if next_pos not in self.app.walls:
                break
        return vec(x_dir, y_dir)

    def get_pixel_pos(self):
        return vec((self.grid_pos.x*self.app.cell_width)+TOP_BOTTOM_BUFFER//2+self.app.cell_width//2,(self.grid_pos.y*self.app.cell_height)+TOP_BOTTOM_BUFFER//2 +self.app.cell_height//2)

    def set_color(self):
        if self.numbers == 0:
            return (189, 29, 29)
        if self.numbers == 1:
            return (215, 159, 33)
        if self.numbers == 2:
            return (189, 29, 29)
        if self.numbers == 3:
            return (215, 159, 33)

    def personality_set(self):
        if self.numbers == 0:
            return "speedy"
        elif self.numbers == 1:
            return "slow"
        elif self.numbers == 2:
            return "random"
        else:
            return "scared"

'''                          DEFINING THE APP, WITH ALL ENEMY AND PLAYER SETTINGS                                       '''

pygame.init()
class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'
        self.cell_width = MAZE_WIDTH//COLS
        self.cell_height = MAZE_HEIGHT//ROWS
        self.walls = []
        self.coins = []
        self.enemies = []
        self.e_pos = []
        self.p_pos = None
        self.load()
        self.player = Player(self, vec(self.p_pos))
        self.making_enemies()

    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_draw()
            elif self.state == 'playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            elif self.state == 'game over':
                self.game_over_events()
                self.game_over_draw()
            else:
                self.running = False
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()


    def draw_text(self, words, screen, pos, size, colour, font_name, centered=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if centered:
            pos[0] = pos[0]-text_size[0]//2
            pos[1] = pos[1]-text_size[1]//2
        screen.blit(text, pos)

    def load(self):
        self.background = pygame.image.load('./Pacman-Game/maze.png')
        self.background = pygame.transform.scale(self.background, (MAZE_WIDTH, MAZE_HEIGHT))

       
        with open("./Pacman-Game/walls.txt",'r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == "1":
                        self.walls.append(vec(xidx, yidx))
                    elif char == "C":
                        self.coins.append(vec(xidx, yidx))
                    elif char == "P":
                        self.p_pos = [xidx, yidx]
                    elif char in ["2", "3", "4", "5"]:
                        self.e_pos.append([xidx, yidx])
                    elif char == "B":
                        pygame.draw.rect(self.background, BLACK, (xidx*self.cell_width, yidx*self.cell_height,self.cell_width, self.cell_height))

    def making_enemies(self):
        for idx, pos in enumerate(self.e_pos):
            self.enemies.append(Enemies(self, vec(pos), idx))

    def draw_grid(self):
        for x in range(WIDTH//self.cell_width):
            pygame.draw.line(self.background, GREY, (x*self.cell_width, 0),(x*self.cell_width, HEIGHT))
        for x in range(HEIGHT//self.cell_height):
            pygame.draw.line(self.background, GREY, (0, x*self.cell_height),(WIDTH, x*self.cell_height))

    def reset(self):
        self.player.lives = 3
        self.player.current_score = 0
        self.player.grid_pos = vec(self.player.starting_pos)
        self.player.pixel_pos = self.player.get_pixel_pos()
        self.player.directions *= 0
        for enemy in self.enemies:
            enemy.grid_pos = vec(enemy.starting_pos)
            enemy.pixel_pos = enemy.get_pixel_pos()
            enemy.directions *= 0

        self.coins = []
        with open("./Pacman-Game/walls.txt",'r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == 'C':
                        self.coins.append(vec(xidx, yidx))
        self.state = "playing"


    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'
                

    def start_draw(self):
        self.screen.fill(BLACK)
        self.draw_text('PUSH SPACE BAR', self.screen, [WIDTH//2, HEIGHT//2-50], START_TEXT_SIZE, (170, 132, 58), START_FONT, centered=True)
        self.draw_text('1 PLAYER ONLY', self.screen, [WIDTH//2, HEIGHT//2+50], START_TEXT_SIZE, (44, 167, 198), START_FONT, centered=True)
        self.draw_text('HIGH SCORE', self.screen, [4, 0],START_TEXT_SIZE, (255, 255, 255), START_FONT)
        pygame.display.update()


    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move_player(vec(-1, 0))
                if event.key == pygame.K_RIGHT:
                    self.player.move_player(vec(1, 0))
                if event.key == pygame.K_UP:
                    self.player.move_player(vec(0, -1))
                if event.key == pygame.K_DOWN:
                    self.player.move_player(vec(0, 1))

    def playing_update(self):
        self.player.update_player()
        for enemy in self.enemies:
            enemy.update_enemies()

        for enemy in self.enemies:
            if enemy.grid_pos == self.player.grid_pos:
                self.remove_life()

    def playing_draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background, (TOP_BOTTOM_BUFFER//2, TOP_BOTTOM_BUFFER//2))
        self.draw_coins()
        self.draw_text('CURRENT SCORE: {}'.format(self.player.current_score),self.screen, [60, 0], 18, WHITE, START_FONT)
        self.draw_text('HIGH SCORE: 0', self.screen, [WIDTH//2+60, 0], 18, WHITE, START_FONT)
        self.player.draw_player()
        for enemy in self.enemies:
            enemy.draw_enemies()
        pygame.display.update()

    def remove_life(self):
        self.player.lives -= 1
        if self.player.lives == 0:
            self.state = "game over"
        else:
            self.player.grid_pos = vec(self.player.starting_pos)
            self.player.pixel_pos = self.player.get_pixel_pos()
            self.player.directions *= 0
            for enemy in self.enemies:
                enemy.grid_pos = vec(enemy.starting_pos)
                enemy.pixel_pos = enemy.get_pixel_pos()
                enemy.directions *= 0

    def draw_coins(self):
        for coin in self.coins:
            pygame.draw.circle(self.screen, (124, 123, 7),(int(coin.x*self.cell_width)+self.cell_width//2+TOP_BOTTOM_BUFFER//2,int(coin.y*self.cell_height)+self.cell_height//2+TOP_BOTTOM_BUFFER//2), 5)


    def game_over_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.reset()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False

    def game_over_draw(self):
        self.screen.fill(BLACK)
        quit_text = "Press the escape button to QUIT"
        again_text = "Press SPACE bar to PLAY AGAIN"
        self.draw_text("GAME OVER", self.screen, [WIDTH//2, 100],  52, RED, "arial", centered=True)
        self.draw_text(again_text, self.screen, [WIDTH//2, HEIGHT//2],  36, (190, 190, 190), "arial", centered=True)
        self.draw_text(quit_text, self.screen, [WIDTH//2, HEIGHT//1.5],  36, (190, 190, 190), "arial", centered=True)
        pygame.display.update()

#screen settings
WIDTH, HEIGHT = 610, 670
FPS = 60
TOP_BOTTOM_BUFFER = 50
MAZE_WIDTH, MAZE_HEIGHT = WIDTH-TOP_BOTTOM_BUFFER, HEIGHT-TOP_BOTTOM_BUFFER

ROWS = 30
COLS = 28

# colour settings
BLACK = (0, 0, 0)
RED = (208, 22, 22)
GREY = (107, 107, 107)
WHITE = (255, 255, 255)
PLAYER_COLOUR = (190, 194, 15)

# font settings
START_TEXT_SIZE = 16
START_FONT = 'arial black'