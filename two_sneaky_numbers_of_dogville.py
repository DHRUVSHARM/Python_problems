from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        total_mask , non_repeating_mask , repeating_mask , partition_mask = 0 , 0 , 0 , 0
        for element in range(0 , len(nums) - 2):
            total_mask ^= element
        # print(total_mask)

        # gives non repeating elements
        for element in nums:
            non_repeating_mask ^= element

        # print(non_repeating_mask)

        # give repeating elements
        repeating_mask = non_repeating_mask ^ total_mask

         #print(repeating_mask)
        # need to get mask to parition based on lsb set
        # guaranteed diff since both elements are different
        # -ve adds 1 and to the complement, and adds 1 to fit to the first 0 pocket, if there are
        # initial ones then then that becomes 0 and carries to the left so we essentially
        # get a set bit at the first set bit , and the others to the right and after bit are same 
        # NOTE :& the -ve is equivalent of (~x + 1)
        partition_mask = repeating_mask & (-repeating_mask)
        # print(partition_mask)

        left , right = 0 , 0

        for element in nums:
            if element & partition_mask:
                left ^= element
            else:
                right ^= element 

        for element in range(0 , len(nums) - 2):
            if element & partition_mask:
                left ^= element
            else:
                right ^= element

        return [left , right]