from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows , cols , dirs, initial_color , visited =  len(image) , len(image[0]) , [(-1 , 0) , (0 , -1) , (0 , 1) , (1 , 0)] , image[sr][sc] , set()

        def dfs(node):
            # color the node
            x , y = node
            image[x][y] = color
            visited.add((x , y))

            for dx , dy in dirs:
                newx , newy = x + dx , y + dy
                if 0 <= newx < rows and 0 <= newy < cols and (newx , newy) not in visited and image[newx][newy] == initial_color:
                    dfs((newx , newy))
                

        
        dfs((sr , sc))
        # return the transformed image
        return image