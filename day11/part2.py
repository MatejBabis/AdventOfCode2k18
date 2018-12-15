import numpy as np

GRID_SIZE = 300
INPUT = 9424

def rack_id(x, y):
    return x + 10

def get_power(x, y):
    power = rack_id(x, y) * y + INPUT
    power *= rack_id(x, y)
    return int(str(power)[-3]) - 5 if power > 99 else -5

# takes x,y coordinate of the top-left corner
def fuelcell_power(grid, x, y, size):
    return np.sum(grid[y:y + size, x:x + size])


if __name__ == "__main__":
    grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
    # populate the grid with power values
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            grid[y][x] = get_power(x, y)

    # container for results
    max_power_values = np.zeros((GRID_SIZE), dtype=int)
    max_power_coords = np.zeros((GRID_SIZE, 2), dtype=int)

    # TODO: POSSIBLY CHECK IF RESULTS CONVERGE / DIVERGE
    # iterate through all possible cell sizes
    for cellsize in range(GRID_SIZE):
        for y in range(GRID_SIZE - cellsize):
            for x in range(GRID_SIZE - cellsize):
                # scan the grid for highest cellsize x cellsize power sum
                power = fuelcell_power(grid, x, y, cellsize + 1)
                if power > max_power_values[cellsize]:
                    max_power_values[cellsize] = power
                    max_power_coords[cellsize] = (x, y)

    # get the index of the max value
    max_value_i = np.where(max_power_values == max(max_power_values))[0][0]
    print("Answer:", tuple(max_power_coords[max_value_i]), max_value_i + 1)
