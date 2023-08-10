import copy

# Reversi Board Size
BOARD_SIZE = 8

# Define player colors
EMPTY = 0
BLACK = 1
WHITE = 2

# Define directions to explore in the board
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0),
              (1, 1), (1, -1), (-1, 1), (-1, -1)]


def create_board():
    return [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def print_board(board):
    print("   " + " ".join(str(i) for i in range(BOARD_SIZE)))
    for i in range(BOARD_SIZE):
        print(f"{i} |" + " ".join(str(board[i][j]) for j in range(BOARD_SIZE)))


def is_valid_move(board, player, row, col):
    if board[row][col] != EMPTY:
        return False

    for dr, dc in DIRECTIONS:
        r, c = row + dr, col + dc
        while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] != EMPTY and board[r][c] != player:
            r, c = r + dr, c + dc
            if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == player:
                return True
    return False


def make_move(board, player, row, col):
    if not is_valid_move(board, player, row, col):
        return False

    board[row][col] = player
    for dr, dc in DIRECTIONS:
        r, c = row + dr, col + dc
        to_flip = []
        while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] != EMPTY and board[r][c] != player:
            to_flip.append((r, c))
            r, c = r + dr, c + dc
            if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == player:
                for flip_row, flip_col in to_flip:
                    board[flip_row][flip_col] = player
                break
    return True


def get_valid_moves(board, player):
    valid_moves = []
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if is_valid_move(board, player, i, j):
                valid_moves.append((i, j))
    return valid_moves


def count_discs(board):
    black_count = sum(row.count(BLACK) for row in board)
    white_count = sum(row.count(WHITE) for row in board)
    return black_count, white_count


def evaluate_board(board, player):
    black_count, white_count = count_discs(board)
    if player == BLACK:
        return black_count - white_count
    else:
        return white_count - black_count


def minimax(board, depth, player, alpha, beta, maximizing_player):
    if depth == 0:
        return evaluate_board(board, player)

    valid_moves = get_valid_moves(board, player)
    if maximizing_player:
        max_eval = float('-inf')
        for row, col in valid_moves:
            new_board = copy.deepcopy(board)
            make_move(new_board, player, row, col)
            eval = minimax(new_board, depth - 1, player, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for row, col in valid_moves:
            new_board = copy.deepcopy(board)
            make_move(new_board, player, row, col)
            eval = minimax(new_board, depth - 1, player, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


def find_best_move(board, player):
    valid_moves = get_valid_moves(board, player)
    best_move = None
    best_eval = float('-inf')

    for row, col in valid_moves:
        new_board = copy.deepcopy(board)
        make_move(new_board, player, row, col)
        move_eval = minimax(new_board, depth=3, player=player, alpha=float(
            '-inf'), beta=float('inf'), maximizing_player=False)

        if move_eval > best_eval:
            best_eval = move_eval
            best_move = (row, col)

    return best_move


def main():
    board = create_board()
    board[3][3], board[4][4] = WHITE, WHITE
    board[3][4], board[4][3] = BLACK, BLACK

    current_player = BLACK

    while True:
        print_board(board)

        if current_player == BLACK:
            row, col = find_best_move(board, BLACK)
            print(f"AI (BLACK) chooses: ({row}, {col})")
        else:
            valid_moves = get_valid_moves(board, WHITE)
            print("Valid moves for White:", valid_moves)
            row = int(input("Enter row: "))
            col = int(input("Enter col: "))

        if not make_move(board, current_player, row, col):
            print("Invalid move! Try again.")
            continue

        black_count, white_count = count_discs(board)
        print(f"Black: {black_count}, White: {white_count}")

        if not get_valid_moves(board, BLACK) and not get_valid_moves(board, WHITE):
            print("Game Over!")
            if black_count > white_count:
                print("Black wins!")
            elif black_count < white_count:
                print("White wins!")
            else:
                print("It's a draw!")
            break

        current_player = WHITE if current_player == BLACK else BLACK


if __name__ == "__main__":
    main()
