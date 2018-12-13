def open_file(filename):
    raw_text = open(filename)
    words = raw_text.readline().split()

    # return number of players and value of last marble
    return int(words[0]), int(words[6])

# we use a circular list as a container
class Circle:
    def __init__(self):
        self.data = [0]
        self.current = 0

    def add(self, i, score):
        # usual case
        if i % 23 != 0:
            one_clkws = (self.current + 1) % len(self.data) + 1
            self.current = one_clkws
            self.data.insert(one_clkws, i)

        # mod 23 special case
        else:
            seven_cntrclkws = (self.current - 7) % len(self.data)
            score += (i + self.data[seven_cntrclkws])
            del self.data[seven_cntrclkws]
            self.current = seven_cntrclkws

        return score


if __name__ == "__main__":
    n_players, last_marble = open_file("input.txt")

    # game container
    circle = Circle()
    # initialise score tracker
    scores = [0 for p in range(n_players)]

    # iterate through the marbles available
    for marble in range(1, last_marble + 1):
        player = marble % n_players
        # update player score
        scores[player] = circle.add(marble, scores[player])

    answer = max(scores)
    print("Answer:", answer)
