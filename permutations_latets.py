from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = [
            [-20 for _ in range(len(nums))]
        ]  # -20 will be a placeholder that means empty
        curr_index = len(nums) - 1

        for levels in range(len(nums)):
            curr_ans = []
            for sub_ans in ans:
                for index in range(0, len(sub_ans)):
                    if sub_ans[index] == -20:
                        # empty
                        copied_sub_ans = sub_ans.copy()
                        copied_sub_ans[index] = nums[curr_index]
                        curr_ans.append(copied_sub_ans)
            ans = curr_ans
            # print("ans for this level is : ", ans)
            curr_index -= 1

        return ans
