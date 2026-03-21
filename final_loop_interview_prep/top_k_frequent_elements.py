"""

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2, 1,2 ,1,2, 3,1,3,2], k = 2

Output: [1,2]
1,2,3         1,2,3     1,2   1,2             
1           2           3       4       5 



k = 2 , 1 , 2
k = 3, 1 , 2 , 4

set 



# assign meemory to the cache, 
# [1 , len(nums)]
# [1 , 10**5]

# iinear complexity 

1 : 3
2 : 2
3 : 1




"""

from typing import List
import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets , result , freq = [[] for _ in range(len(nums) + 1)] , set() , collections.defaultdict(int)
        
        for element in nums:
            freq[element] += 1
            buckets[freq[element]].append(element)
        

        for i in range(len(buckets) - 1 , -1 , -1):
            for j in range(len(buckets[i]) - 1 , -1 , -1):
                if buckets[i][j] not in result:
                    result.add(buckets[i][j])
                    if len(result) == k:
                        return list(result)

        return list(result)

         
