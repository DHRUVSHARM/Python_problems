from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        ans = []

        def helper(target, subans, index):
            if target == 0:
                ans.append(subans.copy())
                return

            if index == len(candidates) or target < 0:
                return

            # include
            subans.append(candidates[index])
            helper(target - candidates[index], subans, index + 1)
            subans.pop()

            # exclude
            curr_index = index
            while (
                curr_index < len(candidates)
                and candidates[index] == candidates[curr_index]
            ):
                curr_index += 1

            index = curr_index

            helper(target, subans, index)

        helper(target, [], 0)

        return ans
