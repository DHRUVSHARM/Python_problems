import collections

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total = sum(skill)
        teams = len(skill) // 2

        seen = collections.defaultdict(int)
        ans = 0

        if total % teams == 0:
            target = total // teams
            # print("target : " , target)

            for element in skill:
                # print(seen)
                if target - element not in seen:
                    seen[element] += 1                    
                else:
                    seen[target - element] -= 1
                    if not seen[target - element]:
                        seen.pop(target - element)
                    ans += (element * (target - element))
        else:
            return -1

    
        return -1 if len(seen) else ans