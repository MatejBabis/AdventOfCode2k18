import numpy as np

GENERATIONS = 20

def input_parser(filename):
    f = open(filename)

    init_state = f.readline().split()[2]

    rules = {}
    f.readline()    # skip the empty line
    for line in f.readlines():
        pattern, _, output = line.strip().split()
        rules[pattern] = output

    f.close()
    return list(init_state), rules

# returns the distance of the last occurence of a char from the end of a string
def rindex(a, x):
    return a[-1::-1].index(x)


if __name__ == "__main__":
    state, rules = input_parser("input.txt")

    front_pad_len = 0
    for i in range(GENERATIONS):
        # prepend '.' so that there are always at least 5 dots at the front
        front_pad = ['.' for _ in range(5 - state.index('#'))]
        # append '.' so that there are always at least 5 dots at the end
        back_pad = ['.' for _ in range(5 - rindex(state, '#'))]
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
        # print("%2d: " % (i + 1), "".join(state))

    # compute the sum of the numbers of all pots which contain a plant
    plants = [i - front_pad_len for i in range(len(state)) if state[i] == "#"]
    print("Answer:", np.sum(plants))
