import collections
from typing import List

if __name__ == "__main__":
    d = {1: 1, 2: 2, 3: 3, 5: 1, 6: 1}
    print(d)

    removed_keys = []
    for key, val in d.items():
        val -= 1
        d[key] -= 1
        if val == 0:
            removed_keys.append(key)

    print("removed keys : ", removed_keys)
    for k in removed_keys:
        d.pop(k)
    print(d)


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        frequency = collections.defaultdict(int)
        for index in range(0, len(nums)):
            frequency[nums[index]] += 1
            if len(frequency) > 2:
                removed_keys = []
                for key, val in frequency.items():
                    frequency[key] -= 1
                    if frequency[key] == 0:
                        removed_keys.append(key)
                for k in removed_keys:
                    frequency.pop(k)

        # print("frequency : " , frequency)

        if len(frequency) == 0:
            return []
        elif len(frequency) == 1:
            element = list(frequency.keys())[0]
            first, first_frequency = element, 0
            # print(first)
            for num in nums:
                if num == first:
                    first_frequency += 1
            # print(first_frequency)
            return [element] if first_frequency > len(nums) // 3 else []
        elif len(frequency) == 2:
            element_1, element_2 = list(frequency.keys())
            print(element_1, element_2)
            first, first_frequency, second, second_frequency = (
                element_1,
                0,
                element_2,
                0,
            )
            for num in nums:
                if num == first:
                    first_frequency += 1
                if num == second:
                    second_frequency += 1
            if first_frequency > len(nums) // 3 and second_frequency > len(nums) // 3:
                return [first, second]
            elif first_frequency > len(nums) // 3 or second_frequency > len(nums) // 3:
                return [first] if first_frequency > len(nums) // 3 else [second]
            else:
                return []
