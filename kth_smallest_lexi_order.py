"""
Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

 

Example 1:

Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
Example 2:

Input: n = 1, k = 1
Output: 1
 

Constraints:

1 <= k <= n <= 109

problem can be solved with trie
max depth would be 9

""

1               ...     2   3           9

1 2 ..9

for each digit try to get the closest >= perdigit

k <= n so number will exist 
            i
        ex: 1072 

        ""
0   1   2   3   ... 9

1
    13
9^(remlen - 1) * (lastd)

    

    
            0 (n = 13)
    10              1           1       1           1
    1               2           3       4    ..     9
                
    


    9


            ""
        
    n =     1   3

    
    [  1    2   4   ]  


            1273

    1                       2

    


    1273
    
1273 % 1000 = 273

1273 //


123                12



12  19


                0
                ""

    1[274]              2[0]                ... 

11  12      19
    
"""

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        pass