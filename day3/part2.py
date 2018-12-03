import numpy as np
import part1

if __name__ == "__main__":
    board, claims = part1.create_board("input.txt")

    unique_id = None    # store the result
    for id, x0, y0, width, height in claims:
        unique = True
        for y in np.arange(y0, y0 + height):
            for x in np.arange(x0, x0 + width):
                # loop through board pieces only claimed by this claim
                if board[y][x][0] != 1:
                    unique = False  # stop if other claim found for this (x,y)
                    break
            # leave the double for loop
            if unique is False:
                break
        # we have a result, no need to consider other claims
        if unique is True:
            unique_id = id
            break

    print("Answer:", unique_id)
