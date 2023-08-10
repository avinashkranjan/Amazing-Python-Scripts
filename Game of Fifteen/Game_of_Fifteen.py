import random


def create_board():
    numbers = list(range(1, 16))
    random.shuffle(numbers)
    numbers.append(None)

    board = [numbers[i:i+4] for i in range(0, 16, 4)]
    return board


def display_board(board):
    for row in board:
        print(' | '.join(str(num).rjust(2)
              if num is not None else '  ' for num in row))
        print('-' * 23)


def get_empty_position(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] is None:
                return i, j


def is_valid_move(move, empty_row, empty_col):
    row, col = move
    return (0 <= row < 4 and 0 <= col < 4 and
            (row == empty_row and abs(col - empty_col) == 1 or
             col == empty_col and abs(row - empty_row) == 1))


def make_move(board, move):
    empty_row, empty_col = get_empty_position(board)
    row, col = move
    board[empty_row][empty_col], board[row][col] = board[row][col], board[empty_row][empty_col]


def check_win(board):
    return all(board[i][j] == i*4 + j + 1 for i in range(4) for j in range(4)) and board[3][3] is None


def game_of_fifteen():
    board = create_board()

    print("Welcome to the Game of Fifteen!")
    print("Arrange the numbers in numerical order by sliding the tiles.")
    print("Enter 'Q' to quit.")

    while not check_win(board):
        display_board(board)
        move = input(
            "Enter the number you want to move (1-15) or 'Q' to quit: ")

        if move.lower() == 'q':
            print("Quitting the game...")
            break

        if not move.isdigit() or int(move) not in range(1, 16):
            print("Invalid input. Please enter a number from 1 to 15.")
            continue

        move = int(move)
        empty_row, empty_col = get_empty_position(board)

        moves = [(empty_row - 1, empty_col), (empty_row + 1, empty_col),
                 (empty_row, empty_col - 1), (empty_row, empty_col + 1)]

        if any(is_valid_move(move, row, col) for row, col in moves):
            make_move(board, (empty_row, empty_col))
        else:
            print("Invalid move. Try again.")

    if check_win(board):
        print("Congratulations! You solved the puzzle.")


if __name__ == "__main__":
    game_of_fifteen()
