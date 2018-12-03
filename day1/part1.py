f = open("input.txt")

total = 0
for number in f.readlines():
    total += int(number[:-1])
f.close()

print("Answer:", total)
