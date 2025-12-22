from typing import List


# new_element = chr(ord('a') + 1)
# this is the way to increment a character and we will use this for the problem
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # first we need to create a list of the keys
        prefix_sums = [0 for _ in range(0 , len(s) + 1)]
        for start , end , direction in shifts:
            if direction == 0:
                prefix_sums[end + 1] -= 1
                prefix_sums[start] += 1
            else:
                prefix_sums[start] -= 1
                prefix_sums[end + 1] += 1

        index , cum_sum = len(s) , 0
        cum_sum = (cum_sum + prefix_sums[index])
        index -= 1

        ordinals = [ord(element) - ord('a') for element in s]


        def modular_addition(a , b , m):
            ans = a + b
            while not (0 <= ans < m):
                if ans < 0:
                    ans += m
                else:
                    ans -= m
            return ans

        while index >= 0:

            # only works because we are in python
            # ordinals[index] = (ordinals[index] + cum_sum + 26) % 26
            
            # trying by writing something of my own , to make it run for other languages
            ordinals[index] = modular_addition(ordinals[index] , cum_sum , 26)
            
            cum_sum = cum_sum + prefix_sums[index]
            index -= 1

        return "".join([chr(element + ord('a')) for element in ordinals])