# Pseudocode outline:
# 1. Initialize 100x100 grid with all susceptible (0)
# 2. Randomly select one cell to be infected (1)
# 3. For each time step:
#    a. Copy current grid to avoid overwriting
#    b. For each infected cell:
#       i. With probability gamma, recover to state 2
#       ii. Infect all susceptible neighbours with probability beta
#    c. Update grid
#    d. Plot the grid every 10 steps
import numpy as np
import matplotlib.pyplot as plt

# ----------------------
# Parameters
# ----------------------
grid_size = 100
time_steps = 100
beta = 0.3   # infection probability to neighbours
gamma = 0.05 # recovery probability

# ----------------------
# Initialize grid
# 0: susceptible, 1: infected, 2: recovered
# ----------------------
population = np.zeros((grid_size, grid_size), dtype=int)

# Randomly choose outbreak location
outbreak = np.random.choice(range(grid_size), 2)
x0, y0 = outbreak[0], outbreak[1]
population[x0, y0] = 1

# ----------------------
# Helper: get 8 neighbours (ignore out-of-bounds)
# ----------------------
def get_neighbours(x, y, size):
    neighbours = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size:
                neighbours.append((nx, ny))
    return neighbours

# ----------------------
# Simulation loop
# ----------------------
for t in range(time_steps):
    # Make a copy to avoid overwriting during updates
    new_population = population.copy()

    # Find all infected cells
    infected_cells = np.where(population == 1)
    infected_coords = list(zip(infected_cells[0], infected_cells[1]))

    # Step 1: Infected cells recover with probability gamma
    for (x, y) in infected_coords:
        if np.random.rand() < gamma:
            new_population[x, y] = 2

    # Step 2: Infected cells spread to neighbours with probability beta
    for (x, y) in infected_coords:
        neighbours = get_neighbours(x, y, grid_size)
        for (nx, ny) in neighbours:
            if population[nx, ny] == 0:  # only infect susceptible
                if np.random.rand() < beta:
                    new_population[nx, ny] = 1

    # Update the grid
    population = new_population

    # Plot every 10 steps to show progression
    if t % 10 == 0:
        plt.figure(figsize=(5, 5))
        plt.imshow(population, cmap='viridis', interpolation='nearest', vmin=0, vmax=2)
        plt.title(f'Spatial SIR Model - Time Step {t}')
        plt.colorbar(ticks=[0, 1, 2], label='State')
        plt.gca().set_xticks([])
        plt.gca().set_yticks([])
        plt.show()