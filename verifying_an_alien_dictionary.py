from typing import List
import collections

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # simple appproach 
        weights = collections.defaultdict(int)

        for index, element in enumerate(order):
            weights[element] = index


        def helper(w1 , w2):
            # check if w1 <= w2 lexicographically
            left , right = 0 , 0
            
            while left < len(w1) and right < len(w2):
                if weights[w1[left]] < weights[w2[right]]:
                    # we found a point where first element is less than the other side
                    return True
                elif weights[w1[left]] == weights[w2[right]]:
                    # equality, continue further
                    left += 1
                    right += 1
                else:
                    # return on first violation 
                    # order violation
                    return False

            if left == len(w1) and right == len(w2):
                # checked both means same element 
                return True
            
            if left == len(w1):
                return True
            
            if right == len(w2):
                return False
        
        sorted = True
        for index in range(1 , len(words)):
            sorted = sorted and helper(words[index - 1] , words[index])
            if not sorted:
                break


        return sorted