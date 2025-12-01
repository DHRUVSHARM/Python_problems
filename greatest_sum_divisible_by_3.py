from typing import List
import heapq

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        ans , curr_sum , ones, twos = 0 , sum(nums) , [] , []

        for element in nums:
            if element % 3 == 1:
                ones.append(element)
            elif element % 3 == 2:
                twos.append(element)


        heapq.heapify(ones)
        heapq.heapify(twos)

        # three possible cases 
        if curr_sum % 3 == 0:
            ans = curr_sum
        elif curr_sum % 3 == 1:
            # we can remove the minimal with remainder 1, or 2 minimal 2's 
            # mathematically atleast one of these options should be there in this case 
            if ones:
                ans = curr_sum - ones[0]
            if len(twos) > 1:
                element1 = heapq.heappop(twos)
                element2 = heapq.heappop(twos)
                ans = max(ans , curr_sum - element1 - element2)

        else:
            # we can remove the minimal with remainder 2, or 2 minimal 1's 
            if twos:
                ans = curr_sum - twos[0]
            if len(ones) > 1:
                element1 = heapq.heappop(ones)
                element2 = heapq.heappop(ones)
                ans = max(ans , curr_sum - element1 - element2)


        # return the answer
        return ans
