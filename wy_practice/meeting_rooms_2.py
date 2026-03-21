# meeting rooms 2
# premium problem 
"""

Given an array of meeting time interval objects 
consisting of start and end times 
[[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.

Note: (0,8),(8,10) is not considered a conflict at 8.

Example 1:

Input: intervals = [(0,40),(5,10),(15,20)]


ALGORITHM : sort by start time 


0               40 
   5  10 
          15 20

          give us the earliest end time 
op 2

0, 40  15 20 |
2
"""


from typing import List
import heapq

# Definition of Interval:

class Interval(object):
    def __init__(self, start, end):
        # start < end
        self.start = start
        self.end = end


"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # equal end and start are not conflict 
        rooms = float("-inf")
        intervals.sort( key= lambda element : (element.start , element.end) )
        meeting_rooms = []

        for interval in intervals:
            if meeting_rooms and meeting_rooms[0][0] <= interval.start:
                heapq.heappop(meeting_rooms)
            heapq.heappush(meeting_rooms , (interval.end , interval.start))
            rooms = max(rooms , len(meeting_rooms))
        
        return 0 if rooms == float("-inf") else rooms

