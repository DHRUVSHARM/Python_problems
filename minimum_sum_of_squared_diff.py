class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        """
        k1 for nums1        k2 for nums2 
        +1 k1 times on nums -> -1 k1 times on nums2 
        -1 k1 times on nums  -> +1 k1 times on nums2 

        +1/-1 k1 times on nums1 -> nums2
        +1/-1 k2 times on nums2 -> nums1 

        so actualy we have k1 + k2 +1/-1 ops which can be applied to any of the arrays 

        if we select a k and say we want diff == k
        THE subproblem could be to bring them as closer
        for that take the max and reduce it as much as possinle 
        think of the final answer as a series of squared terms

        FFFFFFFFFFTTTTTTTTTTT
        return R

        l =


        """
import collections

# using binary search (not recommended solution)
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        """
        apporach binary search 

        FFFFFFFF    TTTTTTTTT

        -1 : never possible
        max : always possible       
        """

        diff = [abs(x - y) for x , y in zip(nums1, nums2)]
        diff.sort() # keep sorted
        freq = collections.Counter(diff)

        # print("diff : " , diff)

        left, right = -1 , max(diff)

        def helper(target , k):
            # print(target)
            for key in sorted(freq.keys()):
                # print(key)
                if key <= target:
                    pass
                else:
                    if k >= (key - target) * freq[key]:
                        k -= ((key - target) * freq[key])
                    else:
                        return False
            return True  


        while left + 1 < right:
            mid = (left + right) // 2

            if helper(mid , k1 + k2):
                right = mid
            else:
                left = mid

        # right 
        # print("cap : " , right)
        ans = 0
        steps = k1 + k2

        # we know we can reduce each of these to right 
        # or less, we may have some remaining keys
        # which are to be applied to the 
        # we can modify the freq 
        # we can use the diff to make new freq 

        new_diff = collections.defaultdict(int)
        max_element = float("-inf")

        if right == 0:
            return 0 

        for element in diff:
            if element <= right:
                new_diff[element] += 1 # no steps needed
                max_element = max(max_element, element) 
            else:
                new_diff[right] += 1
                steps -= (element - right) # can always do this         
                max_element = max(max_element, right)

        new_diff[max_element] -= steps # use the remaining to reduce the count 
        # of the highest group currently
        new_diff[max_element - 1] += steps

        ans = sum([(k ** 2) * v for k , v in new_diff.items()])

        return ans


# apporach 1 merge intervals 
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        """
        k1 + k2 ops allowed 

        we can keep a map of the elements abs diff -> count 

        """

        k = k1 + k2
        elements = [abs(x - y) for x , y in zip(nums1, nums2)]
        freq = collections.Counter(elements)
        elements = list(set(elements))
        elements.sort()

        # print("elements : " , elements)

        while k and not (len(elements) == 1 and elements[-1] == 0):
            
            # print(elements)

            curr_diff = elements[-1] 
            curr_freq = freq[curr_diff]

            if k >= curr_freq:
                # interval will move down by 1
                k -= curr_freq
                freq[curr_diff - 1] += curr_freq
                freq.pop(curr_diff)
                elements.pop()

                if len(elements) and (elements[-1] == (curr_diff - 1)):
                    # merge intervals for next 
                    # freq is already merged 
                    pass
                else:
                    elements.append(curr_diff - 1)

            else:
                # cannot move not enough ops to reduce all occurrences of the current sq
                freq[curr_diff] -= k
                freq[curr_diff - 1] += k
                k = 0

        ans = sum([ (k ** 2) * v for k , v in freq.items() ])
        return ans