from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for detail in details:
            if (
                ord(detail[11]) - ord("0") > 6
                and ord(detail[12]) - ord("0") >= 0
                or ord(detail[11]) - ord("0") == 6
                and ord(detail[12]) - ord("0") > 0
            ):
                ans += 1

        return ans
