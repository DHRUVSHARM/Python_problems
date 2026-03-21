from typing import List

"""
Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

For i <= k < j:
arr[k] > arr[k + 1] when k is odd, and
arr[k] < arr[k + 1] when k is even.
Or, for i <= k < j:
arr[k] > arr[k + 1] when k is even, and
arr[k] < arr[k + 1] when k is odd.
 

KEY OBSERVATIONS    
the order is fixed 

Example 1:

result = 1
greater = True


                l r
Input: arr = [9,4,2,10,7,8,8,1,9]



Output: 5
Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
Example 2:

Input: arr = [4,8,12,16]
Output: 2
Example 3:

Input: arr = [100]
Output: 1
 

"""

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return len(arr)
        
        result , greater , left = 1 , None , 0

        for r in range(1 , len(arr)):
            if arr[r] == arr[r- 1]:
                left = r
                greater = None
                continue
            
            if greater is None:
                greater = 1 if arr[r - 1] > arr[r] else 0

            if (greater and arr[r - 1] > arr[r]) or (not greater and arr[r - 1] < arr[r]):
                result = max(result , r - left + 1)
                greater ^= 1
            else:
                left = r - 1
                result = max(result , r - left + 1)
                greater = 1 if arr[left] > arr[r] else 0
                greater ^= 1

            # print("left : " , left , "r : " , r , "greater : " , greater)

        return result