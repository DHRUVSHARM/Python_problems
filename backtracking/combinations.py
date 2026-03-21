"""
Docstring for backtracking.combinations

Input: n = 3, k = 2

Output: [
    [1,2],
    [1,3],
    [2,3]
]

1 2 |_ stop
1 _ 3
_ 2 3

# combinations  =  (remaining 1 ) , skip 2 on ...

                                []
    [1] # start at 1 onwards          [2] # start at 2 onwards
  [2] [3]                           [3]

"""

from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        result = []
        def dfs(index , combination):
            # base cases 
            if len(combination) == k:
                result.append(combination.copy())
                return
            
            
            for element in range(index , n + 1):    
                # we put the element
                combination.append(element) # [1 , 2]
                # print(combination)
                dfs(element + 1 , combination) # [3 ...]
                combination.pop() 


        dfs(1 , [])
        return result

