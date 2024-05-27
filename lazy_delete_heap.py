# class implemented for lazy heap deletion
import itertools
from heapq import *


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

        self.REMOVED = '<removed-task>'
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
        raise KeyError('pop from an empty priority queue')
        # means that the queue is empty

    def peek(self):
        """return the lowest priority task. Raise KeyError if empty."""
        while self.pq:
            if self.pq[0][2] is self.REMOVED:
                # ignore and pop
                heappop(self.pq)
            else:
                return self.pq[0][2]
        raise KeyError('peek from an empty priority queue')
        # means that the queue is empty

    def get_size(self):
        return len(self.entry_finder)


if __name__ == '__main__':

    d = {1 : "hello"}
    #d.pop(100)
    print(d)

    lazy_minHeap = lazy_heap()
    print(lazy_minHeap.entry_finder)
    # print(pq)
    lazy_minHeap.add_task("Eat", 10)
    print(lazy_minHeap.entry_finder)
    # print(pq)
    lazy_minHeap.add_task("sleep", 1)
    print(lazy_minHeap.entry_finder)
    # print(pq)
    lazy_minHeap.add_task("Eat", 100)
    print(lazy_minHeap.entry_finder)
    # print(pq)
    lazy_minHeap.add_task("Eat", 3)
    print(lazy_minHeap.entry_finder)
    # print(pq)
    lazy_minHeap.add_task("Eat", -100)
    print(lazy_minHeap.entry_finder)
    # print(pq)
    lazy_minHeap.add_task("play", 1)
    print(lazy_minHeap.entry_finder)

    """
    print(lazy_minHeap.pq)
    print(lazy_minHeap.real_heap_size)

    print("*************************************************************** \n")
    print(lazy_minHeap.pop_task())
    print(lazy_minHeap.pq)
    print(lazy_minHeap.real_heap_size)

    print("*************************************************************** \n")
    print(lazy_minHeap.pop_task())
    print(lazy_minHeap.pq)
    print(lazy_minHeap.real_heap_size)

    print("*************************************************************** \n")
    print(lazy_minHeap.pop_task())
    print(lazy_minHeap.pq)
    print(lazy_minHeap.real_heap_size)

    # print(pop_task())
    # print(entry_finder)
    # print(pop_task())
    # print(entry_finder)
    """

    while lazy_minHeap.get_size():
        print(lazy_minHeap.pop_task())
