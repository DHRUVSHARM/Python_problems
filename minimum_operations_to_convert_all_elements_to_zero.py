from typing import List 

# this problem uses the monotonic stack 
# note that the smallest element size can be 0
# these function as holes
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack , ans = [] , 0

        for element in nums:
            # first step will be to pop out the unwanted elements
            while stack and stack[-1] > element:
                # we can remove the elements since there intervals have been accounted for 
                stack.pop()
            
            # at this point it is either empty or there is some top element 
            if (stack and stack[-1] != element) or (not stack):
                ans += 1 if element else 0

            stack.append(element)
                

        return ans