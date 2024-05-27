import collections
import heapq
from typing import List

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]
    n = len(arr)
    # arr.insert(0, 100)
    print(arr)
    arr.insert(n - 1, 100)
    print(arr)

    a = [[1, 2], [4, 3], [-1, 3]]
    a.sort(key=lambda x: x[1])
    print(a)

    m = [[3, 1], [1, 2], [2, 2], [3, 2], [1, 1]]
    m.sort(key=lambda interval: (interval[0], -1 * interval[1]))
    print(m)

    print("talking about custom style heaps")
    h = []
    heapq.heappush(h, (5, 'write code'))
    heapq.heappush(h, (7, 'release product'))
    heapq.heappush(h, (1, 'write spec'))
    heapq.heappush(h, (1, 'zzzzzzzz'))
    heapq.heappush(h, (3, 'create tests'))
    print(heapq.heappop(h))
    print(heapq.heappop(h))

# interesting problem where we insert an interval and maintain the non overlapping,
# start time ascending order nature of the original interval list
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals has non overlapping and start time ordered
        s = [newInterval]
        for start, end in intervals:
            # print(start , end)
            n_s, n_e = s.pop()
            if n_e < start:
                s.append([n_s, n_e])
                s.append([start , end])
            elif n_s > end:
                s.append([start , end])
                s.append([n_s, n_e])
            else:
                # overlap
                s.append([min(n_s, start), max(n_e, end)])
            # print(s)
        return s
"""

"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        s = [intervals[0]]
        for index in range(1, len(intervals)):
            start, end = s.pop()
            n_s, n_e = intervals[index]
            if n_s <= end:
                # overlap , need to merge
                s.append([min(start, n_s), max(end, n_e)])
            else:
                # non overlapping interval
                s.append([start, end])
                s.append([n_s, n_e])
        return s
"""

"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda interval: (interval[0], interval[1]))
        s = [intervals[0]]
        for index in range(1, len(intervals)):
            # for equal start time intervals , we get the lower start time first
            start, end = s.pop()
            n_s, n_e = intervals[index]

            if n_s >= end:
                # non overlap , and n_e is greater than or equal to end
                # put both inside
                s.append([start , end])
                s.append([n_s , n_e])
            else:
                # overlap , choose the lower end time always (greedy)
                if n_e < end:
                    s.append([n_s, n_e])
                else:
                    # no difference , put the thing back
                    s.append([start, end])

        return len(intervals) - len(s)
"""


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


"""
class Solution:
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True
        intervals.sort(key=lambda i: i.start)
        s = [intervals[0]]
        for index in range(1, len(intervals)):
            interval = s.pop()
            if intervals[index].start >= interval.end:
                s.append(interval)
                s.append(intervals[index])
            else:
                return False

        return True
"""

"""
class Solution:
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        # we need to find the minimal number of rooms to accommodate all events
        rooms = 0
        if len(intervals) == 0:
            return rooms

        # sorting by start time , and give priority to availability by end time
        # so that the fastest completing room is available to the incoming interval
        intervals.sort(key=lambda i: i.start)

        minHeap = []
        for index in range(0, len(intervals)):
            if not len(minHeap):
                # no available room , just accommodate
                heapq.heappush(minHeap, intervals[index].end)
            elif minHeap[0] <= intervals[index].start:
                # room can be used without conflict
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, intervals[index].end)
            else:
                # simple insert new room required
                heapq.heappush(minHeap, intervals[index].end)

            rooms = max(rooms, len(minHeap))

        return rooms
    """