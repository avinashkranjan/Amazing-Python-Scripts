'''
Maze Generation Visualizer using Backtracking Algorithm

Python scripts for generating random solvable mazes using the depth-first search and recursive backtracking algorithms.
The code also implements a recursive backtracking pathfinding algorithm for solving the generated mazes. 

'''

import pygame
import random
pygame.init()


#Initialise screen and define Cell dimensions
width = 15
height = 15
screen = pygame.display.set_mode((735,735))
pygame.display.set_caption('Maze')


class Cell():
    #Cell class that defines each walkable Cell on the grid
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.visited = False
        self.walls = [True, True, True, True] # Left, Right, Up, Down


    def getChildren(self, grid: list) -> list:
        #Check if the Cell has any surrounding unvisited Cells that are walkable
        a = [(1, 0), (-1,0), (0, 1), (0, -1)] # Surrounding squares
        children = []

        for x, y in a:
            if self.x+x in [len(grid), -1] or self.y+y in [-1, len(grid)]: # Check if the neighbouring square is within range
                continue
        
            child = grid[self.y+y][self.x+x] # Get the child cell

            if child.visited: # Check if the child has already been visited
                continue

            children.append(child)
        return children


    def show(self, width: int, height: int, c: int, c2: int):
        #Draw a Cells existing walls
        x = self.x
        y = self.y

        if self.walls[0]:
            pygame.draw.rect(screen, (20,20,20), (width*x+c-width, height*y+c2, width, height))
        if self.walls[1]:
            pygame.draw.rect(screen, (20,20,20), (width*x+c+width, height*y+c2, width, height))
        if self.walls[2]:
            pygame.draw.rect(screen, (20,20,20), (width*x+c, height*y+c2-height, width, height))    
        if self.walls[3]:
            pygame.draw.rect(screen, (20,20,20), (width*x+c, height*y+c2+height, width, height))  
    

    def mark(self, width: int, height: int):
        #Mark the current cell
        x = self.x*width
        y = self.y*height
        pygame.draw.rect(screen, (134, 46, 222), (x*2+width,y*2+height, width, height))


def removeWalls(current: Cell, choice: Cell):
    #Removeing the wall between two Cells
    if choice.x > current.x:     
        current.walls[1] = False
        choice.walls[0] = False
    elif choice.x < current.x:
        current.walls[0] = False
        choice.walls[1] = False
    elif choice.y > current.y:
        current.walls[3] = False
        choice.walls[2] = False
    elif choice.y < current.y:
        current.walls[2] = False
        choice.walls[3] = False


def cornerFill():
    #Fill in the 'corners' of the grid (due to the walls being square)
    for x in range(len(grid)+1):
        for y in range(len(grid)+1):
            pygame.draw.rect(screen, (20,20,20), (x*width*2, y*height*2, width, height))


#Define the grid, set the current Cell and initialise the stack#
grid = [[Cell(x, y) for x in range(24)] for y in range(24)]
current = grid[0][0]
stack = []

screen.fill((210, 210 ,210))
#Main loop#
exit = False
while not exit:
    for x in range(len(grid)):
        for y in range(len(grid)):
            grid[x][y].show(width, height, (y+1)*width, (x+1)*height) # Draw walls
    
    cornerFill()

    current.visited = True
    current.mark(width, height) # Highlight the current Cell

    #If the current has neighours then choose a random one, mark it as visited, 
    #remove the walls between it and the current and set it as the new current
    children = current.getChildren(grid) 
    if children:
        choice = random.choice(children)
        choice.visited = True

        stack.append(current)

        removeWalls(current, choice)

        current = choice
    

    elif stack: # If the current has no neighbours go back to the last Cell on the stack
        current = stack.pop()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    
    pygame.display.update()
    screen.fill((210, 210 ,210))
pygame.quit()
quit()
