import math


def is_valid(board, row, col, num, group_size):
    # Check if 'num' can be placed in the given position without violating the rules
    # Check row and column
    for i in range(len(board)):
        if board[i][col] == num or board[row][i] == num:
            return False

    # Check the group constraints
    group_start_row, group_start_col = row - \
        row % group_size, col - col % group_size
    for i in range(group_size):
        for j in range(group_size):
            if board[group_start_row + i][group_start_col + j] == num:
                return False

    return True


def find_empty_cell(board):
    # Find an empty cell (cell with value 0) on the board and return its coordinates
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return i, j
    return None


def solve_kenken(board, group_size):
    # Function to solve the KenKen puzzle using backtracking
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        # If no empty cell found, the board is solved
        return True

    row, col = empty_cell

    for num in range(1, len(board) + 1):
        if is_valid(board, row, col, num, group_size):
            board[row][col] = num

            if solve_kenken(board, group_size):
                return True

            board[row][col] = 0

    return False


def validate_puzzle_input(size, groups):
    # Function to validate the user-provided KenKen puzzle input
    # Check for the following conditions:
    # 1. The board size is valid (greater than 1 and a perfect square)
    # 2. The number of groups is equal to the board size
    # 3. Each group has a valid target number (greater than 0)
    # 4. Each group operation is valid (+, -, *, /)

    if size <= 1 or int(size ** 0.5) ** 2 != size:
        print("Invalid board size. The size should be greater than 1 and a perfect square.")
        return False

    if len(groups) != size:
        print(f"Invalid number of groups. Expected {size} groups.")
        return False

    valid_operations = {'+', '-', '*', '/'}
    for target, operation in groups:
        if target <= 0:
            print(
                "Invalid target number. The target number should be greater than 0 for each group.")
            return False
        if operation not in valid_operations:
            print("Invalid operation. Valid operations are '+', '-', '*', or '/'.")
            return False

    return True


def get_puzzle_input():
    # Function to get the KenKen puzzle input from the user
    size = int(input("Enter the size of the grid (e.g., 5 for a 5x5 puzzle): "))
    group_size = int(
        input("Enter the size of each group (e.g., 3 for a standard 9x9 puzzle): "))

    groups = []
    for i in range(size):
        while True:
            try:
                group_target = int(
                    input(f"Enter the target number for group {i + 1}: "))
                group_operation = input(
                    f"Enter the operation for group {i + 1} (+, -, *, /): ")
                groups.append((group_target, group_operation))
                break
            except ValueError:
                print("Invalid input. Please enter a valid target number and operation.")

    if validate_puzzle_input(size, groups):
        return size, group_size, groups
    else:
        print("Invalid puzzle input. Please try again.")
        return None


def print_board(board):
    # Function to pretty print the KenKen board
    for row in board:
        print(" ".join(str(num) if num != 0 else "-" for num in row))
    print()


def main():
    # Main function to run the KenKen puzzle solver
    print("KenKen Puzzle Solver")

    puzzle_input = get_puzzle_input()
    if puzzle_input:
        size, group_size, groups = puzzle_input

        # Initialize the board with zeros
        kenken_board = [[0 for _ in range(size)] for _ in range(size)]

        if solve_kenken(kenken_board, group_size):
            print("Solved KenKen Puzzle:")
            print_board(kenken_board)
        else:
            print("No solution exists.")


if __name__ == "__main__":
    main()
