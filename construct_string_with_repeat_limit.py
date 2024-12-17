import collections


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = collections.Counter(s)
        s = [[ord(k) - ord('a') , k , v] for k , v in freq.items()]
        s.sort()
        # print(s)

        result = []
        while len(s):
            _ , element , frequency = s.pop()
            # we reomove the element to be put first
            if frequency >= repeatLimit:
                result.append(element * repeatLimit)
                frequency -= repeatLimit
            else:
                # exhaust the frequency
                result.append(element * (frequency % repeatLimit))
                frequency = 0
            
            while len(s) and frequency:
                result.append(s[-1][1])
                s[-1][2] -= 1
                if frequency - repeatLimit >= 0:
                    result.append(element * repeatLimit)
                    frequency -= repeatLimit
                else:
                    result.append(element * (frequency % repeatLimit))
                    frequency = 0
                if not s[-1][2]:
                    s.pop()


        return "".join(result)

    
