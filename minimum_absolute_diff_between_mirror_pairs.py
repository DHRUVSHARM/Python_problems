from typing import List
class Solution:
    
    def reverse(self, num):
        # 1 <= nums[i] <= 109​​​​​​​
        result = 0
        while num // 10:
            result = (result + num%10) * 10
            num = num // 10
        
        result += num
        return result


    def minMirrorPairDistance(self, nums: List[int]) -> int:
        last_seen , result = {} , float("inf")

        for index in range(len(nums) - 1, -1 , -1):
            element = nums[index]
            reversed_num = self.reverse(element)

            if reversed_num in last_seen:
                result = min(result, last_seen[reversed_num] - index)
            
            last_seen[element] = index
        
        return -1 if result == float("inf") else result