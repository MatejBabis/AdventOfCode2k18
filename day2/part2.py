f = open("input.txt")
text = []
for line in f.readlines():
    text += [line[:-1]]     # trim '\n'

finished = False
seen = set()
for i, w1 in enumerate(text):
    for j, w2 in enumerate(text):
        answer = ""
        diff = 0
        assert(len(w1) == len(w2))  # sanity check

        # don't compare a string with itself, or repeat a comparison
        if i is j or (i, j) in seen:
            continue
        seen.update([(i, j), (j,  i)])  # append indices to "seen" set

        for letter_index, _ in enumerate(w1):   # or could be w2
            # build up answer string, otherwise increment difference counter
            if w1[letter_index] is w2[letter_index]:
                answer += w1[letter_index]
            else:
                diff += 1

            if diff > 1:
                break   # no need to continue

        if diff is 1:
            # no need to loop anymore
            finished = True
            print("line", i, "\t", text[i])
            print("line", j, "\t", text[j])
            break

    if finished is True:
        break

f.close()

print("Answer:", answer)
