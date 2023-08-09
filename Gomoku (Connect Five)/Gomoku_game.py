def create_board(size):
    return [[' ' for _ in range(size)] for _ in range(size)]


def display_board(board):
    size = len(board)
    for row in board:
        print(' | '.join(row))
        print('-' * (size * 4 - 1))


def check_win(board, row, col):
    size = len(board)
    player = board[row][col]

    # Check horizontal
    for i in range(max(0, col - 4), min(size, col + 5)):
        if board[row][i:i + 5] == [player] * 5:
            return True

    # Check vertical
    for i in range(max(0, row - 4), min(size, row + 5)):
        if all(board[i + j][col] == player for j in range(5)):
            return True

    # Check diagonal (top-left to bottom-right)
    for i in range(max(0, row - 4), min(size - 4, row + 1)):
        if all(board[row + j][col + j] == player for j in range(5)):
            return True

    # Check diagonal (bottom-left to top-right)
    for i in range(max(0, row - 4), min(size - 4, row + 1)):
        if all(board[row - j][col + j] == player for j in range(5)):
            return True

    return False


def is_board_full(board):
    return all(board[row][col] != ' ' for row in range(len(board)) for col in range(len(board[0])))


def gomoku():
    size = 15
    board = create_board(size)
    player = 'X'

    while True:
        display_board(board)

        if is_board_full(board):
            print("It's a draw!")
            break

        row = int(input(f"Player {player}, enter row (0-{size - 1}): "))
        col = int(input(f"Player {player}, enter column (0-{size - 1}): "))

        if 0 <= row < size and 0 <= col < size and board[row][col] == ' ':
            board[row][col] = player

            if check_win(board, row, col):
                display_board(board)
                print(f"Player {player} wins!")
                break

            player = 'O' if player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")


if __name__ == "__main__":
    gomoku()
