from typing import List
import random


class Solution:

    def __init__(self, w: List[int]):
        self.prefix_arr = [0]
        for element in w:
            self.prefix_arr.append(element + self.prefix_arr[-1])


    def pickIndex(self) -> int:
        target = random.random() * self.prefix_arr[-1]
        left , right = 0 , len(self.prefix_arr) - 1

        # TTTTTTTTFFFFFF 
        while left + 1 < right:
            mid = (left + right) // 2
            if self.prefix_arr[mid] <= target:
                left = mid
            else:
                right = mid
        
        return left







# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


while True:
    print(random.random())