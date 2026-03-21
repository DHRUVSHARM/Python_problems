"""



Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]


0 1
    1
0

Output: 6

"""

from typing import List, Optional
class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height) <= 1:
            # cannot trap any water
            return 0
        
        lmh , rmh , left, right , ans = height[0] , height[-1] , 0 , len(height) - 1 , 0

        while left <= right:
            # we can move the less one always since the one on the other side is already greater and will only be greater further and we 
            # need the min only 
            lmh = max(lmh , height[left])
            rmh = max(rmh , height[right])

            if lmh <= rmh:
                ans += max(0 , lmh  - height[left])
                left += 1
                
            else:
                ans +=  max(0 , rmh - height[right])
                right -= 1
                

        # print("lmh : " , lmh)
        # print("rmh : " , rmh)
        return ans
