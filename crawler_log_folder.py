from typing import List

print("here ..")
a = "/d1"
b = "./"
c = "../"

print(a.split("/")[0])
print(b.split("/")[0])
print(c.split("/")[0])


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        step = 0
        for element in logs:
            curr = element.split("/")[0]
            if curr == "..":
                step = max(step - 1, 0)
            elif curr == ".":
                pass
            else:
                step = step + 1

        return step
