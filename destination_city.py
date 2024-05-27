from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        seen = set()
        for src, _ in paths:
            seen.add(src)

        for _, dest in paths:
            if dest not in seen:
                return dest
