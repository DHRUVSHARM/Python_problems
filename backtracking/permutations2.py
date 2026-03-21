from typing import List

"""
Input: nums = [1,1,2]


1 1 2
1 2 1



Output: [
    [1,1,2],
    [1,2,1],
    [2,1,1]
]


1: 
2 :1

1:2
2:1

   _1_2_


   112
   121
   211


   
   1112
   1121
   2111


 1          1: 2
            2 : 1


 1 ,         1 ,         2
                                [2]
1 1 2        1_2_                     
            

1 2 1        2 1_ 


             121
             211
             112
             211 no repeat
             121 no
             211 
             
             
             if repeating after last 1 only 
otherwise after 
1 1 2
1 2 1
2 1 1

1 1 2
1 2 1
1 2 1
1 2 1
2 1 1
2 1 1

2 1 1
1 2 1
1 1 2
 

1 ,            2 ,                 3
               [_2 _3_]              [3]
               [_3_ 2_]

123
213
231
               

permutations 
1 1 2


1 2 3 4




    i           j     
1 2 4 | 3 4 7 1 2  

find first
ind = i - 1 , where i-1 < i from right 

    ind   j 
1 4 5   8 7 3 2 1
    
    ind   j
1 4 7   8 5 3 2 1

147 81235

145 87321
147 12358

now we need to revers so that we can be closer since now we are above so reduction required 

edge cases 

# none greater  ?
 ind j
1 4         7 4 4 3 2 1

1 7         1 2 3 4 4 4


need to find the smallest that we can move to 

  i     j
1 1     2
1 1     2



1 1 2
1 2 1
2 1 1


2 2 2 2 


1 2 3 4
1 2 4 3
1 3 2 4

1 2 3 4
1 4 3 2 -> 1 2 3 4


1 2 3 4
1 2 4 3
1 3 2 4
1 3 4 2


1 2 3
1 3 2

2 1 3
2 3 1

3 1 2
3 2 1


"""
import collections
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = collections.defaultdict(list)
        
        for index in range(len(nums) -1 , -1 , -1):
            # [1 2 3]
            #    index
            #    [ [2 , 3] , [3 , 2] ]

            if (index + 1) == len(nums):
                result[index].append( [nums[index]] )

            else:
                seen = set()
                for perm in result[index + 1]:
                    # handle for non repeating first 
                    # [2,3]
                    for i in range(0 , len(perm) + 1):
                        # simple set approach 
                        new_perm = perm[:i] + [nums[index]] + perm[i:]
                        new_perm_key = "".join([str(element) for element in new_perm])
                        if new_perm_key in seen:
                            continue
                        seen.add(new_perm_key)
                        # print("here : " , new_perm)
                        result[index].append(new_perm)
            # print(result)
        return result[0]