from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m , n = len(box) , len(box[0])
        for i in range(0 , m):
            j , hash_index = n - 1 , n - 1
            while j >= 0:
                if box[i][j] == '.':
                    # we can move ahead. empty
                    pass
                elif box[i][j] == '*':
                    # this will be the new base, obstacle
                    hash_index = j - 1
                else:
                    # we need to swap
                    box[i][j] , box[i][hash_index] = box[i][hash_index] , box[i][j]
                    hash_index -= 1
                j -= 1
        
        """
        for i in range(0 , m):
            for j in range(0 , n):
                print(box[i][j] , end=" ")
            print("")
        """
        ans = [["" for _ in range(0 , m)] for _ in range(0 , n)]

        for i in range(0 , m):
            for j in range(0 , n):
                ans[j][m - 1 -i] = box[i][j]

        return ans 

