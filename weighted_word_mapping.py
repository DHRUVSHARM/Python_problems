from typing import List
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        reverse_map , ch = {} , 'a'

        for step in range(25 , -1 , -1):
            reverse_map[step] = ch
            ch = chr(ord(ch) + 1)
        
        
        # normal weights are simple index mapped 
        res = []
        for word in words:
            weight = 0
            for ch in word:
                weight += weights[(ord(ch) - ord('a'))]
            weight %= 26
            res.append(reverse_map[weight])
        
        return "".join(res)
    