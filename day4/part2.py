import part1

if __name__ == "__main__":
    sorted_data = part1.process_file("input.txt")
    dataset = part1.organise_records(sorted_data)

    # hold the record (GuardID, "most asleep" minute, value at this minute)
    maximum = (None, None, 0)
    for guard in dataset:
        _, most_sleepy_minute, most_sleepy_minute_val = part1.count_sleeps(
            guard, dataset)
        if most_sleepy_minute_val > maximum[2]:
            maximum = (guard, most_sleepy_minute, most_sleepy_minute_val)

    print("Answer:", maximum[0] * maximum[1])
