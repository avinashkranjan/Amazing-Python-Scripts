import pygame
import random
import copy
import sys
from pygame.math import Vector2 as vec


vec = pygame.math.Vector2

'''                              PLAYER DEFINING FUNCTIONS IN THE GAME                                                       '''

class Player:
    def __init__(self,app,pos):
        self.app = app
        self.start_pos = [pos.x, pos.y]
        self.grid_pos = pos
        self.pix_pos = self.get_pixel_pos()
        self.direction = vec(1,0)
        self.stored_direction = None
        self.stored_direction = None
        self.able_to_move = True
        self.current_score = 0
        self.lives = 3
        
    def update_player(self):
        if self.able_to_move:
            self.pix_pos += self.direction
        if self.time_to_move_player():
            if self.stored_direction != None:
                self.direction = self.stored_direction
            self.able_to_move = self.can_move()
        if self.on_coin():
            self.eat_coin()
    
    def draw_player(self):
        pygame.draw.circle(self.app.screen, PLAYER_COLOUR, (int(self.pix_pos.x), int(self.pix_pos.y)),(self.app.cell_width)//2-2)
        for x in range(self.lives):
            pygame.draw.circle(self.app.screen, PLAYER_COLOUR, (30 + 10*x, HEIGHT -15), 7)
                               
    def on_coin(self):
        if self.grid_pos in self.app.coins:
            if int(self.pix_pos.x == TOP_BOTTOM_BUFFER//2) % self.app.cell_width ==0:
                if self.direction == vec(1,0) or self.direction == vec(-1,0):
                    return True
            if int(self.pix_pos.y == TOP_BOTTOM_BUFFER//2) % self.app.cell_height ==0:
                if self.direction == vec(0,1) or self.direction == vec(0,-1):
                    return True
        return False
    
    
    def eat_coin(self):
            self.app.coins.remove(self.grid_pos)
            self.current_score +=1
    
    def move_player(self,direction):
        self.direction = direction
        
    def get_pixel_pos(self):
        return vec((self.grid_pos.x*self.app.cell_width)+ TOP_BOTTOM_BUFFER//2 + self.app.cell_width//2, (self.grid_pos.y*self.app.cell_height)+TOP_BOTTOM_BUFFER//2 + self.app.cell_height//2)
        print(self.grid_pos, self.pix_pos)
        
    def time_to_move_player(self):
        if int(self.pix_pos.x == TOP_BOTTOM_BUFFER//2) % self.app.cell_width ==0:
            if self.direction == vec(1,0) or self.direction == vec(-1,0) or self.direction == vec(0,0):
                return True
        if int(self.pix_pos.y == TOP_BOTTOM_BUFFER//2) % self.app.cell_height ==0:
            if self.direction == vec(0,1) or self.direction == vec(0,-1) or self.direction == vec(0,0):
                return True
            
    def can_move(self):
        for wall in self.app.walls:
            if vec(self.grid_pos + self.direction) == wall:
                return False
        return True
    
    
    
'''                                 DEFINING ENEMIES IN THE GAME                                                            '''

class Enemies:
    def __init__(self, app, pos, number):
        self.app = app
        self.grid_pos = pos
        self.start_pos = [pos.x, pos.y]
        self.pix_pos = self.get_pixel_pos()
        self.radius = int(self.app.cell_width//2.3)
        self.number= number
        self.colour = self.colour_set()
        self.directions = vec(0,0)
        self.personality = self.personality_set()
        self.target = None
        self.speed = self.speed_set()
        
    def update_enemies(self):
        if not self.target != self.grid_pos:
            self.target = self.target_set()
            self.pix_pos += self.directions
            if self.to_move_enemies():
                self.move()
        
        self.grid_pos[0] = (self.pix_pos[0]-TOP_BOTTOM_BUFFER +
                            self.app.cell_width//2)//self.app.cell_width+1
        self.grid_pos[1] = (self.pix_pos[1]-TOP_BOTTOM_BUFFER +
                            self.app.cell_height//2)//self.app.cell_height+1
    
    def draw_enemies(self):
        if self.number == 0:
            pygame.draw.circle(self.app.screen, (255,255,255), (int(self.pix_pos.x), int(self.pix_pos.y)), self.radius)
    
    def speed_set(self):
        if self.personality is ["speedy" , "scared"]:
            speed=2
        else:
            speed = 1
            
    def target_set(self):
        if self.personality == "speedy" or self.personality == "slow" :
            return vec(self.app.player.grid_pos[0], self.app.player.grid_pos[1])
        else:
            if self.app.player.grid_pos[0] > COLS//2 and self.app.player.grid_pos[1] > ROWS//2:
                return vec(1,1)
            elif self.app.player.grid_pos[0] > COLS//2 and self.app.player.grid_pos[1] < ROWS//2:
                return vec(1,ROWS - 2)
            elif self.app.player.grid_pos[0] < COLS//2 and self.app.player.grid_pos[1] > ROWS//2:
                return vec(COLS - 2,1)
            else :
                return vec(COLS-2,ROWS -2)
            
    def to_move_enemies(self):
        if int(self.pix_pos.x == TOP_BOTTOM_BUFFER//2) % self.app.cell_width ==0:
            if self.directions == vec(1,0) or self.directions == vec(-1,0) or self.directions == vec(0,0):
                return True
        if int(self.pix_pos.y == TOP_BOTTOM_BUFFER//2) % self.app.cell_height ==0:
            if self.directions == vec(0,1) or self.directions == vec(0,-1) or self.directions == vec(0,0):
                return True
        return False
    
    def move(self):
        if self.personality == "random":
            self.directions = self.get_path_enemies(self.target)
            
        if self.personality == "slow":
            self.directions = self.get_path_enemies(self.target)
            
        if self.personality == "speedy":
            self.directions = self.get_path_enemies(self.target)
            
        if self.personality == "scared":
            self.directions = self.get_path_enemies(self.target)
            
    def get_path_enemies(self,target):
        next_cell = self.find_next_cell_in_path(self.target)
        xdir = next_cell[0] - self.grid_pos[0]
        ydir = next_cell[1] - self.grid_pos[1]
        return vec(xdir, ydir)
    
    def find_next_cell_in_path(self, target):
        path = self.BFS([int(self.grid_pos.x), int(self.grid_pos.y)], [int(target[0]), int(target[1])])
        return path[1]
    
    def BFS(self, start, target):
        grid=[[0 for x in range(28)] for y in range(30)]
        for cell in self.app.walls:
            if cell.x < 28 and cell.y < 30:
                grid[int(cell.y)][int(cell.x)] = 1
        queue = [start]
        path = []
        while queue:
            current = queue[0]
            queue.remove(queue[0])
            visited.append(current)
            if current == target:
                break
            else:
                neighbours = [[0,-1],[1,0],[0,1],[1,0]]
                for neighbour in neighbours:
                    if neighbour[0] + current[0] >= 0 and neighbour[0] + current [0] < len(grid[0]):
                        if neighbour[1] + current[1] >= 0 and neighbour[1] + current [1] < len(grid):
                            next_cell = [neighbour[0] + current[0], neighbour[1] + current[1]]
                            if next_cell not in visited:
                                if grid[next_cell[1]][next_cell[0]] != 1:
                                    queue.append(next_cell)
                                    path.append([{"Current": current, "Next": next_cell}])
        shortest = [target]
        while target != start:
            for step in path:
                if stop["Next"] == target:
                    target = stop["Current"]
                    shortest.insert(0, stop["Current"])
        return shortest

        
    def get_random_directions(self):
        while True:
            number= random.randint(-2,2)
            if number == -2:
                x_dir, y_dir = 1, 0
            elif number == -1 :
                x_dir, y_dir = 0,1
            elif number == 0 :
                x_dir, y_dir = -1,0
            else:
                x_dir, y_dir = 0,-1
            next_pos = vec(self.grid_pos.x + x_dir, self.grid_pos.y + y_dir)
            if next_pos not in self.app.walls:
                break
            return vec(x_dir, y_dir)
    
    def get_pixel_pos(self):
        return vec((self.grid_pos.x*self.app.cell_width)+ TOP_BOTTOM_BUFFER//2 + self.app.cell_width//2, (self.grid_pos.y*self.app.cell_height)+TOP_BOTTOM_BUFFER//2 + self.app.cell_height//2)
        
    def colour_set(self):
        if self.number == 0:
            return (189, 29, 29)
        if self.number == 1:
            return (215, 159, 33)
        if self.number == 2:
            return (189, 29, 29)
        if self.number == 3:
            return (215, 159, 33)
        
    def personality_set(self):
        if self.number == 0:
            return "speedy"
        elif self.number == 1:
            return "slow"
        elif self.number == 2:
            return "random"
        else:
            return "scared"
    
    
'''                                THE ACTUAL CODE FOR THE GAME AND ALL REQUIRED SETTINGS                                   '''          

pygame.init()
class App:
    def __init__(self):
        self.screen= pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock= pygame.time.Clock()
        self.running= True
        self.state= 'start'
        self.cell_width = MAZE_WIDTH//COLS
        self.cell_height = MAZE_HEIGHT//ROWS
        self.walls = []
        self.coins = []
        self.enemies = []
        self.e_pos = []
        self.p_pos = None
        self.load()
        
        self.player = Player(self, vec(self.p_pos))
        self.make_enemies()
        
    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            elif self.state == 'playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            elif self.state == 'game over':
                self.game_over_events()
                self.game_over_update()
                self.game_over_draw()
            else:
                self.running = False
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()
        
    def draw_text(self, words, screen, pos, size, colour, font_name, centered=False):
        font = pygame.font.SysFont('arial black', 16, bold = True, italic = True)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if centered:
            pos[0] = pos[0]-text_size[0]//2
            pos[1] = pos[1]-text_size[1]//2
        screen.blit(text, pos)
        
    def load(self):
        self.background = pygame.image.load('maze.png')
        self.background = pygame.transform.scale(self.background, (MAZE_WIDTH,MAZE_HEIGHT))
        # File that contains walls
        with open("walls.txt",'r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == "1":
                        self.walls.append(vec(xidx, yidx))
                    elif char == "C":
                        self.coins.append(vec(xidx, yidx))
                    elif char == "P":
                        self.p_pos = [xidx,yidx]
                    elif char is ["2","3","4","5"]:
                        self.e_pos.append([xidx, yidx])
                    elif char == "B":
                        pygame.draw.rect(self.background, BLACK, (xidx*self.cell_width, yidx*self.cell_height, self.cell_width, self.cell_height))
                        
    def make_enemies(self):
        for enemy in enumerate(self.e_pos):
            self.enemies.append(Enemies(self, vec(pos), idx))
        
    def draw_grid(self):
        for x in range(WIDTH//self.cell_width):
            pygame.draw.line(self.background, GREY, (x*self.cell_width,0),(x*self.cell_width,HEIGHT))
        for x in range(HEIGHT//self.cell_height):
            pygame.draw.line(self.background, GREY, (0,x*self.cell_height),(WIDTH,x*self.cell_height))
    
    def reset_game(self):
        self.player.lives = 3
        self.player.current_score = 0
        self.player.grid_pos = vec(self.player.start_pos)
        self.player.pix_pos = self.player.get_pixel_pos()
        self.player.direction *= 0
        for enemy in self.enemy:
            enemy.grid_pos = vec(enemy.start_pos)
            enemy.pix_pos=enemy.get_pixel_pos()
        self.coins = []
        with open("walls.txt",'r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == "C":
                        self.coins.append(vec(xidx, yidx))
        
        self.state = 'playing'
        
    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running=False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state= 'playing'
                
    def start_update(self):
        pass
                
    def start_draw(self):
        self.screen.fill(BLACK)
        self.draw_text('PUSH SPACE BAR', self.screen, [WIDTH//2, HEIGHT//2-50], START_TEXT_SIZE, (170, 132, 58), START_FONT, centered=True)
        self.draw_text('1 PLAYER ONLY', self.screen, [WIDTH//2, HEIGHT//2+50], START_TEXT_SIZE, (44, 167, 198), START_FONT, centered=True)
        self.draw_text('HIGH SCORE', self.screen, [4, 0],START_TEXT_SIZE, (255, 255, 255), START_FONT)
        pygame.display.update()
        

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move_player(vec(-1,0))
                if event.key == pygame.K_RIGHT:
                    self.player.move_player(vec(1,0))
                if event.key == pygame.K_UP:
                    self.player.move_player(vec(0,1))
                if event.key == pygame.K_DOWN:
                    self.player.move_player(vec(0,-1))
                
    def playing_update(self):
        self.player.update_player()
        for enemy in self.enemies:
            enemy.update_enemies()
            
        for enemies in self.enemies:
            if enemy.grid_pos == self.player.grid_pos:
                self.life_removed()
                
    def playing_draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background, (TOP_BOTTOM_BUFFER//2, TOP_BOTTOM_BUFFER//2))
        self.draw_coins()
        self.draw_text('Current Score: {}'.format(self.player.current_score), self.screen, [60,0],18, WHITE, START_FONT, centered=False)
        self.draw_text('High Score: 0', self.screen, [WIDTH//2 + 60,0],18, WHITE, START_FONT, centered=False)
        self.player.draw_player()
        for enemy in self.enemies:
            enemy.draw()
        pygame.display.update()
        
    def life_removed(self):
        self.player.lives -=1
        if self.player.lives == 0:
            self.state = "GAME OVER"
        else:
            self.player.grid_pos = vec(self.player.start_pos)
            self.player.pix_pos = self.player.get_pix_pos()
            self.player.direction *= 0
            
            for enemy in self.enemies:
                enemy.grid_pos = vec(enemy.start_pos)
                enemy.pix_pos = enemy.get_pixel_pos()
                self.directions *=0
            
                             
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

    def game_over_update(self):
        pass

    def game_over_draw(self):
        self.screen.fill(BLACK)
        quit_text = "Press the escape button to QUIT"
        again_text = "Press SPACE bar to PLAY AGAIN"
        self.draw_text("GAME OVER", self.screen, [WIDTH//2, 100],  52, RED, "arial", centered=True)
        self.draw_text(again_text, self.screen, [
                       WIDTH//2, HEIGHT//2],  36, (190, 190, 190), "arial", centered=True)
        self.draw_text(quit_text, self.screen, [
                       WIDTH//2, HEIGHT//1.5],  36, (190, 190, 190), "arial", centered=True)
        pygame.display.update()

      
    
    def game_over_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.reset_game()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False

    def game_over_update(self):
        pass

    def game_over_draw(self):
        self.screen.fill(BLACK)
        quit_text = "Press ESC to QUIT"
        again_text = "Press SPACE BAR to PLAY AGAIN"
        self.draw_text("GAME OVER", self.screen, [WIDTH//2, 100],  52, RED, "arial", centered=True)
        self.draw_text(again_text, self.screen, [
                       WIDTH//2, HEIGHT//2],  36, (190, 190, 190), "arial", centered=True)
        self.draw_text(quit_text, self.screen, [
                       WIDTH//2, HEIGHT//1.5],  36, (190, 190, 190), "arial", centered=True)
        pygame.display.update()
        
    

#screen
WIDTH= 560
HEIGHT=620
FPS=60
TOP_BOTTOM_BUFFER = 50
MAZE_WIDTH, MAZE_HEIGHT = WIDTH-TOP_BOTTOM_BUFFER, HEIGHT-TOP_BOTTOM_BUFFER
ROWS = 28
COLS = 30


#colour
BLACK = (0,0,0)
RED = (208,22,22)
GREY = (107,107,107)
WHITE = (255,255,255)
PLAYER_COLOUR = (190,194,15)


#font
START_TEXT_SIZE= 24
START_FONT= 'arial black'


if __name__ == '__main__':
    app = App()
    app.run()