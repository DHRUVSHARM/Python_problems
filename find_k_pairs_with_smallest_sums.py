from typing import List

import heapq 
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        minHeap , ans = [] , []

        # we will first put in all possible pairs with the first element 
        # basicallly from the first array , and the first element from second array 
        # pull out the minimal element and push the next choice by increasing the value in nums2 
        # since both arrays are sorted, we will get the minimal element and add the displaced pair from nums2 compare with 
        # what we have from the nums1 pair

        # pick the k smallest elements from first array 
        for index in range(0 , min(k , len(nums1))):
            heapq.heappush(minHeap , (nums1[index] + nums2[0] , index , 0))
        
        while len(minHeap) and len(ans) < k:
            s , i , j = heapq.heappop(minHeap)
            ans.append([nums1[i] , nums2[j]]) # put the minimal at this poin t
            # pop and put the next one in 
            if j + 1 < len(nums2):
                # we have a pair to add
                heapq.heappush(minHeap , (nums1[i] + nums2[j + 1] , i , j + 1))

        return ans