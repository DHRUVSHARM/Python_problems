from typing import List

"""

Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

[[1,3],[2,6],[8,10],[15,18]]


1    6
           8    10 
                        8    18

"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start time
        intervals.sort()

        s = [ intervals[0] ]

        # we can use stack and return it as the final output as a list 
        for index in range(1 , len(intervals)):
            start , end = intervals[index]
            if start > s[-1][1]:
                # non overlapping can be added safely
                s.append([start , end])
            else:
                # overlapping
                current_start , current_end = s.pop()
                # older start 
                s.append([current_start , max(end , current_end )])

        return s
        


