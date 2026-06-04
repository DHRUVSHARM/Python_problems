class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # for the zigzag we can consider a 2d list for the final solution 
        res = [[] for _ in range(numRows)]
        index = 0 # index over s 
        row_index = 0

        if len(res) == 1:
            return s

        while index < len(s):
            
            # top bottom
            while index < len(s) and row_index < len(res):
                res[row_index].append(s[index])
                index += 1
                row_index += 1

            # exceed move up to match and one less
            while row_index >= len(res) - 1:
                row_index -= 1

            # bottom up 
            while index < len(s) and row_index >= 0:
                res[row_index].append(s[index])
                index += 1
                row_index -= 1
            
            while row_index <= 0:
                row_index += 1

        # print(res)
        flat_res = []
        for subans in res:
            flat_res.append("".join(subans))
        
        return "".join(flat_res)