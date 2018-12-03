f = open("input.txt")

foundFlag = False
total = 0
freqDict = set()

while foundFlag is False:
    for number in f.readlines():
        val = int(number[:-1])
        total += val
        if total not in freqDict:
            freqDict.add(total)
        else:
            foundFlag = True
            break

    # go back to first line
    if foundFlag is False:
        f.seek(0)

f.close()

print("Answer:", total)
