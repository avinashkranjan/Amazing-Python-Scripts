import heapq
import random


class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.start = (0, 0)
        self.goal = (self.rows - 1, self.cols - 1)

    def get_neighbors(self, node):
        row, col = node
        neighbors = []
        if row > 0 and not self.maze[row - 1][col]:
            neighbors.append((row - 1, col))
        if row < self.rows - 1 and not self.maze[row + 1][col]:
            neighbors.append((row + 1, col))
        if col > 0 and not self.maze[row][col - 1]:
            neighbors.append((row, col - 1))
        if col < self.cols - 1 and not self.maze[row][col + 1]:
            neighbors.append((row, col + 1))
        return neighbors

    def heuristic(self, node):
        return abs(node[0] - self.goal[0]) + abs(node[1] - self.goal[1])

    def solve(self):
        open_set = []
        closed_set = set()
        g_score = {self.start: 0}
        f_score = {self.start: self.heuristic(self.start)}
        heapq.heappush(open_set, (f_score[self.start], self.start))

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == self.goal:
                path = []
                while current in g_score:
                    path.append(current)
                    current = g_score[current]
                return path[::-1]

            closed_set.add(current)

            for neighbor in self.get_neighbors(current):
                if neighbor in closed_set:
                    continue
                tentative_g_score = g_score[current] + 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + \
                        self.heuristic(neighbor)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return None


def generate_random_maze(rows, cols, obstacle_probability):
    return [[random.random() < obstacle_probability for _ in range(cols)] for _ in range(rows)]


def print_maze(maze):
    for row in maze:
        print("".join(["#" if cell else " " for cell in row]))


def main():
    rows = 10
    cols = 10
    obstacle_probability = 0.2

    maze = generate_random_maze(rows, cols, obstacle_probability)
    print("Random Maze:")
    print_maze(maze)

    maze_solver = MazeSolver(maze)
    path = maze_solver.solve()

    if path:
        print("\nSolution Path:")
        for node in path:
            maze[node[0]][node[1]] = True  # Marking the path in the maze
        print_maze(maze)
    else:
        print("\nNo path found!")


if __name__ == "__main__":
    main()
