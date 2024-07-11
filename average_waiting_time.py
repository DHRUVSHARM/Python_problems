from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        ans, ct = 0, customers[0][0]
        for st, time in customers:
            # ans += abs(ct - st)
            if st >= ct:
                ct = st
            else:
                ans += ct - st

            ans += time
            ct += time
            print("current time : ", ct)

        return ans / len(customers)
