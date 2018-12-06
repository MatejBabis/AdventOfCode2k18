import part1

if __name__ == "__main__":
    s = part1.read_input("input.txt")

    results = {}
    # store the length of reaction string when 'c' is removed
    for c in "abcdefghijklmnopqrstuvwxyz":
        results[c] = len(part1.polymer_reaction(s, c))

    # find the minimum value in the dictionary
    minimum_val = min(results.items())
    # what letter does it correspond to
    result = [key for key, val in results.items() if val == minimum_val][0]
    print("Answer: {0} ('{1}')".format(results[result], result))
