from collections import defaultdict


class Cart:
    def __init__(self, symbol, pos):
        self.pos = pos
        self.next_rotation = 0

        # transform the symbol into a complex-represented direction
        if symbol == "v":
            self.direction = 1j
        elif symbol == "<":
            self.direction = -1
        elif symbol == ">":
            self.direction = 1
        elif symbol == "^":
            self.direction = -1j

    def __str__(self):
        return self.direction + " " + str(self.x) + "," + str(self.y)

    # downwards facing y axis so imaginary part is flipped
    def turn(self, track):
        if not track:   # empty, | or -
            return
        elif track == '\\':
            if self.direction.real == 0:
                self.direction *= -1j   # turn left
            else:
                self.direction *= 1j    # turn right
        elif track == '/':
            if self.direction.real == 0:
                self.direction *= 1j    # turn right
            else:
                self.direction *= -1j   # turn left
        elif track == "+":
            # first turn left, then straight, then right (and loop)
            self.direction *= -1j * (1j ** self.next_rotation)
            # without the mod we would get inaccuracies in later iterations
            self.next_rotation = (self.next_rotation + 1) % 3


def input_parser(filename):
    f = open(filename)

    map = []
    for i, line in enumerate(f.readlines()):
        map.append(line[:-1])

    f.close()
    return map


def process_map(map):
    carts = []
    # only stores important tracks (with a potential to cause a cart turn)
    tracks = defaultdict(str)

    # iterate through the map
    for y, line in enumerate(map):
        for x, char in enumerate(line):
            # if we find a cart
            if char in 'v><^':
                # store its direction and (x,y) as complex numbers
                # directions are just one of the numbers +1, +1j, -1, -1j
                #   therefore, changing a direction means multiplying it
                #   by either +1j (clockwise turn) or -1j (counterclockwise)
                carts.append(Cart(char, (x + y * 1j)))
            # store the useful tracks
            elif char in '\\/+':
                tracks[(x + y * 1j)] = char

    return carts, tracks


if __name__ == "__main__":
    map = input_parser("input.txt")
    carts, tracks = process_map(map)

    # loop until we have a crash
    crash = None
    while crash is None:
        # consider carts based on y (ascending) and then x (ascending)
        carts.sort(key=lambda c: (c.pos.imag, c.pos.real))
        for i, cart in enumerate(carts):
            # update position based on direction
            cart.pos += cart.direction

            # check for crash caused by the new position...
            for j, cart2 in enumerate(carts):
                if i != j and cart.pos == cart2.pos:
                    crash = int(cart.pos.real), int(cart.pos.imag)

            # ...or turn where appropriate
            track = tracks[cart.pos]
            cart.turn(track)

    print("Answer:", crash)
