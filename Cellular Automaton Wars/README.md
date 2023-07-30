# Cellular Automaton Wars

Cellular Automaton Wars is a simulation game where players design and deploy cellular automaton-based organisms to compete for resources in a virtual environment. Each organism's behavior is determined by its cellular automaton rules, and the player must strategize to create the most successful organisms and outcompete others.

## Features

- Organisms interact with nearby cells and consume resources.
- Organisms have energy levels and can reproduce when reaching a certain threshold.
- Organisms can move left or right based on certain conditions or rules.
- The player can influence the game by adding/removing organisms and resources at specific locations.

## How to Use

1. Clone the repository or download the script file.

2. Open a terminal or command prompt and navigate to the directory containing the script.

3. Run the script using Python:

```bash
python cellular_automaton_wars.py
```

4. The script will initialize the grid with organisms and resources and simulate their behavior for a certain number of iterations. The output will display the state of the grid at each iteration.

## Customization

You can customize the game by adjusting the following constants in the script:

- `GRID_SIZE`: Change the size of the grid to accommodate more cells.
- `NUM_ORGANISMS`: Set the initial number of organisms in the grid.
- `NUM_RESOURCES`: Set the initial number of resources in the grid.
- `ENERGY_THRESHOLD`: Adjust the energy threshold for organisms to reproduce.

You can also define new rules in the `RULES` dictionary to create different behaviors for organisms based on their energy levels.

## Contributions

Contributions are welcome! If you find any issues or have ideas to improve the game, please feel free to create a pull request or open an issue.

## Acknowledgments

The game is inspired by cellular automaton simulations and evolutionary algorithms.