class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sums = collections.defaultdict(int)
        prefix_sums[-1] = 0
        for index , element in enumerate(nums):
            prefix_sums[index] = element  +  prefix_sums[index - 1]
        
        # print(prefix_sums)
        
        pivot = -1
        for index in range(len(nums)):
            # print( prefix_sums[index - 1] , " " , prefix_sums[len(nums)-1] - prefix_sums[index])
            if (prefix_sums[index - 1]) == (prefix_sums[len(nums) - 1] - prefix_sums[index]):
                pivot = index
                break

        return pivot 