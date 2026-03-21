from typing import List

"""
    [2,1,5,6,2,3]

    [ (1 , 1) ,  (2 , 4) , (3 , 5)]  (0 , 6)      

    
    [5 , 5 ,5  ,5]  0
    # so no need to store repeats 
    
    0 , 3  ,2,  5


    [4,2,0,3,2,5]
    
    (4 , 0)     2 , 1

    [ (0 , 0) , (2 , 3) , (5 , 5) ] (-1 , 6)  


    4 , 4 , 3
    
2 * (1 - 0)
6 * (4 - 3)
10
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights , ans , s = heights + [-1] , 0 , []

        for index, h in enumerate(heights):
            
            last_popped_index = None
            while s and s[-1][0] > h:
                prev_height , prev_index = s.pop()
                ans = max(ans , prev_height * (index - prev_index))
                last_popped_index = prev_index
            # add if greater, not equal or if empty 
            # if empty
            # print("last_pooped : " , index, ": " , last_popped_index)
            index_to_push = last_popped_index if last_popped_index is not None else index
            if not s:
                s.append((h , index_to_push))
            else:
                if s[-1][0] < h:
                    s.append((h , index_to_push))

            
            # print(s)
        return ans
