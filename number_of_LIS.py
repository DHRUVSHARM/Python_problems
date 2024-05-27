from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
        we need to return the number of strictly LIS
        :param nums: ip
        :return: num LIS
        """
        # we will maintain 2 dp arrays
        # lis[i] = the length of the LIS ending at index i
        # frequency[i] = frequency of the LIS ending at index i

        lis = [0 for _ in range(0, len(nums) + 1)]
        frequency = [0 for _ in range(0, len(nums) + 1)]

        frequency[0] = 1  # empty sequence frequency is 1
        maximal_lis_length = 0

        for index in range(1, len(lis)):
            max_length, frontier, j = 0, nums[index - 1], index - 1
            while j > 0:
                if frontier > nums[j - 1]:
                    max_length = max(max_length, lis[j])
                j -= 1
            lis[index] = max_length + 1

            # we need to update the frequency
            j = index - 1
            while j > 0:
                if lis[j] == lis[index] - 1 and frontier > nums[j - 1]:
                    frequency[index] += frequency[j]
                j -= 1

            if lis[j] == lis[index] - 1:
                # for empty
                frequency[index] += frequency[j]

            maximal_lis_length = max(maximal_lis_length, lis[index])

        result = 0
        for index in range(len(frequency)):
            if lis[index] == maximal_lis_length:
                result += frequency[index]

        return result
