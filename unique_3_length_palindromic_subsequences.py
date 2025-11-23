import collections


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left , right , ans , seen = collections.defaultdict(int) , collections.defaultdict(int) , 0 , set()   
        
        left[s[0]] += 1

        for index in range(2 , len(s)):
            right[s[index]] += 1

        def add_combinations(middle_element):
            # iterate over the combinations of letters
            ans , element = 0 , ord('a')
            for index in range(0 , 26):
                side_element = element + index
                side_char = chr(side_element)

                if side_char in left and side_char in right:
                    # print(side_char + middle_element + side_char)
                    seen.add(side_char + middle_element + side_char)
            


        for index in range(1 , len(s) - 1):
            # print("left , right : " , left , " " , right)
            add_combinations(s[index])
            right[s[index + 1]] -= 1
            if not right[s[index + 1]]:
                right.pop(s[index + 1])
            left[s[index]] += 1

        return len(seen)
    



if __name__ == '__main__':
    element = ord('a')
    print(chr(element))
    element += 2
    print(chr(element))
    element -= 2
    print(chr(element))
    element += 25
    print(chr(element))
    