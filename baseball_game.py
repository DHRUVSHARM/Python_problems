from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        
        def get_base_10(nums:str)->int:
            result , multiplier = 0 , 1
            for c in reversed(nums):
                result += ((ord(c) - ord('0')) * multiplier)
                multiplier *= 10
            return result

        def get_integer(nums:str)->int:

            """
            if nums[0] == '-':
                return -1 * get_base_10(nums[1:])
            else:
                return get_base_10(nums)
            """
            # we can use builtin
            return int(nums)
        
        s , new_ops = [] , [get_integer(element) if element not in {'D', 'C' , '+'} else element for element in operations]

        # print(new_ops)

        for element in new_ops:
            if element == '+':
                nums1 = s.pop()
                nums2 = s.pop()
                s.extend([nums2 , nums1 , nums1 + nums2])
            elif element == 'C':
                nums1 = s.pop()
            elif element == 'D':
                nums1 = s.pop()
                s.extend([nums1 , 2 * nums1])
            else:
                # simple numeric ans
                s.append(element)
        

        return sum(s)