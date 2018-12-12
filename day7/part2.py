import part1

STEP = 60
WORKERS = 5

def duration(n):
    return STEP + ord(n) - ord('A') + 1


if __name__ == "__main__":
    incoming_edges, outgoing_edges = part1.get_supporting_structures(
        "input.txt")

    # start by creating a list of where we can start (i.e. have no inward edges)
    queue = [k for k in outgoing_edges if incoming_edges[k] == []]
    # worker pool
    workers = [{"time": 0, "letter": None} for _ in range(WORKERS)]

    answer = ""
    clock = 0

    # loop while items are in queue or if a worker is processing
    while queue or len([w for w in workers if w["letter"] is not None]) > 0:
        for i, worker in enumerate(workers):
            # worker is about to finishing
            #   store its result and add new nodes to queue
            if worker["time"] == 1:
                answer += worker["letter"]
                for child in outgoing_edges[worker["letter"]]:
                    # neat way to check if all we have visited all nodes required
                    # to be able to proceed to this node
                    if set(incoming_edges[child]).issubset(set(answer)):
                        queue.append(child)
                # remove the node that was processed
                workers[i]["letter"] = None

            # decrement time for all workers processing
            if worker["time"] != 0:
                workers[i]["time"] = workers[i]["time"] - 1

        # distribute items in the queue to available workers
        for item in queue:
            for i, worker in enumerate(workers):
                if len(queue) > 0 and worker["time"] == 0:
                    vertex = queue[0]   # get the head
                    queue = queue[1:]
                    workers[i] = {"time": duration(vertex), "letter": vertex}

        clock += 1

    print("Answer:", answer)
    print("Time:", clock - 1)
