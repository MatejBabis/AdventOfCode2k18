import re
import numpy as np

# strings to match
ASLEEP = 'falls asleep'
AWAKE = 'wakes up'
GUARD = 'Guard'

# process the input file
def process_file(filename):
    f = open(filename)

    records_list = []
    for line in f.readlines():
        raw = line[6:-1]   # first six letter carry no information
        month = int(raw[:2])
        day = int(raw[3:5])
        hour = int(raw[6:8])
        minute = int(raw[9:11])
        message = raw[13:]
        records_list += [(month, day, hour, minute, message)]

    f.close()

    # sort the items based on timestamps
    records_list.sort(key=lambda x: (x[0], x[1], x[2], x[3]))

    return records_list

# create a dictionary with data for each guard
def organise_records(array):
    output = {}
    # sleeping = False    # flag

    # initialise variable
    guard_id = None
    asleep_from = None
    asleep_to = None

    for log in array:
        msg = log[4]
        # only minutes as sleep happens between 00:00 and 00:59
        time = log[3]
        # initialise
        if guard_id not in output:
            output[guard_id] = []
        # get ID from string 'Guard #X begins shift'
        if msg.startswith(GUARD):
            guard_id = int(re.findall(r'\d+', msg)[0])
        # get 'falls asleep' time
        elif msg == ASLEEP:
            # sleeping = True
            asleep_from = time
        # get 'wakes up' time and stores in dictionary
        elif msg == AWAKE:
            asleep_to = time
            # store datum
            output[guard_id] += [(asleep_from, asleep_to)]
        # unexpected input
        else:
            raise ValueError('Unexpected input: ', log)

    return output

# return a triple used to computer answers:
#   1. minutes asleep,
#   2. the minute the guard is asleep most often
#   3. the maximum value at 2.
def count_sleeps(g, data):
    asleep_at_minute = np.zeros(60)
    for timestamp in data[g]:
        for minute in range(timestamp[0], timestamp[1]):
            asleep_at_minute[minute] = asleep_at_minute[minute] + 1

    return np.sum(asleep_at_minute), np.argmax(asleep_at_minute), max(asleep_at_minute)


if __name__ == "__main__":
    sorted_data = process_file("input.txt")
    dataset = organise_records(sorted_data)

    # hold the record (GuardID, how much sleep, "most asleep" minute)
    maximum = (None, 0, None)
    for guard in dataset:
        time_asleep, most_sleepy_minute, _ = count_sleeps(guard, dataset)
        if time_asleep > maximum[1]:
            maximum = (guard, time_asleep, most_sleepy_minute)

    print("Answer:", maximum[0] * maximum[2])
