import random

GRID_SIZE = 50
NUM_ORGANISMS = 5
NUM_RESOURCES = 20
ENERGY_THRESHOLD = 10

RULES = {
    0: lambda neighbors, energy: (sum(neighbors) + energy) % 2,
    1: lambda neighbors, energy: (sum(neighbors) - energy) % 2
}


def initialize_grid():
    grid = [0] * GRID_SIZE
    for _ in range(NUM_ORGANISMS):
        organism_position = random.randint(0, GRID_SIZE - 1)
        grid[organism_position] = random.randint(1, 5)
    for _ in range(NUM_RESOURCES):
        resource_position = random.randint(0, GRID_SIZE - 1)
        resource_value = random.randint(1, 5)
        grid[resource_position] = -resource_value
    return grid


def get_neighbors(grid, index):
    neighbors = []
    if index > 0:
        neighbors.append(grid[index - 1])
    if index < GRID_SIZE - 1:
        neighbors.append(grid[index + 1])
    return neighbors


def apply_rule(grid, index):
    cell_state = grid[index]
    neighbors = get_neighbors(grid, index)
    if cell_state > 0:  # If the cell represents an organism.
        energy = cell_state
        new_state = RULES[cell_state % len(RULES)](neighbors, energy)
        if energy >= ENERGY_THRESHOLD and grid.count(0) > 1:
            empty_spots = [i for i in range(GRID_SIZE) if grid[i] == 0]
            new_organism_position = random.choice(empty_spots)
            # New organism created through reproduction.
            grid[new_organism_position] = energy // 2
        grid[index] = new_state
    elif cell_state < 0:  # If the cell represents a resource.
        grid[index] = 0


def run_simulation(grid, num_iterations):
    for _ in range(num_iterations):
        new_grid = grid.copy()
        for i in range(GRID_SIZE):
            apply_rule(new_grid, i)
        grid = new_grid
    return grid


def display_grid(grid):
    for cell in grid:
        if cell == 0:
            print('.', end=' ')
        elif cell > 0:
            print('O', end=' ')
        else:
            print(abs(cell), end=' ')
    print()


def main():
    grid = initialize_grid()
    display_grid(grid)

    num_iterations = 10
    grid = run_simulation(grid, num_iterations)

    print("\nSimulation Results:")
    display_grid(grid)


if __name__ == "__main__":
    main()
