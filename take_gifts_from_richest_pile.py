import heapq
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        result = sum(gifts)
        maxHeap = [-1 * element for element in gifts]
        heapq.heapify(maxHeap)

        def square_root(number):
            left , right = 0 , 10**5 + 1
            # ....ttttfffff....
            while left + 1  < right:
                mid = (left + right) // 2
                if mid * mid <= number:
                    left = mid
                else:
                    right = mid
            return left
        
        while len(maxHeap) and k:
            maximal_element = -1 * heapq.heappop(maxHeap)
            root = square_root(maximal_element)
            result = result - maximal_element + root
            heapq.heappush(maxHeap , -1 * root)
            k -= 1

        return result