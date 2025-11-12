from typing import List 

class Solution:

    def gcd(self , a , b):
        # note a >= b for this to work 
        if b == 0:
            return a
        return self.gcd(b , a%b)

    def minOperations(self, nums: List[int]) -> int:
        # if we have atleast 1 or running gcd is never one we can ans
        running_gcd , is_one = nums[0] , False
        is_one = True if nums[0] == 1 else False

        for i in range(1 , len(nums)):
            if nums[i] == 1:
                is_one = True
                break
            running_gcd = self.gcd(max(running_gcd , nums[i]) , min(running_gcd , nums[i]))
            
        # print("len : " , len(nums))
        # print("nums count : " , nums.count(1))

        if is_one:
            # print("nums count : " , nums.count(1))
            return len(nums) - nums.count(1)
        
        if running_gcd != 1:
            return -1
        
        min_len = float("inf")
        for i in range(0 , len(nums)):
            running_gcd = nums[i]
            for j in range(i + 1 , len(nums)):
                running_gcd = self.gcd(max(running_gcd , nums[j]) , min(running_gcd , nums[j]))
                if running_gcd == 1:
                    min_len = min(min_len , j - i + 1)

        # print("min len : " , min_len)        
        return min_len - 1 + len(nums) - 1

