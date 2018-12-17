import part1


if __name__ == "__main__":
    map = part1.input_parser("input.txt")
    carts, tracks = part1.process_map(map)

    # loop until we have only one cart
    while len(carts) > 1:
        # we were left with two carts, so no (single) last cart will remain
        if len(carts) == 2:
            raise ValueError("NO RESULT: even number of carts remaining")

        # container for carts crashed in this iteration (to be removed)
        crashed = []
        # consider carts based on y (ascending) and then x (ascending)
        carts.sort(key=lambda c: (c.pos.imag, c.pos.real))
        for i, cart in enumerate(carts):
            # update position based on direction
            cart.pos += cart.direction

            # check for crash caused by the new position
            for j, cart2 in enumerate(carts):
                if i != j and cart.pos == cart2.pos:
                    # add the participants to the to-be-removed list
                    crashed += [cart, cart2]
                    break

            # turn if a crash did not occur
            if cart not in crashed:
                track = tracks[cart.pos]
                cart.turn(track)

        # update the list of carts
        carts = [c for c in carts if c not in crashed]

    last_remaining = int(carts[0].pos.real), int(carts[0].pos.imag)
    print("Answer:", last_remaining)
