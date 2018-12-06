def read_input(filename):
    f = open(filename)
    # only one line, and remove '\n'
    output = f.readline().strip()
    f.close()
    return output


# helper function that checks if two letters are equal are diffent case
def conflict(a, b):
    return a.lower() == b.lower() and ((a.isupper() and b.islower()) or (a.islower() and b.isupper()))


# recation function
def polymer_reaction(string, ignored=None):
    stack = []
    for c in string:
        if c.lower() == ignored:
            continue    # skip
        if len(stack) == 0:
            stack.append(c)
        elif conflict(stack[-1], c):
            stack.pop()
        else:
            stack.append(c)
    return stack


if __name__ == "__main__":
    s = read_input("input.txt")
    print("Answer:", len(polymer_reaction(s)))
