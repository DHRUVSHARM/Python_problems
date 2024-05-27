class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        dp = {}

        def dfs(index, k, prev_char, prev_count):
            if index == len(s):
                # base case
                # keep the new char , breaking the streak
                res = float("inf")

                if k >= prev_count:
                    # can delete and make the entire thing zero
                    res = min(res, 0)

                if prev_count > 1 and k >= prev_count - 1:
                    res = min(
                        res,
                        1
                    )
                if prev_count >= 9 and k >= prev_count - 9:
                    res = min(
                        res,
                        2
                    )
                if prev_count >= 99 and k >= prev_count - 99:
                    res = min(
                        res,
                        3
                    )
                # cases for simple conversion
                if prev_count == 1:
                    res = min(
                        res,
                        1
                    )
                elif 2 <= prev_count <= 9:
                    res = min(
                        res,
                        2
                    )
                elif 10 <= prev_count <= 99:
                    res = min(
                        res,
                        3
                    )
                elif prev_count == 100:
                    res = min(
                        res,
                        4
                    )
                return res

            if (index, k, prev_char, prev_count) in dp:
                return dp[(index, k, prev_char, prev_count)]

            res = float("inf")
            if prev_char != s[index]:
                # now we have 2 different choices
                # delete , no change in the streak
                if k - 1 >= 0:
                    res = min(res, dfs(index + 1, k - 1, prev_char, prev_count))
                # keep the new char , breaking the streak
                if k >= prev_count:
                    # can delete and make the entire thing zero
                    res = min(
                        res,
                        0 + dfs(index + 1, k - prev_count, s[index], 1))
                if prev_count >= 1 and k >= prev_count - 1:
                    res = min(
                        res,
                        1 + dfs(index + 1, k - (prev_count - 1), s[index], 1)
                    )
                if prev_count >= 9 and k >= prev_count - 9:
                    res = min(
                        res,
                        2 + dfs(index + 1, k - (prev_count - 9), s[index], 1)
                    )
                if prev_count >= 99 and k >= prev_count - 99:
                    res = min(
                        res,
                        3 + dfs(index + 1, k - (prev_count - 99), s[index], 1)
                    )
                # cases for simple conversion
                if prev_count == 1:
                    res = min(
                        res,
                        1 + dfs(index + 1, k, s[index], 1)
                    )
                if 2 <= prev_count <= 9:
                    res = min(
                        res,
                        2 + dfs(index + 1, k, s[index], 1)
                    )
                elif 10 <= prev_count <= 99:
                    res = min(
                        res,
                        3 + dfs(index + 1, k, s[index], 1)
                    )
                elif prev_count == 100:
                    res = min(
                        res,
                        4 + dfs(index + 1, k, s[index], 1)
                    )
            else:
                # but here we only have one choice , that is to keep the character
                res = dfs(index + 1, k, prev_char, prev_count + 1)

            dp[(index, k, prev_char, prev_count)] = res
            return res

        return dfs(1, k, s[0], 1)