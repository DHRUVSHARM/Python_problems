from typing import List

"""
You are given a 0-indexed integer array nums. 
There exists an array arr of length nums.length, 
where arr[i] is the sum of |i - j| 
over all j such that nums[j] == nums[i] and j != i. If there is no such j, set arr[i] to be 0.

Return the array arr.

Example 1:
             0   2      
1   :       [0 , 2 , 3]   
3   :       [1]
2   :       [4]   

               0 1 2 3 4
Input: nums = [1,3,1,1,2]


indices, 
[a0 , a1 , a2 , a3 , ...... , ak - 1]

res[i] = (ai - a0) + (ai - a1) + .... (ai - ai)  + (ai+1 - ai) + (ai+2 - ai) + ... (ak-1 - ai)

ai * (i - 1 - 0  + 1)   +   0             - ai * (k - 1 - i)
- (sum of left indices)                    + (sum of right indices) 

----------------------------------------------------------------------------------------------------------
i : cnt (0 based) , ai:index exact one 
k : total count of indices 

res[ai] = ai * (i) - (sum of left indices) + (sum of right indices)  -ai*(k - 1 - i)
                    ind_prefix[i - 1]       + ind_prefix[-1] - ind_prefix[i]

               0 1 2 3 4
Input: nums = [1,3,1,1,2]

1 : [0 , 2 , 3]
    [0   2   5] index sum 

    0 * 0 - 0 + 5 - 0(3 - 1 - 0) = 5
    2 * 1 - 0 + 3 - 2(3 - 1 - 1) = 3 
    3 * 2 - 2 + 0 - 3*(3 - 1 - 2) = 4

2 : [4]
    [4] index sum

    4*0 - 0 + 0 - 4(1 - 1 - 0) = 0


"""

import collections
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        element_index_map , result = collections.defaultdict(list) , [0 for _ in range(len(nums))]

        for index, element in enumerate(nums):
            # map the element to the index, index prefix sum 
            if len(element_index_map[element]) == 0:
                element_index_map[element].append((index, index))
            else:
                _ , prefix = element_index_map[element][-1]
                element_index_map[element].append((index , prefix + index))
        
        
        
        for element in element_index_map.keys():
            """
            
                    res[ai] = ai * (i) - (sum of left indices) + (sum of right indices)  -ai*(k - 1 - i)
                    ind_prefix[i - 1]       + ind_prefix[-1] - ind_prefix[i]
            """
            # print("element : " , element)
            # print("indices : " , element_index_map[element])
            # print("-------------------------------------------------")
            
            indices = element_index_map[element]
            for index, element in enumerate(indices):
                ind , ind_prefix = element
                result[ind] = ind * index - (indices[index - 1][1] if (index - 1 >= 0) else 0) + (indices[-1][1] - ind_prefix) - ind*(len(indices) - 1 - index)

        return result
