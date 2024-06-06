class Solution:
    def isPathCrossing(self, path: str) -> bool:
        gradients = {"N": (0, 1), "S": (0, -1), "W": (-1, 0), "E": (1, 0)}

        visited = set([(0, 0)])
        current_pos = tuple([0, 0])

        for i in range(0, len(path)):
            dx, dy = gradients[path[i]]
            current_pos = (current_pos[0] + dx, current_pos[1] + dy)
            # print(current_pos)
            if current_pos in visited:
                return True

            visited.add(current_pos)

        return False
