from typing import List

# convert to intervals + traversal question 
"""
[[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]


sx   sy
1,  0  bottom left 
ex   ey
5,  2  top right 


sx , ex -> interval in x, horizontal direction 
sy , ey -> interval in y, vertical direction 




0 , 2       2 , 4       2 , 3       4 , 5


0           2
            2               3
            2                       4  
                                    4           5
"""

# 0 , 2       if x , y  if x > 

class Solution:

    def helper(self, intervals):
        # check if we can make atleast 2 cuts else false
        cuts = 0
        # size of the intervals set will always be 1 atleast
        s , e = intervals[0][0] , intervals[0][1]
        index = 1

        while index < len(intervals):
            fs , fe = intervals[index]
            if fs >= e:
                # can make a cut and reset
                cuts += 1
                if cuts == 2:
                    return True
                s , e = fs , fe # reset 
            else:
                # fs < e but will be >= s since sorted 
                s , e = min(fs , s) , max(fe , e)
            
            index += 1

        return False


    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # convert to intervals on both dimensions
        # find the number of non overlapping intervals, and check if we can make 2 cuts in either dimension 
        x_dir , y_dir = [] , []
        for sx , sy , ex, ey in rectangles:
            x_dir.append([sx , ex])
            y_dir.append([sy , ey])
    
        x_dir.sort()
        y_dir.sort()

        return self.helper(x_dir) or self.helper(y_dir)
