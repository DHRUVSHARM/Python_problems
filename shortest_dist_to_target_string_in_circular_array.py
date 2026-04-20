from typing import List

"""
                    l    i          r
Input: words = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1
Output: 1
Explanation: We start from index 1 and can reach "hello" by
- moving 3 units to the right to reach index 4.
- moving 2 units to the left to reach index 4.
- moving 4 units to the right to reach index 0.
- moving 1 unit to the left to reach index 0.
The shortest distance to reach "hello" is 1.


                        1   
                            2


Example 2:

Input: words = ["a","b","leetcode"], target = "leetcode", startIndex = 0
Output: 1
Explanation: We start from index 0 and can reach "leetcode" by
- moving 2 units to the right to reach index 2.
- moving 1 unit to the left to reach index 2.
The shortest distance to reach "leetcode" is 1.
Example 3:

Input: words = ["i","eat","leetcode"], target = "ate", startIndex = 0
Output: -1
Explanation: Since "ate" does not exist in words, we return -1.


         a
     llc      t b

(2 + x) - n = 0
     
0 - 2 + n = x

startindex - currindex + n -> distance from currindex from the other side of the loop
currindex - startindex -> distance we calculate

do over currindex in 


1 - 2 + 4

    i   st   
0   1   2 3


     """

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        result = float("inf")

        curr_index = startIndex
        for _ in range(0 , n):
            if words[curr_index] == target:
                result = min(
                    result,
                    max(curr_index , startIndex) - min(curr_index , startIndex),
                    min(curr_index , startIndex) - max(curr_index , startIndex) + n
                )
            
            curr_index = (curr_index + 1) % n

        return -1 if result == float("inf") else result
