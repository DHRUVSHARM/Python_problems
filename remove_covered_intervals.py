from typing import List

"""

Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

Return the number of remaining intervals.

c                          d
        a           b

        
            e   f
  c    d    
a   b

        3                       6
    2                                           8
1           4
"""

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        st = []
        for s , e in intervals:
            # first we need to remove all for which the incoming will cover
            while len(st) and s <= st[-1][0] and e >= st[-1][1]:
                st.pop()

            # then check, since now we have not for both or , so can be the case that the incoming is completely covered
            if len(st) and st[-1][0] <= s and st[-1][1] >= e:
                pass
            else:
                st.append([s , e])
        
        return len(st)