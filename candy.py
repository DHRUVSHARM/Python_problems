from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies_distributed = [1 for _ in range(0, len(ratings))]
        for index in range(1, len(ratings)):
            if ratings[index] > ratings[index - 1]:
                candies_distributed[index] = candies_distributed[index - 1] + 1

        # print("candies distributed : " , candies_distributed)

        for index in range(len(ratings) - 2, -1, -1):
            if ratings[index] > ratings[index + 1] and candies_distributed[index] <= candies_distributed[index + 1]:
                candies_distributed[index] = candies_distributed[index + 1] + 1
        # print("candies distributed : " , candies_distributed)

        return sum(candies_distributed)
