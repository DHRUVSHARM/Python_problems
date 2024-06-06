from typing import List

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]

    for i in range(0, len(arr), 1):
        print(arr[i])

    print("********************************************")

    for i in range(0, len(arr), 3):
        print(arr[i])

    print("********************************************")

    for i in range(len(arr) - 1, -1, -1):
        print(arr[i])

    print("********************************************")

    for i in range(len(arr) - 1, -1, -2):
        print(arr[i])

    print("********************************************")


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ans, prefix, suffix = (
            [],
            [0 for _ in range(0, len(nums))],
            [0 for _ in range(0, len(nums))],
        )

        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i]

        suffix[-1] = nums[-1]
        for j in range(len(nums) - 2, -1, -1):
            suffix[j] = suffix[j + 1] + nums[j]

        for index in range(0, len(nums)):
            if index == 0:
                ans.append(suffix[index] - (len(nums) * nums[index]))
            elif index == len(nums) - 1:
                ans.append((len(nums) * nums[index]) - (prefix[index]))
            else:
                ans.append(
                    ((index) * nums[index])
                    - prefix[index - 1]
                    - ((len(nums) - index) * nums[index])
                    + suffix[index]
                )

        return ans
