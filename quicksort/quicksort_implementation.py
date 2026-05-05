from typing import List
# quicksort implementation 
# Definition for a pair.

class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]: 
        """
        1 pick the last value as the pivot  
        2 <= left, [] | pivot,
        3 swap left + 1 , pivot element
        pivot = 4 
        [1 , 2 , 3 , 4 , 5 , 6 , 7]
         l
        """

        n = len(pairs)

        def helper(left, right):
            # print("left , right : " , left,  " " , right)
            if right - left + 1 <= 1:
                return # single or overlap 
            
            # pick the last element 
            pivot , pivot_index = pairs[right].key , right
            index , less_index = left , left
            # print("to pivot : " , pivot)

            while index < pivot_index:
                # print("index : " , index)
                if pairs[index].key < pivot:
                    # print("here")
                    pairs[less_index] , pairs[index] = pairs[index] , pairs[less_index]
                    less_index += 1
                # greater keep moving
                index += 1

            # final swap , swap less_index, with pivot 
            # print("pivot on : " , less_index)
            # print("pivot index : " , pivot_index)
            pairs[less_index] , pairs[pivot_index] = pairs[pivot_index] , pairs[less_index] 
            # now the less_index has the pivot
            

            helper(left , less_index - 1)
            helper(less_index + 1, right)

        # sort in place 
        helper(0 , n - 1)

        return pairs