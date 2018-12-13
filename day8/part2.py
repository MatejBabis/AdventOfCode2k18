import numpy as np
import part1


def extractor(input_data):
    sum = 0
    values = []

    n_children, metadata_entries = input_data[:2]
    payload = input_data[2:]

    # recursively iterate through children nodes
    for child in range(n_children):
        payload_sum, value, payload = extractor(payload)
        sum += payload_sum
        values.append(value)

    # when leaf node reached, add the accumulated value to the sum
    metadata = payload[:metadata_entries]
    sum += np.sum(metadata)

    if n_children > 0:
        # node's value constrained on part2 description
        child_value = 0
        for m in metadata:
            # ignore entries that do not exist or are 0
            if m <= len(values) and m != 0:
                child_value += values[m - 1]

        return sum, child_value, payload[metadata_entries:]
    else:
        # just like before
        return sum, np.sum(metadata), payload[metadata_entries:]


if __name__ == "__main__":
    data = part1.open_file("input.txt")

    _, answer, _ = extractor(data)

    print("Answer:", answer)
