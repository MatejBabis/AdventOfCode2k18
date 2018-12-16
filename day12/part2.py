import numpy as np
import part1

# this number is too big to iterate through
# instead, we look for a repeating pattern
GENERATIONS = int(5e10)


if __name__ == "__main__":
    state, rules = part1.input_parser("input.txt")

    front_pad_len = 0
    sum_previous_gen = 0
    diff = 0
    for i in range(GENERATIONS):
        # prepend '.' so that there are always at least 5 dots at the front
        front_pad = ['.' for _ in range(5 - state.index('#'))]
        # append '.' so that there are always at least 5 dots at the end
        back_pad = ['.' for _ in range(5 - part1.rindex(state, '#'))]
        # keep track of how many 0s have been prepended
        front_pad_len += len(front_pad)

        # attach the padding
        state = front_pad + state + back_pad

        # to be the future state
        future_state = state.copy()

        # we skip the first 2 and last 2 pots
        for pot in range(2, len(state) - 2):
            # the pattern currently examined
            substring = "".join(state[pot - 2:pot + 3])
            # corresponding action
            if substring in rules:
                future_state[pot] = rules[substring]
            else:
                future_state[pot] = "."

        # update the state
        state = future_state
        # compute the sum of the numbers of all pots which contain a plant
        plants = [
            i - front_pad_len for i in range(len(state)) if state[i] == "#"]
        sum = np.sum(plants)

        # if the change of sum in the previous generation was the same,
        # we hit a linear pattern and we don't need to iterate anymore
        if diff == sum - sum_previous_gen:
            print("Answer:", (sum + (GENERATIONS - i - 1) * diff))
            break
        else:
            diff = sum - sum_previous_gen
            sum_previous_gen = sum
