from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:

        # we will write a solution which is iterative o(n)
        curr, ans = 1, []

        while len(ans) < n:

            ans.append(curr)

            if curr * 10 <= n:
                curr = curr * 10
            else:
                while curr == n or (curr) % 10 == 9:
                    curr = curr // 10
                curr += 1

        return ans
