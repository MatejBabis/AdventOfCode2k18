f = open("input.txt")

# counter [doubles, triples]
counter = [0, 0]
for string in f.readlines():
    double_flag = False
    triple_flag = False
    string = string[:-1]    # trim '\n'

    for letter in string:
        letters_encountered = set()     # for efficiency, don't check a letter twice
        if (double_flag is True and triple_flag is True) \
                or letter in letters_encountered:
            continue
        else:
            letters_encountered.add(letter)
            letter_count = string.count(letter)
            if letter_count is 2:
                double_flag = True
            if letter_count is 3:
                triple_flag = True

    if double_flag is True:
        counter[0] = counter[0] + 1
    if triple_flag is True:
        counter[1] = counter[1] + 1

print("Answer:", counter[0] * counter[1])
