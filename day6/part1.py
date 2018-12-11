import numpy as np
from scipy.spatial.distance import cdist
from collections import Counter

# optionally plot results
def visualise_results(input, grid):
    import matplotlib.pyplot as plt
    plt.imshow(np.where(grid > len(input), np.NaN, grid))
    plt.colorbar()
    plt.show()


if __name__ == "__main__":
    input_points = np.loadtxt('input.txt', delimiter=', ')

    # find min/max coordinates for rectangle corners
    min_x, min_y = np.amin(input_points, axis=0)
    max_x, max_y = np.amax(input_points, axis=0)

    # shape of the rectangle considered
    x_range = np.arange(min_x, max_x + 1)   # we want to include the max
    y_range = np.arange(min_y, max_y + 1)
    # create coordinate pairs for points evaluated
    candidates = np.array(np.meshgrid(x_range, y_range)).T.reshape(-1, 2)

    # compute cityblock (= Manhattan) distances for each candidate & input point
    distances = cdist(input_points, candidates, metric='cityblock')
    # select the closest point
    grid = np.argmin(distances, axis=0)

    # we want to remove points that have multiple closest points...
    min_distance = np.min(distances, axis=0)
    multple_mins_filter = (distances == min_distance).sum(axis=0) > 1  # filter
    # mark for later
    grid[multple_mins_filter] = -1

    # ...and same goes for points that are on rectangle edges (infinite)
    grid = np.reshape(grid, (len(x_range), len(y_range)))
    borders = np.unique(
        np.hstack([grid[0], grid[-1], grid[:, 0], grid[:, -1]]))
    border_coords_filter = np.isin(grid, borders)     # create a filter
    grid[border_coords_filter] = -1

    # count the results
    areas = Counter(grid.flatten())
    del areas[-1]   # remove values marked invalid
    result = areas.most_common()[0]

    print("Answer: {0} {1}".format(
        result[1], tuple(input_points[result[0]].astype(int))))

    visualise_results(input_points, grid)
