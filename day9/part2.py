# unfortunately part1 solution cannot be used due to complexity
# of insert / slicing a list when the last marble is 100x larger
#   instead of Circle, use collections.deque
#   (which would also yield a more efficient soluon for part1)
from collections import deque
import part1

ONE_CLKWS = -1
SEVEN_CNTRCLKWS = 7


if __name__ == "__main__":
    n_players, last_marble = part1.open_file("input.txt")

    # game container
    circle = deque([0])
    # initialise score tracker
    scores = [0 for p in range(n_players)]

    # iterate through the marbles available
    for i in range(1, last_marble * 100 + 1):
        player = i % n_players

        if i % 23 != 0:
            circle.rotate(ONE_CLKWS)
            circle.append(i)
        else:
            circle.rotate(SEVEN_CNTRCLKWS)
            # update player score
            scores[player] += (i + circle.pop())
            circle.rotate(ONE_CLKWS)

    answer = max(scores)
    print("Answer:", answer)
