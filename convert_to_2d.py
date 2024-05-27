import collections
from typing import List

if __name__ == '__main__':
    arr = [[] for _ in range(3)]
    print(arr)

    arr[0].extend([1, 2, 3, 4])
    arr[1].extend([1, 2])
    arr[2].extend([1])

    print(arr[0])

    c = collections.Counter(arr[0])
    print(c)


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = collections.Counter(nums)
        sorted_freq = [(value, key) for key, value in freq.items()]
        sorted_freq.sort(reverse=True)

        ans = [[] for _ in range(sorted_freq[0][0])]

        prev_freq, index, elements = sorted_freq[0][0], 0, []
        while index < len(sorted_freq):
            if sorted_freq[index][0] < prev_freq:
                for j in range(0, prev_freq):
                    ans[j].extend(elements)
                elements = []
                prev_freq = sorted_freq[index][0]

            elements.append(sorted_freq[index][1])
            index += 1

        for j in range(0, prev_freq):
            ans[j].extend(elements)

        return ans
