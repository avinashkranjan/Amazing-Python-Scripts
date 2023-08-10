import random
import copy


class AI2048:
    def __init__(self, board):
        self.board = board

    def get_empty_cells(self):
        empty_cells = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    empty_cells.append((i, j))
        return empty_cells

    def get_max_tile(self):
        return max(map(max, self.board))

    def move_left(self):
        merged = []
        for row in self.board:
            new_row = [tile for tile in row if tile != 0]
            for i in range(len(new_row) - 1):
                if new_row[i] == new_row[i + 1]:
                    new_row[i] *= 2
                    new_row[i + 1] = 0
                    merged.append(new_row[i])
            new_row = [tile for tile in new_row if tile != 0]
            new_row.extend([0] * (len(row) - len(new_row)))
            self.board[self.board.index(row)] = new_row
        return merged

    def move_right(self):
        self.flip_board()
        merged = self.move_left()
        self.flip_board()
        return merged

    def move_up(self):
        self.transpose_board()
        merged = self.move_left()
        self.transpose_board()
        return merged

    def move_down(self):
        self.transpose_board()
        merged = self.move_right()
        self.transpose_board()
        return merged

    def get_score(self):
        return sum(map(sum, self.board))

    def get_heuristic_score(self):
        max_tile = self.get_max_tile()
        empty_cells = len(self.get_empty_cells())
        smoothness = self.calculate_smoothness()
        monotonicity = self.calculate_monotonicity()

        # Weighted sum of different heuristics
        return 0.1 * self.get_score() + 2.7 * empty_cells + 1.0 * smoothness + 1.5 * monotonicity + 3.0 * max_tile

    def calculate_smoothness(self):
        smoothness = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] != 0:
                    value = math.log2(self.board[i][j])
                    for (dx, dy) in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                        x, y = i + dx, j + dy
                        if 0 <= x < len(self.board) and 0 <= y < len(self.board[i]) and self.board[x][y] != 0:
                            neighbor_value = math.log2(self.board[x][y])
                            smoothness -= abs(value - neighbor_value)
        return smoothness

    def calculate_monotonicity(self):
        monotonicity = [0, 0, 0, 0]
        for i in range(len(self.board)):
            current = 0
            next = current + 1
            while next < 4:
                while next < 4 and self.board[i][next] == 0:
                    next += 1
                if next >= 4:
                    next -= 1
                current_value = 0 if self.board[i][current] == 0 else math.log2(
                    self.board[i][current])
                next_value = 0 if self.board[i][next] == 0 else math.log2(
                    self.board[i][next])
                if current_value > next_value:
                    monotonicity[0] += next_value - current_value
                elif next_value > current_value:
                    monotonicity[1] += current_value - next_value
                current = next
                next += 1

        for j in range(len(self.board[0])):
            current = 0
            next = current + 1
            while next < 4:
                while next < 4 and self.board[next][j] == 0:
                    next += 1
                if next >= 4:
                    next -= 1
                current_value = 0 if self.board[current][j] == 0 else math.log2(
                    self.board[current][j])
                next_value = 0 if self.board[next][j] == 0 else math.log2(
                    self.board[next][j])
                if current_value > next_value:
                    monotonicity[2] += next_value - current_value
                elif next_value > current_value:
                    monotonicity[3] += current_value - next_value
                current = next
                next += 1

        return max(monotonicity)

    def get_children_states(self):
        children = []
        for move in ['left', 'right', 'up', 'down']:
            new_board = copy.deepcopy(self.board)
            merged = self.move(new_board, move)
            if merged:
                children.append((new_board, merged))
        return children

    def get_best_move(self, depth=3):
        moves = ['left', 'right', 'up', 'down']
        best_score = float('-inf')
        best_move = random.choice(moves)
        for move in moves:
            new_board = copy.deepcopy(self.board)
            merged = self.move(new_board, move)
            if merged:
                child = AI2048(new_board)
                score = self.expectimax(child, depth - 1, False)
                if score > best_score:
                    best_score = score
                    best_move = move
        return best_move

    def expectimax(self, node, depth, is_maximizing):
        if depth == 0:
            return node.get_heuristic_score()

        if is_maximizing:
            max_eval = float('-inf')
            children = node.get_children_states()
            for child_board, merged in children:
                child = AI2048(child_board)
                eval = self.expectimax(child, depth - 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            total_score = 0
            empty_cells = node.get_empty_cells()
            for cell in empty_cells:
                child_board = copy.deepcopy(node.board)
                child_board[cell[0]][cell[1]] = 2
                child = AI2048(child_board)
                eval = self.expectimax(child, depth - 1, True)
                total_score += eval
            return total_score / len(empty_cells)

    def move(self, board, direction):
        merged = []
        if direction == 'left':
            merged = self.move_left(board)
        elif direction == 'right':
            merged = self.move_right(board)
        elif direction == 'up':
            merged = self.move_up(board)
        elif direction == 'down':
            merged = self.move_down(board)
        return merged

    def move_left(self, board):
        merged = []
        for row in board:
            new_row = [tile for tile in row if tile != 0]
            for i in range(len(new_row) - 1):
                if new_row[i] == new_row[i + 1]:
                    new_row[i] *= 2
                    new_row[i + 1] = 0
                    merged.append(new_row[i])
            new_row = [tile for tile in new_row if tile != 0]
            new_row.extend([0] * (len(row) - len(new_row)))
            board[board.index(row)] = new_row
        return merged

    def move_right(self, board):
        self.flip_board(board)
        merged = self.move_left(board)
        self.flip_board(board)
        return merged

    def move_up(self, board):
        self.transpose_board(board)
        merged = self.move_left(board)
        self.transpose_board(board)
        return merged

    def move_down(self, board):
        self.transpose_board(board)
        merged = self.move_right(board)
        self.transpose_board(board)
        return merged

    def flip_board(self, board):
        for row in board:
            row.reverse()

    def transpose_board(self, board):
        board[:] = [list(i) for i in zip(*board)]


def print_board(board):
    for row in board:
        print(row)
    print()


if __name__ == "__main__":
    board = [
        [0, 2, 2, 4],
        [0, 2, 0, 4],
        [0, 4, 2, 0],
        [0, 0, 2, 2]
    ]

    ai = AI2048(board)
    print("Initial Board:")
    print_board(ai.board)

    while True:
        if ai.get_empty_cells():
            move = ai.get_best_move()
            print(f"Moving {move}")
            ai.move(move)
            print_board(ai.board)
        else:
            print("No more moves possible.")
            break
