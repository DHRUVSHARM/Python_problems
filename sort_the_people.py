from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        result = []
        for height, name in sorted(zip(heights, names), reverse=True):
            result.append(name)

        return result
