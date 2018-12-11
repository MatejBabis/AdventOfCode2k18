import numpy as np
from scipy.spatial.distance import cdist

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
    # sum the distances to input points
    distances_sum = np.sum(distances, axis=0)
    # add those distances that are < 10000 units away from all points combined
    result = np.sum(distances_sum < 10000)

    print("Answer:", result)
