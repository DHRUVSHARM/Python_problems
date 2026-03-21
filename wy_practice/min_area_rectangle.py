from typing import List

"""
[[1,1],[1,3],[3,1],[3,3],[2,2]

# sort by the x coordinate and y coordinate


1,1   2,2          

3 x 0 = 0

"""


from sortedcontainers import SortedDict
class Solution:

    def calculate_width(self, lower_row , upper_row)->int:
        if len(lower_row) <= 1 or len(upper_row) <= 1:
            return 0
        
        # print("lower row : " , lower_row)
        # print("upper row : " , upper_row)

        upper_row = set(upper_row)
        # we can do sliding window to keep it at linear time 


        ans , left = float("inf") , 0 
        for right in range(1 , len(lower_row)):
            while left < right and lower_row[left] not in upper_row:
                left += 1
            
            if left < right and lower_row[right] in upper_row:
                # can consider 
                ans = min(ans , lower_row[right] - lower_row[left])
                # we can move left to start from right 
                left = right
        


        return 0 if ans == float("inf") else ans



    def minAreaRect(self, points: List[List[int]]) -> int:
        result = float("inf")

        # first we will iterate through the points in sorted column order 
        # sort by first value, second value

        points.sort()
        # map rows to list of columns where the row level appeared 
        row_mapping = SortedDict()

        for col , row in points:
            if row not in row_mapping:
                row_mapping[row] = [] # empty list
            row_mapping[row].append(col)

        # we will now iterate over the keys in sorted order 
        # get the sorted row key list
        rows = row_mapping.keys()
        # print("rows : " , rows)
        for i in range(0 , len(rows)):
            for j in range(i + 1 ,len(rows)):
                # need to find the first row with non zero value
                # j : [1 ,  3]
                # i : [1  , 3]
                # print(rows[i] , " " , rows[j])
                height = rows[j] - rows[i] 
            
                width = self.calculate_width(row_mapping[rows[i]] , row_mapping[rows[j]])
                if width:
                    result = min(result , height * width)

            
        # print(row_mapping)

        return 0 if result == float("inf") else result