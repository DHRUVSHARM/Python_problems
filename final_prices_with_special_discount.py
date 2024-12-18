from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # monotonic stack , if increasing elements kept means we have not found any next smaller or equal element 
        s , ans = [
            (prices[0] , 0)
             ] , [element for element in prices]
        
        for index in range(1 , len(prices)):
            while len(s) and s[-1][0] >= prices[index]:
                ans[s[-1][1]] -= prices[index]
                s.pop()
            s.append((prices[index] , index))

        return ans