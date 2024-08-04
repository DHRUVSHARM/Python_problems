from typing import List
import collections


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        counter_target, counter_arr = collections.Counter(target), collections.Counter(
            arr
        )

        for k, v in counter_target.items():
            # print(k ,  " , " , v)
            if counter_arr[k] != v:
                return False

        return True
