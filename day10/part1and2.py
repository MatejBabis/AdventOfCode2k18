import re
import numpy as np
from collections import defaultdict

MAX_ITERATIONS = 20000


def open_file(filename):
    f = open(filename)

    output = defaultdict(list)
    for line in f.readlines():
        # regex processing to extract information
        m = re.search(r'position=<(-?\d+),(-?\d+)>velocity=<(-?\d+),(-?\d+)>',
                      line.strip().replace(" ", ""))
        # store as tuples
        pos = (int(m.group(1)), int(m.group(2)))
        vel = (int(m.group(3)), int(m.group(4)))
        output[pos].append(vel)

    f.close()
    return output


def print_sky(data_dict):
    # find the corners of the printable area
    min_x, min_y = np.amin(list(data_dict.keys()), axis=0)
    max_x, max_y = np.amax(list(data_dict.keys()), axis=0)

    # print the grid
    for y in np.arange(min_y, max_y + 1):
        for x in np.arange(min_x, max_x + 1):
            if (x, y) in data_dict:
                print('#', end='')
            else:
                print(".", end='')
        print()

def update_pos(data_dict):
    updated_data = defaultdict(list)
    for pos in data_dict.keys():
        # this loop exists because multiple points of light
        # might share one location at some point
        for vel in data_dict[pos]:
            updated_data[tuple(np.array(pos) + np.array(vel))].append(vel)
    return updated_data


# computes area of the bounding box
def calculate_area(data_dict):
    min_x, min_y = np.amin(list(data_dict.keys()), axis=0)
    max_x, max_y = np.amax(list(data_dict.keys()), axis=0)
    return (max_x - min_x) * (max_y - min_y)


if __name__ == "__main__":
    data = open_file("input.txt")

    # under the *assumption* that points will get closer to one another (correct)
    # to form the text, compute the area of the bounding box
    area = calculate_area(data)

    for clock in range(MAX_ITERATIONS):
        # compute candidate value
        future_data = update_pos(data)
        future_area = calculate_area(future_data)
        # the area size is converging, old values are replaced by candidates
        if future_area < area:
            data = future_data
            area = future_area
        # the area size stopped converging - this is the result
        else:
            print_sky(data)
            print("Time taken: {0}s".format(clock))
            break
