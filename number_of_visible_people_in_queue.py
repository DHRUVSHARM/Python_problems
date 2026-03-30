"""
There are n people standing in a queue,
 and they numbered from 0 to n - 1 
 in left to right order. 
 
 You are given an array heights of distinct integers where heights[i] represents the height of the ith person.

A person can see another person 
to their right in the queue if everybody in between is shorter than both of them. More formally, 

the ith person can see the jth person 

if i < j 

min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1]).

Return an array answer of length n where answer[i] is the number of people the ith person can see to their right in the queue.


Input: heights = [10,6,8,5,11,9]
Output: [3,1,2,1,1,0]

11 , 9   


10  , 4 , 2 , 1 , 8

10 can see 4 but not 1 

[10 , ]    

result
10: 3
6: 1
8: 2
5: 1
11: 1
9: 0


all values of height is unique so we can keep a hashmap 
"""

from typing import List
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        result , s = [0 for _ in range(len(heights))] , []

        for index, h in enumerate(heights):
            while len(s) and s[-1][0] < h:
                # pop and consider
                # every pop means that the incoming is the highest it will see so consider 
                result[s[-1][1]] += 1
                s.pop()
            
            # increment the frontier if exists since this is the first time the element will come near it 
            if len(s):
                result[s[-1][1]] += 1
            # add the element , index
            s.append((h , index))

        return result