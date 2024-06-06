import itertools
import sys
from heapq import *
from typing import List


def parse():
    arrays = []
    for line in sys.stdin:
        # print(line, end="")
        arrays.append(line.strip().split(","))
    return arrays


class lazy_heap:
    __slots__ = "pq", "entry_finder", "REMOVED", "counter"

    def __init__(self):
        """
        initializes the pq, we always begin with empty heap
        """
        self.pq = []
        # list of entries arranged in a heap , basic array for heap

        self.entry_finder = {}
        # maps the task label -> [priority , adding order , task label]

        self.REMOVED = "<removed-task>"
        # placeholder for a removed task

        self.counter = itertools.count()
        # unique sequence count, breaks ties if tasks are different but the priorities given are the same

    # functions for use
    def add_task(self, task, priority=0):
        """Add a new task or update the priority of an existing task
        default priority given is 0
        """
        if task in self.entry_finder:
            # we are trying to change the priority of the element
            self.remove_task(task)
        # now we are sure that the task is entered with a unique priority
        count = next(self.counter)
        # this keeps track of the insertion order
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)

    def remove_task(self, task):
        """Mark an existing task as REMOVED.  Raise KeyError if not found."""
        # note that only marking is done , for this we remove the key from the dictionary that
        # keeps track of entries
        if task in self.entry_finder:
            entry = self.entry_finder.pop(task)
            # note that every entry value is of the form [ , , ] where last element is the task label
            entry[-1] = self.REMOVED

    def pop_task(self):
        """Remove and return the lowest priority task. Raise KeyError if empty."""
        while self.pq:
            priority, count, task = heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                # deleting first non remove marked key but not returning anything
                return task
        raise KeyError("pop from an empty priority queue")
        # means that the queue is empty

    def peek(self):
        """return the lowest priority task. Raise KeyError if empty."""
        while self.pq:
            if self.pq[0][2] is self.REMOVED:
                # ignore and pop
                heappop(self.pq)
            else:
                return self.pq[0][2]
        raise KeyError("peek from an empty priority queue")
        # means that the queue is empty

    def get_size(self):
        return len(self.entry_finder)


def medianSlidingWindow(nums: List[int], k: int) -> List[int]:
    # we will need to keep to heaps which can support the delete operation
    small = lazy_heap()  # maxHeap
    large = lazy_heap()  # minHeap

    def addNum(index) -> None:

        small.add_task(index, -1 * nums[index])
        # task always added to small

        if (
            small.get_size()
            and large.get_size()
            and (nums[small.peek()]) > nums[large.peek()]
        ):
            t_index = small.pop_task()
            # print("top index : " , t_index)
            large.add_task(t_index, nums[t_index])

        if small.get_size() > large.get_size() + 1:
            # pop small move to large
            t_index = small.pop_task()
            # print("top index : " , t_index)
            large.add_task(t_index, nums[t_index])

        elif large.get_size() > small.get_size() + 1:
            # pop large move to small
            t_index = large.pop_task()
            # print("top index : " , t_index)
            small.add_task(t_index, -1 * nums[t_index])

    def findMedian() -> float:
        """
        find the median
        :return: median of stream
        """
        # print(small.get_size() , "**" , large.get_size())
        # print(small.pq , " ** " , large.pq)

        if abs(small.get_size() - large.get_size()) == 1:
            # odd sized array, we know size would be atleast 1
            if large.get_size() > small.get_size():
                return nums[large.peek()]
            else:
                return nums[small.peek()]

    result, start, end = [], 0, 0
    while end - start + 1 <= k:
        addNum(end)
        # print(small.get_size() , "**" , large.get_size())
        # print(small.pq , " ** " , large.pq)
        end += 1
    result.append(findMedian())
    small.remove_task(start)
    large.remove_task(start)
    start += 1
    # print(start , end)

    while end < len(nums):
        addNum(end)
        end += 1
        result.append(findMedian())
        small.remove_task(start)
        large.remove_task(start)
        start += 1
        # print(start , end)

    return result


def helper(ip, w_size):
    return medianSlidingWindow(ip, w_size)


if __name__ == "__main__":
    arr = parse()
    w_size = int(arr[0][0])
    result = []
    for i in range(1, len(arr)):
        ip = []
        for j in range(0, len(arr[i])):
            ip.append(int(arr[i][j]))

        # print(ip)
        result = helper(ip, w_size)
        comma_separated_string = ", ".join(map(str, result))
        print(comma_separated_string)
