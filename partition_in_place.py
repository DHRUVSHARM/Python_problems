from typing import List

# [9,12,5,10,14,3,10]
# in place pivot partition code
# will not respect relative order if we do this hence quicksort unstable using this version 

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        left , right = -1 , -1

        for index in range(0 , len(nums)):

            if nums[index] < pivot:
                left += 1 # increase boundary
                nums[left] , nums[index] = nums[index] , nums[left] 

                if right == -1:
                    right = index

                if nums[index] == pivot:
                    nums[index] , nums[right] = nums[right] , nums[index]
                    right += 1
                else:
                    # just keep it there at the end
                    # increase right to account for push 
                    right += 1
             
            elif nums[index] > pivot:
                if right == -1:
                    right = index
                else:
                    pass
                    # just keep moving
            else:
                if right == -1:
                    right = index 
                nums[index] , nums[right] = nums[right] , nums[index]
                right += 1


        return nums
        




if __name__ == '__main__':
    s = Solution()
    pivot = 10
    arr = [
        [9,12,5,10,14,3,10],

        [10, 10, 10, 10, 17 , 20 , 2 , 6 , 10],
        [2 , 3 , 4 , 5 , 6 , 20 , 40 , 50 , 10 , 10],
        [20 , 30 , 40 , 40 , 50 , 70 , 2 , 3 , 5 ],
        [2 , 3 , 4 , 5, 100 , 200 , 400],
        [10 , 10],
        [2 , 3, 4],
        [100 , 200 , 400],
        [100 ,200,400, 1],
        [100 ,200,400, 1 , 10],
    ]

    for input in arr:
        print(s.pivotArray(input , pivot))