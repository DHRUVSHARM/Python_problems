from typing import List
class Solution:
    
    def gcd(self, a , b):
        
        while a:
            a , b = b % a , a

        return b


    def findGCD(self, nums: List[int]) -> int:
        minimal , maximal = min(nums) , max(nums)
        return self.gcd(minimal , maximal)