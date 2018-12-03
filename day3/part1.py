import numpy as np

# process text input into desirable format
def line_processing(l):
    id = l[:-1].split('@')[0][1:]
    object = l[:-1].split('@')[1][1:]
    corner = object.split(':')[0].split(',')
    dims = object.split(':')[1][1:].split('x')

    return tuple(map(int, [id] + corner + dims))


def create_board(filename):
    f = open(filename)

    board = np.zeros((1000, 1000, 2))
    claims = []
    for line in f.readlines():
        id, x0, y0, width, height = line_processing(line)
        claims += [(id, x0, y0, width, height)]

        for y in np.arange(y0, y0 + height):
            for x in np.arange(x0, x0 + width):
                board[y][x][0] = board[y][x][0] + 1
                board[y][x][1] = id

    f.close()
    return board, claims


if __name__ == "__main__":
    board, _ = create_board("input.txt")

    counter = 0
    for y in np.arange(board.shape[0]):
        for x in np.arange(board.shape[1]):
            if board[y][x][0] > 1:
                counter += 1

    print("Answer:", counter)
