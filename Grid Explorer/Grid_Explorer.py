import random


def create_grid(size):
    return [[' ' for _ in range(size)] for _ in range(size)]


def place_treasure(grid, size):
    row = random.randint(0, size - 1)
    col = random.randint(0, size - 1)
    grid[row][col] = 'T'
    return row, col


def display_grid(grid):
    size = len(grid)
    for row in grid:
        print(' | '.join(cell.center(3) for cell in row))
        print('-' * (size * 5 - 1))


def move_explorer(grid, row, col, direction):
    size = len(grid)
    if direction == 'up' and row > 0:
        row -= 1
    elif direction == 'down' and row < size - 1:
        row += 1
    elif direction == 'left' and col > 0:
        col -= 1
    elif direction == 'right' and col < size - 1:
        col += 1
    return row, col


def grid_explorer(size):
    grid = create_grid(size)
    explorer_row, explorer_col = random.randint(
        0, size - 1), random.randint(0, size - 1)
    treasure_row, treasure_col = place_treasure(grid, size)

    print("Welcome to Grid Explorer!")
    print("Find the treasure (T) on the grid by navigating in the up, down, left, or right direction.")
    print("Enter 'quit' to exit the game.\n")

    while True:
        display_grid(grid)
        print(f"Explorer position: ({explorer_row}, {explorer_col})")
        move = input("Enter your move (up/down/left/right): ").lower()

        if move == 'quit':
            print("Exiting the game...")
            break

        if move not in ['up', 'down', 'left', 'right']:
            print("Invalid move. Try again.")
            continue

        new_explorer_row, new_explorer_col = move_explorer(
            grid, explorer_row, explorer_col, move)

        if grid[new_explorer_row][new_explorer_col] == 'T':
            display_grid(grid)
            print("Congratulations! You found the treasure!")
            break
        else:
            grid[explorer_row][explorer_col] = ' '
            explorer_row, explorer_col = new_explorer_row, new_explorer_col
            grid[explorer_row][explorer_col] = 'E'


if __name__ == "__main__":
    grid_explorer(5)
