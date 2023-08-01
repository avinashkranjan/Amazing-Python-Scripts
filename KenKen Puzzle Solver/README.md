# KenKen Puzzle Solver

This is a Python script to solve KenKen puzzles, which are grid-based arithmetic puzzles. The script uses a backtracking algorithm to find a solution that satisfies the rules for each group of cells in the puzzle.

## Requirements

- Python 3.x
- math module (included in Python standard library)

## Features

- Solve KenKen puzzles of various sizes and group configurations.
- Customizable grid size and group size.
- Input validation to ensure a valid puzzle is provided.
- User-friendly interface to input the KenKen puzzle interactively.
- Pretty printing of the solved KenKen puzzle.

## How to Use

1. Ensure you have Python 3.x installed on your system.
2. Run the script `kenken_puzzle_solver.py`.
3. Follow the on-screen instructions to input the puzzle details:
   - Enter the size of the grid (e.g., 5 for a 5x5 puzzle).
   - Enter the size of each group (e.g., 3 for a standard 9x9 puzzle).
   - For each group, enter the target number and the operation (+, -, *, /).
4. The script will attempt to solve the puzzle and display the solution or inform you if no solution exists.

## How It Works

1. The script uses a backtracking algorithm to fill the grid with numbers that satisfy the rules for each group.
2. The `solve_kenken` function recursively explores possible solutions until the puzzle is solved or no solution exists.
3. The `is_valid` function checks if a number can be placed in a cell without violating the rules of the puzzle.

## Contributing

If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.
