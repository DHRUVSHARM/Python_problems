class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice_points, bob_points, left = 0, 0, 0

        for r in range(0, len(colors)):
            if r + 1 == len(colors) or colors[r] != colors[r + 1]:
                # a substring of the same color is stopped
                if colors[r] == "A":
                    # alice points
                    alice_points += max(0, (r - left + 1) - 2)
                    # print("alice : " , alice_points)
                else:
                    # bob points
                    bob_points += max(0, (r - left + 1) - 2)
                    # print("bob : " , bob_points)
                left = r + 1

        if alice_points == bob_points:
            return False
        else:
            if alice_points > bob_points:
                return True
            else:
                return False
