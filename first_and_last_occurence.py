class Solution:
    
    def first_occurence(self, nums , target):
        # ...TTTTFFFFFF...
        left , right = -1 , len(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        
        return right

    def last_occurence(self , nums , target):
        # ....TTTTTFFFFF....
        left , right = -1 , len(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        return left


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.first_occurence(nums , target)
        if first == len(nums) or nums[first] != target:
            # element does not exist 
            return [-1 , -1]
        last = self.last_occurence(nums , target)
        return [first , last]