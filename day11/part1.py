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
def fuelcell_power(grid, x, y):
    return np.sum(grid[y:y + 3, x:x + 3])


if __name__ == "__main__":
    grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
    # populate the grid with power values
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            grid[y][x] = get_power(x, y)

    max_power_value = 0
    max_power_coord = None
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            # scan the grid for highest 3x3 fuelcell_power
            power = fuelcell_power(grid, x, y)
            if power > max_power_value:
                max_power_value = power
                max_power_coord = (x, y)

    print("Answer:", max_power_coord)
