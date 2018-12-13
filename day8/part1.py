import numpy as np


def open_file(filename):
    raw_text = open(filename)
    numbers = raw_text.readline().split()

    return np.array(list(map(int, numbers)))


def extractor(input_data):
    sum = 0

    n_children, metadata_entries = input_data[:2]
    payload = input_data[2:]

    # recursively iterate through children nodes
    for child in range(n_children):
        payload_sum, payload = extractor(payload)
        sum += payload_sum

    # when leaf node reached, add the accumulated value to the sum
    metadata = payload[:metadata_entries]
    sum += np.sum(metadata)

    # return the root's sum
    return sum, payload[metadata_entries:]


if __name__ == "__main__":
    data = open_file("input.txt")

    answer, _ = extractor(data)

    print("Answer:", answer)
