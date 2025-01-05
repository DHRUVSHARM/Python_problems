import collections


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left , right = {element : 0 for element in range(0 , 26)} , {element : 0 for element in range(0 , 26)}
        for element in s:
            right[ord(element) - ord('a')] += 1
        # we count the total number which can be fixed if the middle element is fixed
        ans = 0

        # we can start with the second element
        left[ord(s[0]) - ord('a')] += 1
        right[ord(s[0]) - ord('a')] -= 1

        # we need to keep a set as well
        seen = set()

        for index in range(1 , len(s)):
            element = ord(s[index]) - ord('a')
            right[element] -= 1

            # print(left , "\n" , right , "\n\n")


            # calc
            for i in range(0 , 26):
                # if we can find similar chars on either side we can incrememnt by one
                if left[i] > 0 and right[i] > 0:
                    if (i , element) not in seen:
                        ans += 1
                        # print(i , "|" , element)
                        seen.add((i , element))
            
            # print("ans : " , ans)

            left[element] += 1

        return ans  