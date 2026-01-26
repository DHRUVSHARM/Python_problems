from typing import List
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        s = ["main"]

        for ops in logs:
            # print(ops)
            prefix =  ops.split("/")[0]
            # print(prefix)
            # print(s)

            if prefix == "..":
                if len(s) > 1:
                    # print("here")
                    s.pop()
            elif prefix == ".":
                pass
            else:
                s.append(prefix)
            
        # print(s)
        return len(s) - 1