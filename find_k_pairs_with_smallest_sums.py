from typing import List


"""
You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

i                   min

j


Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
"""

import heapq 
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        minHeap = []

        for index in range(0 , min(len(nums1) , k)):
            heapq.heappush(minHeap , (nums1[index] + nums2[0], index, 0))
        
        res = []

        while k:
            _ , i , j = heapq.heappop(minHeap)
            res.append([nums1[i] , nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(minHeap , (nums1[i] + nums2[j + 1] , i , j + 1))
            k -= 1

        return res





