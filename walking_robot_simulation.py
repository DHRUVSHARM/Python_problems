from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:

        ans = 0
        obstacle_set = {(x, y) for x, y in obstacles}

        # nesw moving right
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        curr_direction = 0
        curr_position = (0, 0)

        for command in commands:
            if command == -1:
                # right
                curr_direction = (curr_direction + 1) % 4
            elif command == -2:
                # left
                curr_direction = (curr_direction - 1 + 4) % 4
            else:
                # moving forward
                for _ in range(1, command + 1):
                    new_position = (
                        curr_position[0] + directions[curr_direction][0],
                        curr_position[1] + directions[curr_direction][1],
                    )
                    if new_position in obstacle_set:
                        break
                    else:
                        curr_position = new_position

                ans = max(ans, curr_position[0] ** 2 + curr_position[1] ** 2)

        return ans
