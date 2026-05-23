from typing import List
class Solution:
    def check(self, nums: List[int]) -> bool:
        """
        6 5 4 3 2 1 0 -1

        2 1 0 -1 | 6 5 4 3

        0 -1 | 6 5 4 3 | 2 1

        4 3 |  2 1 0 -1 | 6 5
        
        hypothesise, at most one point of deflection from decreasung that is increase point 
        will check rotation 
        for sorted there have to be 2 decreasing seq 
        so checking 2 dec seq will work -> for rotate sort,
        else one single ok  

        3 4 5 1 2

        1 2 3 4 5 

        4 5 | 1 2 3 
        

        3 4 5 | 1 2
        
        """
        
        seq = []
        sub = []

        frontier = float("-inf")
        for element in nums:
            if element >= frontier:
                sub.append(element)
                frontier = element
            else:
                seq.append(sub)
                sub = [element]
                frontier = element
        
        # check in last if anything left
        if len(sub) != 0:
            seq.append(sub)

        # print(seq)

        if len(seq) == 1:
            return True
        elif len(seq) == 2:
            if seq[1][-1] <= seq[0][0]:
                
                return True
            else: return False
        else:
            return False