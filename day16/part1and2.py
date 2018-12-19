import re
from collections import defaultdict

OPS = {
    # addition
    'addr': lambda reg, a, b: reg[a] + reg[b],
    'addi': lambda reg, a, b: reg[a] + b,
    # multiplication
    'mulr': lambda reg, a, b: reg[a] * reg[b],
    'muli': lambda reg, a, b: reg[a] * b,
    # bitwise AND
    'banr': lambda reg, a, b: reg[a] & reg[b],
    'bani': lambda reg, a, b: reg[a] & b,
    # biwise OR
    'borr': lambda reg, a, b: reg[a] | reg[b],
    'bori': lambda reg, a, b: reg[a] | b,
    # assignment
    'setr': lambda reg, a, b: reg[a],
    'seti': lambda reg, a, b: a,
    # greater than
    'gtir': lambda reg, a, b: 1 if a > reg[b] else 0,
    'gtri': lambda reg, a, b: 1 if reg[a] > b else 0,
    'gtrr': lambda reg, a, b: 1 if reg[a] > reg[b] else 0,
    # equality
    'eqir': lambda reg, a, b: 1 if a == reg[b] else 0,
    'eqri': lambda reg, a, b: 1 if reg[a] == b else 0,
    'eqrr': lambda reg, a, b: 1 if reg[a] == reg[b] else 0
}


def part1_input(filename):
    f = open(filename)
    container = []
    part1 = f.read().split('\n\n')[:-2]
    for line in part1:
        reg_start, funct, reg_end = line.split('\n')
        # first process "Before" registers...
        reg_start = re.search(r'(?<=Before: \[)(.*)(?=\])', reg_start).group(0)
        reg_start = list(map(int, reg_start.split(', ')))
        # ...then process the function...
        funct = list(map(int, funct.split(' ')))
        # ...and lastly the "After" regissers
        reg_end = re.search(r'(?<=After:  \[)(.*)(?=\])', reg_end).group(0)
        reg_end = list(map(int, reg_end.split(', ')))

        container.append((reg_start, funct, reg_end))
    return container


def part2_input(filename):
    f = open(filename)
    container = []
    part2 = f.read().split('\n\n')[-1].split('\n')

    # last line is empty line
    for line in part2[:-1]:
        container.append(list(map(int, line.split())))
    return container


if __name__ == "__main__":
    data = part1_input("input.txt")
    test = part2_input("input.txt")

    # store function candidate for each opcode "codename"
    candidates = defaultdict(set)

    threeplus_candidates = 0    # the anwer
    for before, instruction, after in data:
        codename = instruction[0]   # shorthand for function descriptor
        output_r = instruction[3]   # shorthand variable for output register
        valid = 0
        # iterate through all functions
        for op in OPS:
            # compute and compare it with the expected answer
            result = OPS[op](before, instruction[1], instruction[2])
            if before[:output_r] + [result] + before[output_r + 1:] == after:
                # correct result
                candidates[codename].add(op)
                valid += 1
        # part 1 answer
        if valid >= 3:
            threeplus_candidates += 1

    # work out what each opcode represents
    mapping = defaultdict()
    while len(candidates) > 0:
        for number, ops_list in candidates.items():
            # if there is only one candidate, we have the answer
            if len(ops_list) == 1:
                mapping[number] = ops_list.pop()
                # remove it from the candidates...
                candidates.pop(number)
                # ...and remove any trace of it to reduce number of candidates
                for other_ops_list in candidates.values():
                    other_ops_list.discard(mapping[number])
                break   # no need to iterate

    # now execute the test
    registers = [0, 0, 0, 0]
    for t in test:
        registers[t[3]] = OPS[mapping[t[0]]](registers, t[1], t[2])

    print("Answer #1:", threeplus_candidates)
    print("Answer #2:", registers[0])
