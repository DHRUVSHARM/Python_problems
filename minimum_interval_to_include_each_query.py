import heapq
from typing import List

if __name__ == '__main__':
    # we will need to understand heaps (priority queue) in depth
    # using tuples first smallest removed first , followed by the second element
    minHeap = []
    heapq.heappush(minHeap, (1, 1))
    heapq.heappush(minHeap, (1, 4))
    heapq.heappush(minHeap, (1, 3))
    heapq.heappush(minHeap, (1, 2))
    while len(minHeap):
        print(heapq.heappop(minHeap))

    arr = [1, 2, 3, 4, 5]
    # useful if all you need is the array sorted for a loop
    for element in sorted(arr, reverse=True):
        print(element)

    print(arr)

    # custom comaprator
    """
    def compare(item1, item2):
        if fitness(item1) < fitness(item2):
            return -1
        elif fitness(item1) > fitness(item2):
            return 1
        else:
            return 0


    # Calling
    list.sort(key=compare)
    """

    a = [[4, 4], [3, 2], [1, 2]]
    a.sort()
    print(a)


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervalSize = {}
        # mapping
        # default sort is by the first element
        intervals.sort()
        i, minHeap = 0, []
        for query in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= query:
                l, r = intervals[i][0], intervals[i][1]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1
            while len(minHeap) and minHeap[0][1] < query:
                heapq.heappop(minHeap)
            intervalSize[query] = -1 if not len(minHeap) else minHeap[0][0]

        return [intervalSize[query] for query in queries]