from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result , space_index = [" " for _ in range(0 , len(s) + len(spaces))] , 0
        for i in range(0 , len(s)):
            if space_index < len(spaces) and spaces[space_index] == i:
                result[i + space_index + 1] = s[i]
                space_index += 1
            else:
                result[i + space_index] = s[i]
        
        return "".join(result)