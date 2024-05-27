import itertools
from heapq import *

if __name__ == '__main__':
    h = []
    # we maintain priorities and insertion counts to break ties
    # entry counts are useful to break ties when the priorities are the same for 2 tasks
    """
    heappush(h, (5, 1, 'write code'))
    heappush(h, (7, 2, 'release product'))
    heappush(h, (1, 3, 'write spec'))
    heappush(h, (3, 4, 'create tests'))
    heappush(h, (3, 5, 'create tests'))

    while len(h):
        print(heappop(h))
    """
    # we need to change the priority of an element, and also remove it if required

    # ******************************  *****************************************************

    pq = []  # list of entries arranged in a heap
    # basic array for heap
    entry_finder = {}  # mapping of tasks to entries
    # maps the task label -> [priority , adding order , task label]
    REMOVED = '<removed-task>'  # placeholder for a removed task
    counter = itertools.count()  # unique sequence count, breaks ties if tasks are different but
    # the priorities given are the same


    def add_task(task, priority=0):
        """Add a new task or update the priority of an existing task
            default priority given is 0
        """
        if task in entry_finder:
            # we are trying to change the priority of the element
            remove_task(task)
        # now we are sure that the task is entered with a unique priority
        count = next(counter)
        # this keeps track of the insertion order
        entry = [priority, count, task]
        entry_finder[task] = entry
        heappush(pq, entry)


    def remove_task(task):
        """Mark an existing task as REMOVED.  Raise KeyError if not found."""
        # note that only marking is done , for this we remove the key from the dictionary that
        # keeps track of entries
        entry = entry_finder.pop(task)
        # note that every entry value is of the form [ , , ] where last element is the task label
        entry[-1] = REMOVED


    def pop_task():
        """Remove and return the lowest priority task. Raise KeyError if empty."""
        while pq:
            priority, count, task = heappop(pq)
            if task is not REMOVED:
                del entry_finder[task]
                # deleting key but not returning anything
                return task
        # raise KeyError('pop from an empty priority queue')
        # means that the queue is empty
        return None

    print(entry_finder)
    # print(pq)
    add_task("Eat", 10)
    print(entry_finder)
    # print(pq)
    add_task("sleep", 1)
    print(entry_finder)
    # print(pq)
    add_task("Eat", 100)
    print(entry_finder)
    # print(pq)
    add_task("Eat", 3)
    print(entry_finder)
    # print(pq)
    add_task("Eat", -100)
    print(entry_finder)
    # print(pq)
    add_task("play", 1)
    # print(pq)

    # priority changed
    print(pop_task())
    print(entry_finder)
    print(pop_task())
    print(entry_finder)
    print(pop_task())
    print(entry_finder)

    # to get over the limitation of only being able to put in distinct elements we can
    # make task a tuple
