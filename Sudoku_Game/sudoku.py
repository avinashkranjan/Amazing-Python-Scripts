import tkinter as tk
from tkinter import messagebox, simpledialog
import random


class Sudoku:
    def __init__(self, master):
        self.master = master
        self.board = [[0] * 9 for _ in range(9)]
        self.solution = [[num for num in row] for row in self.board]
        self.empty_cells = self.get_empty_cells(self.board)
        self.create_widgets()

    def create_widgets(self):
        self.master.configure(bg='#ECECEC')
        self.canvas = tk.Canvas(self.master, width=680,
                                height=680, bg='#F8C8DC', highlightthickness=0)
        self.canvas.pack(side=tk.TOP, padx=0, pady=0)

        self.draw_board()

        self.button_frame = tk.Frame(self.master, bg='#ECECEC')
        self.button_frame.pack(side=tk.TOP, pady=20)

        self.check_button = tk.Button(self.button_frame, text='Check', font=('Inter', 12, 'bold'),
                                      bg='#E75442', fg='#FFFFFF', bd=0, command=self.check_solution)
        self.check_button.pack(side=tk.LEFT, padx=10)

        self.solve_button = tk.Button(self.button_frame, text='Solve', font=('Inter', 12, 'bold'),
                                      bg='#3AC6FF', fg='#FFFFFF', bd=0, command=self.solve_puzzle)
        self.solve_button.pack(side=tk.LEFT, padx=10)

        self.level_frame = tk.Frame(self.master, bg='#ECECEC')
        self.level_frame.pack(side=tk.TOP, pady=0)

        self.level_label = tk.Label(self.level_frame, text='Select Level:', font=(
            'Inter', 12, "bold"), bg='#77DD77', fg='#ECECEC')
        self.level_label.pack(side=tk.LEFT, padx=10)

        self.level_var = tk.StringVar()
        self.level_var.set('Easy')
        self.level_dropdown = tk.OptionMenu(self.level_frame, self.level_var, 'Easy', 'Medium', 'Hard',
                                            command=self.new_game)
        self.level_dropdown.config(
            font=('Arial', 12, "bold"), bg='#ffb347', fg='#ECECEC', bd=0)
        self.level_dropdown.pack(side=tk.LEFT, padx=10)

        self.new_game_button = tk.Button(self.level_frame, text='New Game', font=('Inter', 12, 'bold'),
                                         bg='#FFD700', fg='#ECECEC', bd=0, command=self.new_game_wrapper)
        self.new_game_button.pack(side=tk.LEFT, padx=10)
        self.canvas.bind("<Button-1>", self.on_cell_click)

    def new_game_wrapper(self):
        level = self.level_var.get()
        self.new_game(level)

    def new_game(self, level):
        if level == 'Easy':
            num_cells = 40
        elif level == 'Medium':
            num_cells = 50
        elif level == 'Hard':
            num_cells = 60

        self.board = [[0] * 9 for _ in range(9)]
        self.generate_puzzle()
        self.remove_cells(num_cells)
        self.empty_cells = self.get_empty_cells(self.board)
        self.draw_board()

    def generate_puzzle(self):
        self.solve_board(self.board)
        for _ in range(81):
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            temp = self.board[row][col]
            self.board[row][col] = 0
            count = 0
            solution_copy = [row[:] for row in self.board]
            self.solve_board(solution_copy)
            for i in range(9):
                if 0 in solution_copy[i]:
                    count += 1
            if count != 1:
                self.board[row][col] = temp

    def solve_board(self, board):
        empty_cell = self.get_empty_cell(board)
        if not empty_cell:
            return True

        row, col = empty_cell
        for num in range(1, 10):
            if self.is_valid_move(board, row, col, num):
                board[row][col] = num
                if self.solve_board(board):
                    return True
                board[row][col] = 0
        return False

    def on_cell_click(self, event):
        x, y = event.x, event.y
        row, col = (y - 80) // 60, (x - 80) // 60
        if self.board[row][col] != 0:
            messagebox.showinfo(
                'Invalid Move', 'Cannot change pre-filled cells!')
            return
        num = tk.simpledialog.askinteger(
            'Input', 'Enter a number (1-9):', minvalue=1, maxvalue=9)
        if num:
            self.board[row][col] = num
            self.draw_board()

    def get_empty_cell(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return None

    def is_valid_move(self, board, row, col, num):
        return (
            self.is_valid_row(board, row, num)
            and self.is_valid_col(board, col, num)
            and self.is_valid_box(board, row - row % 3, col - col % 3, num)
        )

    def is_valid_row(self, board, row, num):
        for i in range(9):
            if board[row][i] == num:
                return False
        return True

    def is_valid_col(self, board, col, num):
        for i in range(9):
            if board[i][col] == num:
                return False
        return True

    def is_valid_box(self, board, start_row, start_col, num):
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        return True

    def draw_board(self):
        self.clear_board()
        for i in range(9):
            for j in range(9):
                x = i * 60 + 80
                y = j * 60 + 80
                cell_value = self.board[j][i]
                if cell_value != 0:
                    # Adjust the coordinates to avoid intersection
                    text_x = x + 15
                    text_y = y + 15
                    self.canvas.create_text(text_x, text_y, text=str(
                        cell_value), font=('Inter', 20, 'bold'), fill='#333333')

        self.draw_grid()

    def draw_grid(self):
        for i in range(10):
            if i % 3 == 0:
                line_width = 2
            else:
                line_width = 1
            self.canvas.create_line(
                60 * i + 80, 80, 60 * i + 80, 620, width=line_width, fill='#333333')
            self.canvas.create_line(
                80, 60 * i + 80, 620, 60 * i + 80, width=line_width, fill='#333333')

    def clear_board(self):
        self.canvas.delete('all')

    def check_solution(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != self.solution[i][j]:
                    messagebox.showinfo(
                        'Incorrect', 'The solution is not correct!')
                    return
        messagebox.showinfo(
            'Correct', 'Congratulations! You solved the puzzle!')

    def remove_cells(self, num_cells):
        cells = [(i, j) for i in range(9) for j in range(9)]
        random.shuffle(cells)
        for i in range(num_cells):
            row, col = cells[i]
            self.board[row][col] = 0

    def get_empty_cells(self, board):
        empty_cells = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    empty_cells.append((i, j))
        return empty_cells

    def solve_puzzle(self):
        solution_board = [row[:] for row in self.board]
        if self.solve_board(solution_board):
            self.solution = solution_board
            self.board = solution_board
            self.draw_board()
        else:
            messagebox.showinfo(
                'Unsolvable', 'The puzzle does not have a solution.')


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Sudoku')
    gui = Sudoku(root)
    root.mainloop()
