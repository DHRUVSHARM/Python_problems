import heapq


def get_min_machines(start=None, end=None):
    if end is None:
        end = [7, 9, 6, 14, 7]
    if start is None:
        start = [1, 8, 3, 9, 6]

    times = [e for e in zip(start, end)]
    # sort by start time
    times.sort()

    max_machines, minHeap = 0, []

    for s, e in times:
        if len(minHeap) and minHeap[0][0] < s:
            # can use existing machine
            heapq.heappop(minHeap)
            heapq.heappush(minHeap, (e, s))
        else:
            # have to use a new machine
            heapq.heappush(minHeap, (e, s))
        max_machines = max(
            max_machines,
            len(minHeap)
        )

    print(max_machines)


if __name__ == '__main__':
    get_min_machines()
