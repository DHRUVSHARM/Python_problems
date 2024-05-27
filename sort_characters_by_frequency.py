import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = collections.Counter(s)
        temp = []
        for key, value in frequency.items():
            temp.append((value, key))

        # sort based on frequency , decreasing
        temp.sort(key=lambda element: element[0], reverse=True)
        # each element is of the form frequency , element

        result = []
        for frequency , element in temp:
            while frequency:
                result.append(element)
                frequency -= 1
        # join is nice because of non - quadratic behaviour
        return "".join(result)
