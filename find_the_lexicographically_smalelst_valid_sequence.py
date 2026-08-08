"""

"""
from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        i , j = 0 , 0
        m , n = len(word2) , len(word1) # to find the i , m in j , n

        # we can first find if it is possible to find the almost sequence 
        ans = []    # will be size m if exists  
        prefix = [n for _ in range(m)]
        suffix = [-1 for _ in range(m)]

        while i < m and j < n:
            if word2[i] == word1[j]:
                prefix[i] = j # store earlies match index for the prefix 
                i += 1
                j += 1
            else:
                j += 1

        i , j = m - 1 , n - 1
        while i >= 0 and j >= 0:
            if word2[i] == word1[j]:
                suffix[i] = j # store earliest suffix match index 
                i -= 1
                j -= 1
            else:
                j -= 1

        # print(prefix)
        # print(suffix)
        # print(prefix)

        swap_index = -1
        minimal_right = float("inf")
        left_selected = -1
        seen = False
        swapped = True

        for index in range(0 , m):
            left = prefix[index - 1] if index > 0 else -1
            right = suffix[index + 1] if index < m - 1 else n

            if right - left - 1 >= 1 and (n - right + 1) >= (m - index):
                # possible to change and enough elements remaining
                # for i in range(0 , index):
                    # ans.append(prefix[i]) # the ones before are correctly smallest lexicographically 
                # print("index : " , index , "right : " , right , "minimal_right : " , minimal_right)
                # if right < minimal_right:
                # if left + 1 < n and word2[index] == word1[left + 1]:
                    # swapped = True

                # minimal_right = right
                swap_index = index
                left_selected = left
                seen = True
                break
                    # print(swap_index)

        if not seen:
            return []

        for i in range(0 , swap_index):
            ans.append(prefix[i])
        # ans.append(left_selected + 1)
        # print("swap : " , swap_index)
        # we need to find for the suffix as well after the swap index
        i , j = swap_index , left_selected + 1
        # print(i , " : " , j)
        # print("i : " , i , " " , "j : " , j)
        while i < m and j < n:
            if word2[i] == word1[j] or swapped:
                if word2[i] != word1[j]:
                    swapped = False # only use if not equal 

                ans.append(j) # add the closest 
                i += 1
                j += 1
        
            else:
                
                j += 1

        return ans 

